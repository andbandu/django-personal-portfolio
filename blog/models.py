from django.db import models

class Blog(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    date = models.DateField()
