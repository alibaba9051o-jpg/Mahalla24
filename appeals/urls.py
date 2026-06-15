from django.urls import path

from .views import AppealCreateAPIView

urlpatterns = [
    path(
        '',
        AppealCreateAPIView.as_view(),
        name='appeal-create'
    ),
]