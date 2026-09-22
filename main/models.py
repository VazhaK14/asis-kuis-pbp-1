import uuid
from django.db import models


class Projects(models.Model):
    # implement here
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    thumbnail = models.URLField(blank=True, null=True)
    stars = models.PositiveIntegerField(default=0)
    
    @property
    def is_popular(self):
        return self.stars > 50
    
    def increment_stars(self):
        self.stars += 1
        self.save()
    