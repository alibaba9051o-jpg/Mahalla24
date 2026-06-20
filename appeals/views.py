from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from openai import OpenAI

from .forms import AppealForm
from .models import Appeal
from .serializers import AppealSerializer


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


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

        prompt = f"""
Murojaatni tahlil qil.

Muhimlik darajasini aniqla:
normal = oddiy
medium = zarur
urgent = shoshilinch

Kalit so'zlarni ajrat.

Faqat quyidagi formatda javob qaytar:

priority: normal
keywords: suv, quvur, ta'mirlash

Murojaat:

{form.instance.description}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

        try:
            lines = result.split('\n')

            priority = lines[0].split(':')[1].strip()
            keywords = lines[1].split(':')[1].strip()

            form.instance.priority = priority
            form.instance.keywords = keywords

        except:
            form.instance.priority = 'normal'
            form.instance.keywords = ''

        return super().form_valid(form)


class AppealListPageView(TemplateView):
    template_name = 'appeals/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['appeals'] = Appeal.objects.all()

        return context