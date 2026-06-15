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

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appeals'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='appeals'
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    address = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to='appeals/',
        blank=True,
        null=True
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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title