from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from main.models import Projects
from main.forms import ProjectsForm

def show_projects(request):
    context = {
        "project_list": Projects.objects.all()
    }
    return render(request, 'project.html', context)

def add_star(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    
    if request.method == "POST":
        project.increment_stars()
        
    return redirect("projects")