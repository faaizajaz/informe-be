from account.models import CustomUser
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from base_project.models import Item, Project
from indicator.models import IndicatorEvidence, Indicator


# TODO: Separate serializers into files--or maybe not since they are all related
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


class ItemViewSerializer(serializers.ModelSerializer):
    nodes = serializers.SerializerMethodField()
    indicator = IndicatorViewSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = [
            'id',
            'project',
            'level',
            'is_project',
            'name',
            'parent',
            'long_description',
            'nodes',
            'indicator',
        ]

    def get_nodes(self, obj):
        return ItemViewSerializer(obj.get_children(), many=True).data


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'level', 'parent', 'name', 'long_description']


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'long_description', 'parent']


class ItemProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id']


class NestedItemSerializer(WritableNestedModelSerializer):
    parent = ItemUpdateSerializer()
    project = ItemProjectUpdateSerializer()

    class Meta:
        model = Item
        fields = ['id', 'project', 'level', 'parent', 'name', 'long_description']


class NestedProjectSerializer(serializers.ModelSerializer):
    nodes = ItemViewSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = [
            'id',
            'level_config',
            'owner',
            'reporter',
            'name',
            'long_description',
            'name',
            'nodes',
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'long_description', 'level_config', 'owner', 'reporter']


class ProjectEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['level_config']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
