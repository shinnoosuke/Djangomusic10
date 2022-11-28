from django.db import models

class instrument(models.Model):
    inst_name = models.CharField(max_length=50)
    inst_image = models.ImageField(blank=True, null=True)
    #inst_category = models.CharField(max_length=20)

    def __str__(self):
        return self.inst_name

class language(models.Model):
    language_name =  models.CharField(max_length=20)

class teaching_inst(models.Model):
    teaching_inst   = models.ForeignKey(instrument, related_name="teaching_inst" ,  on_delete=models.CASCADE, null=True, blank=True) 
    teaching_inst1  = models.ForeignKey(instrument, related_name="teaching_inst1",  on_delete=models.CASCADE, null=True, blank=True)
    teaching_inst2  = models.ForeignKey(instrument, related_name="teaching_inst2",  on_delete=models.CASCADE, null=True, blank=True)
    teaching_inst3  = models.ForeignKey(instrument, related_name="teaching_inst3",  on_delete=models.CASCADE, null=True, blank=True)


    #year = models.IntegerField()
    #revel = models.IntegerField()

class teaching_langage(models.Model):    
    teaching_lang = models.ForeignKey(language, on_delete=models.CASCADE) 


 #class movie(models.Model):
  #  prof_movie = models.movieField(movie, on_delete=models.CASCADE) 
  # 
class fee(models.Model):
    fee = models.IntegerField()

class academic(models.Model):
    academic = models.TextField(max_length=500)

class experience(models.Model):
    experience = models.TextField(max_length=500)

class certificate(models.Model):
    certificate = models.TextField(max_length=500)                  

class reputation(models.Model):
    reoutation = models.TextField(max_length=500)

class message(models.Model):
    message = models.TextField(max_length=500)

class oneword(models.Model):
    oneword = models.TextField(max_length=500)

  

# Create your models here.