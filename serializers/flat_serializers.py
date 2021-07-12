from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from base_project.models import Item, Project

# TODO: There will be 2 item serializers. One to view, and one nested to PATCH


class ItemViewSerializer(serializers.ModelSerializer):
    nodes = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            'id',
            'project',
            'level',
            'item_type',
            'parent',
            'short_description',
            'long_description',
            'nodes',
        ]

    def get_nodes(self, obj):
        return ItemViewSerializer(obj.get_children(), many=True).data


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'level',
            'parent',
            'item_type',
            'short_description',
            'long_description',
        ]


class NestedItemSerializer(WritableNestedModelSerializer):
    parent = ItemUpdateSerializer()

    class Meta:
        model = Item
        fields = [
            'id',
            'level',
            'parent',
            'item_type',
            'short_description',
            'long_description',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    items = ItemViewSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'long_description', 'short_description', 'items']


# class ImpactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Impact
#         fields = ['id', 'short_description', 'long_description']
