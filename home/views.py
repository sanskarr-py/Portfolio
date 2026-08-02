from django.shortcuts import render
from skills.models import Skill
from projects.models import Project
from contact.forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect

def home(request):

    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
              request,
              "Your message has been sent successfully!"
           )

            return redirect(f"{request.path}#contact")
    else:

        form = ContactForm()

    context = {
        "featured_projects": featured_projects,
        "skills": skills,
        "form": form,
    }

    return render(request, "home/index.html", context)