from django.contrib import admin
from django.utils.html import format_html

from .models import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'category',
        'priority_badge',
        'status',
        'created_at',
    )

    list_filter = (
        'priority',
        'status',
        'category',
    )

    search_fields = (
        'title',
        'description',
        'address',
        'keywords',
    )

    readonly_fields = (
        'priority',
        'keywords',
        'created_at',
        'updated_at',
    )

    def priority_badge(self, obj):
        colors = {
            'normal': '#ffffff',
            'medium': '#ffc107',
            'urgent': '#dc3545',
        }

        texts = {
            'normal': 'Oddiy',
            'medium': 'Zarur',
            'urgent': 'Shoshilinch',
        }

        text_color = 'black'
        if obj.priority == 'urgent':
            text_color = 'white'

        return format_html(
            '<span style="background:{}; color:{}; padding:5px 10px; border-radius:8px;">{}</span>',
            colors[obj.priority],
            text_color,
            texts[obj.priority]
        )

    priority_badge.short_description = 'Muhimlik'