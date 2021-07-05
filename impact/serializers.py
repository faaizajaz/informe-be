from rest_framework import serializers
from .models import Impact


class ImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impact
        fields = ['id', 'short_description', 'long_description']
