from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .forms import AppealForm
from .models import Appeal
from .serializers import AppealSerializer


class AppealCreateAPIView(generics.CreateAPIView):
    serializer_class = AppealSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppealCreatePageView(CreateView):
    model = Appeal
    form_class = AppealForm
    template_name = 'appeals/create.html'
    success_url = reverse_lazy('my-appeals')

    def form_valid(self, form):
        first_appeal = Appeal.objects.first()

        if first_appeal:
            form.instance.user = first_appeal.user

        return super().form_valid(form)


class AppealListPageView(TemplateView):
    template_name = 'appeals/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['appeals'] = Appeal.objects.all()

        return context