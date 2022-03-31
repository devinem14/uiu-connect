from django.db import models

# Create your models here.

class Courses (models.Model):
    name = models.CharField(max_length=300)
    prerequisites = models.CharField(max_length=300, blank=True)
