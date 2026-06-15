from rest_framework import serializers

from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Appeal

        fields = (
            'id',
            'category',
            'title',
            'description',
            'address',
            'image',
            'status',
            'created_at',
        )

        read_only_fields = (
            'status',
            'created_at',
        )