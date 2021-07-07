from drf_writable_nested.serializers import WritableNestedModelSerializer
from base_project.models import Impact, Outcome, Project
from serializers.flat_serializers import (
    ImpactSerializer,
    OutcomeSerializer,
    OutputSerializer,
)


class NestedProjectSerializer(WritableNestedModelSerializer):
    impact = ImpactSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'short_description', 'long_description', 'impact']


class NestedImpactSerializer(WritableNestedModelSerializer):
    outcome = OutcomeSerializer(many=True)

    class Meta:
        model = Impact
        fields = ['id', 'short_description', 'long_description', 'outcome']


class NestedOutcomeSerializer(WritableNestedModelSerializer):
    output = OutputSerializer(many=True)

    class Meta:
        model = Outcome
        fields = ['id', 'short_description', 'long_description', 'output']
