from rest_framework import serializers
from base_project.models import Item, Project


class ItemSerializer(serializers.ModelSerializer):
    nodes = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            'short_description',
            'long_description',
            'parent',
            'nodes',
            'level',
            'item_type',
        ]

    def get_nodes(self, obj):
        return ItemSerializer(obj.get_children(), many=True).data


class ProjectSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'long_description', 'short_description', 'items']


# class ImpactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Impact
#         fields = ['id', 'short_description', 'long_description']
