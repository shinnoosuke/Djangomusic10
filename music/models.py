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

class User(models.Model):
    movie = models.URLField(max_length=200, null=True, blank=True)
    fee = models.IntegerField()
    academic = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    certificate = models.TextField(max_length=500)
    reputation = models.TextField(max_length=500)
    message = models.TextField(max_length=500)
    oneword = models.TextField(max_length=500)

 