from django.shortcuts import render, redirect, get_object_or_404

from main.models import Experience
from main.forms import ExperienceForm
from django.core import serializers
from django.http import HttpResponse
def show_main(request):
    context = {
        "name": "Burhan",
        "npm": "2206000000",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    EXPERIENCE_CHOICES = ["internship", "research", "volunteer", "part-time", "full-time", "freelance"]
    
    
    experiences = Experience.objects.all()
    title_query = ""
    if request.method == "GET":
        title_query = request.GET.get("title", "").strip()
        category_query = request.GET.get("category", "").strip()
        experiences = experiences.filter(title__icontains=title_query, category__icontains=category_query)
    context = {
        "name": "Burhan",
        "experience_list": experiences,
        "title_query": title_query,
        "category_query": category_query,
        "experience_choices": EXPERIENCE_CHOICES
        
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    
    if request.method == "POST" or form.is_valid():
        form.save()
        return redirect("main:show_experience")
        
    context = {
        "name": "Burhan",
        "form": form
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        
    return redirect("main:show_experience")

def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")
    context = {
        "form": form
    }
    return render(request, "experience_form.html", context)

def get_experiences_json(request):
    experiences = Experience.objects.all()
  
    if experiences == None:
        return HttpResponse("Data tidak ada")
    
    experiences = serializers.serialize("json", experiences)
    return HttpResponse(experiences, content_type="application/json")


def show_experiences_from_json(request):
    experiences_json = get_experiences_json(request)
    
    experiences = serializers.deserialize("json", experiences_json.content.decode("utf-8"))
    experiences = [experience.object for experience in experiences] 