from rest_framework import serializers
from .models import Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
        read_only_fields = ['owner']