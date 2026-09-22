from django.forms import ModelForm
from main.models import Projects


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ["title", "description", "url", "thumbnail", "stars"]
        
   