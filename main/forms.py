from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail"]
        
        labels = {
            "title": "Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "Momen Pengalaman"
        }
        
        
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "https://drive.google.com/thumbnail?id=...&zw=1000w",
                }
            ),
        }