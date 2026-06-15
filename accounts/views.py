from django.views.generic import TemplateView

from rest_framework import generics

from .models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
serializer_class = RegisterSerializer

class LoginPageView(TemplateView):
    template_name = 'accounts/login.html'

class RegisterPageView(TemplateView):
    template_name = 'accounts/register.html'
