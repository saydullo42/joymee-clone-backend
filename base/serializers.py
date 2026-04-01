from rest_framework import serializers
from .models import BaseModel


class BaseSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M', read_only=True)

    class Meta:
        model = BaseModel
        fields = '__all__'

