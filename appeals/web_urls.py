from django.urls import path

from .views import AppealCreatePageView, AppealListPageView

urlpatterns = [
path(
'appeal/create/',
AppealCreatePageView.as_view(),
name='appeal-create-page'
),

path(
    'my-appeals/',
    AppealListPageView.as_view(),
    name='my-appeals'
),

]
