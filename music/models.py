from django.db import models

class instrument(models.Model):
    inst_name = models.CharField(max_length=50)
    inst_image = models.ImageField(blank=True, null=True)

class language(models.Model):
    language_name =  models.CharField(max_length=20)

class teaching_inst(models.Model):
    teaching_inst = models.ForeignKey(instrument, on_delete=models.CASCADE) 

class teathing_language(models.Model):    
    teaching_inst = models.ForeignKey(language, on_delete=models.CASCADE) 

# Create your models here.