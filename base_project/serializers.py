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
            'nodes',
            'organization',
        ]


#########################################################################
# THESE TWO SERIALIZERS NEEDED FOR FLAT REPR OF ITEMS UNDER PROJ ########


class ItemsFlatSerializer(serializers.ModelSerializer):
    indicator = IndicatorViewSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'long_description', 'level', 'indicator']


class ProjectItemsFlatSerializer(serializers.ModelSerializer):
    nodes = ItemsFlatSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'long_description', 'organization', 'nodes']


#########################################################################


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
        """Updates the Organization instance"""
        # TODO: Check if new_owner exists in instance.owner. This can be used to add and delete owners.

        # PATCH request comes with a 'for' parameter.
        selection = self.context['request'].data.get('for')

        # Add or remove based on the 'for' parameter
        if selection == 'add':
            instance = self.add_owner(instance, validated_data)
            return instance
        elif selection == 'remove':
            instance = self.remove_from_all(instance, validated_data)
            return instance
        elif selection == 'remove-owner':
            instance = self.remove_from_owner(instance, validated_data)
            return instance

    def add_owner(self, instance, validated_data):
        """
        Adds a new owner to the Organization instance.
        Also adds the same user as a reporter since all owners should be reporters.
        """
        new_owner = validated_data['owner'][0]
        instance.owner.add(new_owner.id)
        instance.member.add(new_owner.id)
        instance.save()
        return instance

    def remove_from_all(self, instance, validated_data):
        """
        Removes a user from Org owner and member roles. Also removes
        the user from all Org projects (as owner and reporter).
        """
        person = validated_data['owner'][0]

        # Remove user from owners and members
        instance.owner.remove(person.id)
        instance.member.remove(person.id)

        # Remove user from org's projects
        for proj in instance.project.all():
            for owner in proj.owner.all():
                if person.username == owner.username:
                    proj.owner.remove(person.id)
            for reporter in proj.reporter.all():
                if person.username == reporter.username:
                    proj.reporter.remove(person.id)

        # Save Organization instance and return
        instance.save()
        return instance

    def remove_from_owner(self, instance, validated_data):
        person = validated_data['owner'][0]

        instance.owner.remove(person.id)
        instance.save()
        return instance


# NOTE: We don't need this serializer since member adding is handled in the invitation
# handling view
#
# class OrgMemberEditSerializer(serializers.ModelSerializer):


class ProjectOwnerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['owner']

    # To automatically set the new owner as a member
    def update(self, instance, validated_data):
        # TODO: Check if new_owner exists in instance.owner. This can be used to add and delete owners.
        new_owner = validated_data['owner'][0]
        instance.owner.add(new_owner.id)
        instance.reporter.add(new_owner.id)
        instance.save()
        return instance


class ProjectReporterEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['reporter']

    def update(self, instance, validated_data):
        # TODO: Check if new_owner exists in instance.owner. This can be used to add and delete owners.
        selection = self.context['request'].data.get('for')

        if selection == 'add':
            instance = self.add_reporter(instance, validated_data)
            return instance
        elif selection == 'remove':
            instance = self.remove_from_all(instance, validated_data)
            return instance

    def add_reporter(self, instance, validated_data):
        new_reporter = validated_data['reporter'][0]
        instance.reporter.add(new_reporter.id)
        instance.save()
        return instance

    # ALERT: This is terrible. But since you would never remove a reporter while still
    # retaining that person as an owner, we have a single remove_from_all method that
    # takes care of both removing the person from reporters, and from owners. If you want
    # to remove a person as reporter without removing as owner, tough shit, you'll have to
    # remove from both and then add as a reporter manually

    def remove_from_all(self, instance, validated_data):
        reporter = validated_data['reporter'][0]
        instance.reporter.remove(reporter.id)
        instance.owner.remove(reporter.id)
        instance.save()
        return instance
