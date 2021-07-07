from django.contrib import admin
from .models import Project, Impact, Outcome, Output

admin.site.register(Project)
admin.site.register(Impact)
admin.site.register(Outcome)
admin.site.register(Output)

# Register your models here.
