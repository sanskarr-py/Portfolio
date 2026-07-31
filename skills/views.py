from django.shortcuts import render
from .models import Skill


def skills(request):
    skills = Skill.objects.all()

    return render(request, "index.html", {
        "skills": skills
    })