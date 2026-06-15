from django.contrib import admin

from .models import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'category',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'category',
    )

    search_fields = (
        'title',
        'description',
        'address',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )