from rest_framework import serializers
from .models import Project
from impact.serializers import ImpactSerializer
import json


class ProjectSerializer(serializers.ModelSerializer):
    impact = ImpactSerializer(read_only=False)

    class Meta:
        model = Project
        fields = ['id', 'name', 'impact', 'short_description', 'long_description']
        # depth = 6
