from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from main.models import Projects
from main.forms import ProjectsForm

def show_projects(request):
    projects = Projects.objects.all()

    if request.method == "GET":
        title_query = request.GET.get("title", "").strip() 
        projects = projects.filter(title__icontains=title_query)

    context = {
        "project_list":  projects
    }
    return render(request, 'project.html', context)

def add_star(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)

    if request.method == "POST":
        project.increment_stars()


    return redirect("projects")

def create_project(request):
    form = ProjectsForm(request.POST or None)

    if request.method == "POST" or form.is_valid():
        form.save()
        return redirect('projects')

    context =  {
        "form": form
    }

    return render(request, "project_form.html", context) 

def delete_project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    
    if request.method == "POST":
        project.delete()
        
    return redirect("projects")

def edit_project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    form = ProjectsForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("projects")
    
    context = {
        "form": form
    }
    return render(request, "project_form.html", context)