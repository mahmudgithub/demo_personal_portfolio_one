from django.db import models

class project(models.Model):
    Title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='portfolio/image/')
    url=models.URLField(blank=True)