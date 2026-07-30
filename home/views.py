from django.shortcuts import render
from projects.models import Project


def home(request):
    featured_projects = Project.objects.filter(featured=True)

    return render(
        request,
        "home/index.html",
        {
            "featured_projects": featured_projects,
        },
    )