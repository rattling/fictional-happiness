from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Dataset
from .forms import ProjectForm, WorkflowForm, DatasetForm


# Define a view to list all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, "analytics/project_list.html", {"projects": projects})


# Define a view to create a new project
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "analytics/project_form.html", {"form": form})


# Iteration 2: Define a view to create a workflow for a project
def workflow_create(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        form = WorkflowForm(request.POST)
        if form.is_valid():
            workflow = form.save(commit=False)
            workflow.project = project
            workflow.save()
            return redirect("project_list")
    else:
        form = WorkflowForm()
    return render(
        request, "analytics/workflow_form.html", {"form": form, "project": project}
    )


# Define a view to upload a dataset for a project
def dataset_upload(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.project = project
            dataset.save()
            return redirect("project_list")
    else:
        form = DatasetForm()
    return render(
        request, "analytics/dataset_form.html", {"form": form, "project": project}
    )


# Define a view to list and view uploaded datasets for a project
def dataset_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    datasets = project.datasets.all()
    return render(
        request,
        "analytics/dataset_list.html",
        {"project": project, "datasets": datasets},
    )


# Define a view to display the contents of a dataset
def dataset_view(request, dataset_id):
    dataset = get_object_or_404(Dataset, id=dataset_id)
    import pandas as pd
    import os

    # Load the CSV file and convert it to HTML for display
    file_path = dataset.file.path
    if os.path.exists(file_path) and file_path.endswith(".csv"):
        df = pd.read_csv(file_path, sep="\t")
        table_html = df.to_html()
    else:
        table_html = "<p>File not found or not a valid CSV.</p>"

    return render(
        request,
        "analytics/dataset_view.html",
        {"dataset": dataset, "table_html": table_html},
    )
