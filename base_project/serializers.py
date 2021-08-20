from account.serializers import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from indicator.serializers import IndicatorViewSerializer
from rest_framework import serializers

from .models import Item, Organization, Project


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
    owner = UserSerializer(many=True, required=False, read_only=True)
    reporter = UserSerializer(many=True, required=False, read_only=True)

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
            'organization',
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'long_description', 'level_config', 'owner', 'reporter']


class ProjectEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['level_config']


class OrgListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name']


class OrgCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'description']


class OrgOwnerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['owner']

    # To automatically set the new owner as a member
    def update(self, instance, validated_data):
        # TODO: Check if new_owner exists in instance.owner. This can be used to add and delete owners.
        new_owner = validated_data['owner'][0]
        instance.owner.add(new_owner.id)
        instance.member.add(new_owner.id)
        instance.save()
        return instance


class OrgMemberEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['member']


class ProjectOwnerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['owner']

    # To automatically set the new owner as a member
    def update(self, instance, validated_data):
        # TODO: Check if new_owner exists in instance.owner. This can be used to add and delete owners.
        new_owner = validated_data['owner'][0]
        instance.owner.add(new_owner.id)
        instance.member.add(new_owner.id)
        instance.save()
        return instance


class ProjectReporterEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['reporter']
