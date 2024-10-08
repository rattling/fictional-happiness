from django import forms
from .models import Project, Workflow, Dataset


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]


# Iteration 2: 5.2 Create Forms in 'analytics/forms.py' to Handle Input
class WorkflowForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ["name", "description"]


# Form to handle dataset upload
class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ["file"]


# Step 6: Add URLs for the Views
# Define URLs for listing, creating projects, workflows, and uploading datasets in 'analytics/urls.py'
