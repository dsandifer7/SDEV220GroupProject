from django.db import models

class URL(models.Model): # collects URL from user

    name = models.CharField(max_length=100)
    url = models.URLField()
    image_path = models.CharField(max_length= 100, null = True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null = True, blank=True )

    def __str__(self):
        return self.name