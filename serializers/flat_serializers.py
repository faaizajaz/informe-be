from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from base_project.models import Item, Project

# TODO: rename this module to just serializers


class ItemViewSerializer(serializers.ModelSerializer):
    nodes = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            'id',
            'project',
            'level',
            'item_type',
            'name',
            'parent',
            'long_description',
            'nodes',
        ]

    def get_nodes(self, obj):
        return ItemViewSerializer(obj.get_children(), many=True).data


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'level', 'parent', 'item_type', 'name', 'long_description']


class ItemProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id']


class NestedItemSerializer(WritableNestedModelSerializer):
    parent = ItemUpdateSerializer()
    project = ItemProjectUpdateSerializer()

    class Meta:
        model = Item
        fields = [
            'id',
            'project',
            'level',
            'parent',
            'item_type',
            'name',
            'long_description',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    items = ItemViewSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'long_description', 'name', 'items']
