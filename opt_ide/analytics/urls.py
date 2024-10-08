from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("create/", views.project_create, name="project_create"),
    path(
        "project/<int:project_id>/workflow/create/",
        views.workflow_create,
        name="workflow_create",
    ),
    path(
        "project/<int:project_id>/dataset/upload/",
        views.dataset_upload,
        name="dataset_upload",
    ),
    path("project/<int:project_id>/datasets/", views.dataset_list, name="dataset_list"),
    path("dataset/<int:dataset_id>/view/", views.dataset_view, name="dataset_view"),
]
