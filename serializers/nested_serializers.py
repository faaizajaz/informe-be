from drf_writable_nested.serializers import WritableNestedModelSerializer
from base_project.models import Impact, Outcome
from serializers.flat_serializers import OutcomeSerializer


class NestedImpactSerializer(WritableNestedModelSerializer):
    outcome = OutcomeSerializer(many=True)

    class Meta:
        model = Impact
        fields = ['id', 'short_description', 'long_description', 'outcome']
