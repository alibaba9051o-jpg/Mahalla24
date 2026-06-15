from django import forms
from .models import Appeal


class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = [
            'category',
            'title',
            'description',
            'address',
            'image',
        ]