from django.forms import ModelForm
from .models import Projects

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = ["title", "url", "thumbnail", "stars"]


