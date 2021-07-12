# from drf_writable_nested.serializers import WritableNestedModelSerializer

# from base_project.models import Project


# class NestedProjectSerializer(WritableNestedModelSerializer):
#     impact = ImpactSerializer(many=True)

#     class Meta:
#         model = Project
#         fields = ['id', 'name', 'short_description', 'long_description', 'impact']


# class NestedImpactSerializer(WritableNestedModelSerializer):
#     outcome = OutcomeSerializer(many=True)

#     class Meta:
#         model = Impact
#         fields = ['id', 'short_description', 'long_description', 'outcome']
