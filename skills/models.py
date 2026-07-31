from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    level = models.CharField(max_length=30, default="Learning")

    def __str__(self):
        return self.name