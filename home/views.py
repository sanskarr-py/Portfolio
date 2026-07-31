from django.shortcuts import render
from skills.models import Skill
from projects.models import Project

def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()

    context = {
        "featured_projects": featured_projects,
        "skills": skills,
    }

    return render(request, "home/index.html", context)