from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField()

    technologies = models.CharField(
        max_length=255,
        default="Python",
        help_text="Example: Python, Django, SQLite"
    )

    github_url = models.URLField()

    live_demo = models.URLField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    featured = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Technology(models.Model):
    name = models.CharField(max_length=50)
technologies = models.ManyToManyField(Technology)