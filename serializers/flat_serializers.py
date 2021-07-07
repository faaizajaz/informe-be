from rest_framework import serializers
from base_project.models import Project
from impact.models import Impact
from outcome.models import Outcome


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'long_description', 'short_description', 'impact']
        depth = 6


class ImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impact
        fields = ['id', 'short_description', 'long_description']


class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = ['id', 'short_description', 'long_description']
