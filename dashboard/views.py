from django.views.generic import TemplateView

from appeals.models import Appeal


class HomePageView(TemplateView):
    template_name = 'dashboard/home.html'


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_appeals'] = Appeal.objects.count()

        context['new_appeals'] = Appeal.objects.filter(
            status='new'
        ).count()

        context['in_progress_appeals'] = Appeal.objects.filter(
            status='in_progress'
        ).count()

        context['resolved_appeals'] = Appeal.objects.filter(
            status='resolved'
        ).count()

        return context