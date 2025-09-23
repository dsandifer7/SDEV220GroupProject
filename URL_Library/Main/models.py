from django.db import models

class URL(models.Model): # collects URL from user

    name = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to='qr_codes/') 
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()