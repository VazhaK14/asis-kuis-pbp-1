from django.forms import ModelForm
from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        models = Experience
        fields = ["title", "description", "category", "thumbnail"]
        
        labels = {
            "title": "Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "Momen Pengalaman"
        }
        
        
            
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # title = models.CharField(max_length=255)
    # description = models.TextField()
    # category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    # thumbnail = models.URLField(blank=True, null=True)
    # started_at = models.DateTimeField(auto_now_add=True)
    # ended_at = models.DateTimeField(blank=True, null=True)