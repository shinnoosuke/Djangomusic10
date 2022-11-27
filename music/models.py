from django.db import models

class instrument(models.Model):
    inst_name = models.CharField(max_length=50)
    inst_image = models.ImageField(blank=True, null=True)

class language(models.Model):
    language_name =  models.CharField(max_length=20)

class teaching_inst(models.Model):
    teaching_inst = models.ForeignKey(instrument, on_delete=models.CASCADE) 

class tl(models.Model):    
    teaching_lang = models.ForeignKey(language, on_delete=models.CASCADE) 

 #class movie(models.Model):
  #  prof_movie = models.movieField(movie, on_delete=models.CASCADE) 
  # 
class fee(models.Model):
    fee = models.IntegerField(max_length=3)

class academic(models.Model):
    academic = models.TextField()

class experience(models.Model):
    experience = models.TextField()

class certificate(models.Model):
    certificate = models.TextField()                  

class reputation(models.Model):
    reoutation = models.TextField()

class message(models.Model):
    message = models.TextField()

class oneword(models.Model):
    oneword = models.TextField()       

# Create your models here.