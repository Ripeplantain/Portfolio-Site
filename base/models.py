from django.db import models

# Create your models here.
class Project(models.Model):
    """
        Attribute:- id,  name, description
        Methods:- def __str__
    """
    name = models.CharField(max_length=200)
    description = models.CharField(null=True, max_length=200)
    image = models.ImageField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
        Attribute:- id, body, project
        Methods:- def __str__
    """
    body = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.project