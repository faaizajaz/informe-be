from django.contrib import admin

from .models import Item, Organization, Project

admin.site.register(Project)
admin.site.register(Item)
admin.site.register(Organization)

# Register your models here.
