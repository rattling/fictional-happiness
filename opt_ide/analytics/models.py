from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Workflow(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="workflows"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.name}"


class Dataset(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="datasets"
    )
    file = models.FileField(upload_to="datasets/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dataset for {self.project.name}"
