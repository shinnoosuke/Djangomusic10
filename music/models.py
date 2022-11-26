from django.db import models

class instrument(models.Model):
    inst_name = models.CharField(max_length=50)
    inst_image = models.ImageField(blank=True, null=True)

class language(models.Model):
    language_name =  models.CharField(max_length=20)   
# Create your models here.
