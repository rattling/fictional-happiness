from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Workflow, Dataset

admin.site.register(Project)
admin.site.register(Workflow)
admin.site.register(Dataset)
