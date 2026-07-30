from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    # technologies = models.CharField(
    #     max_length=255,
    #     help_text="Example: Python, Django, MySQL"
    # )

    github_url = models.URLField()

    # live_demo = models.URLField(
    #     blank=True,
    #     null=True
    # )

    # image = models.ImageField(
    #     upload_to="projects/",
    #     blank=True,
    #     null=True
    # )

    featured = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title