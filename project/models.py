from django.db import models

# Create your models here.
class Cv(models.Model):
    """Attributes : id file"""
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title
