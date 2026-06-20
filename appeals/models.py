from django.conf import settings
from django.db import models

from categories.models import Category


class Appeal(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    )

    PRIORITY_CHOICES = (
        ('normal', 'Oddiy'),
        ('medium', 'Zarur'),
        ('urgent', 'Shoshilinch'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    address = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='appeals/',
        blank=True,
        null=True
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='normal'
    )

    keywords = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title