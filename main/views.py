from django.shortcuts import render

# Create your views here.

from main.models import Projects

def show_projects(request):
    context = {
        "project_list": Projects.objects.all()
    }
    return render(request, 'project.html', context)