from rest_framework import serializers

from .models import Indicator, IndicatorEvidence


class IndicatorEvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorEvidence
        fields = ['id', 'name', 'description', 'indicator', 'file']


class IndicatorViewSerializer(serializers.ModelSerializer):
    evidence = IndicatorEvidenceSerializer(many=True, read_only=True)

    class Meta:
        # ALso handle indicator evidence here
        model = Indicator

        fields = ['id', 'name', 'description', 'item', 'evidence']


class IndicatorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        # ALso handle indicator evidence here
        model = Indicator
        fields = ['id', 'name', 'description', 'item']
