from django.db import models
from django.conf import settings
from accounts.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class instrument(models.Model):
    inst_name = models.CharField(max_length=50)
    inst_image = models.ImageField(blank=True, null=True)
    #inst_category = models.CharField(max_length=20)
    #TODO:AUTH_USER_MODELにカスタムユーザーモデルの在り処が書いてあるので、settingsから呼び出し、1対多を組む
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="ユーザー", on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return self.inst_name

class language(models.Model):
    language_name =  models.CharField(max_length=20)

class teaching_inst(models.Model):
    teaching_inst   = models.ForeignKey(instrument, related_name="teaching_inst" ,  on_delete=models.CASCADE, null=True, blank=True) 
    #teaching_inst1  = models.ForeignKey(instrument, related_name="teaching_inst1",  on_delete=models.CASCADE, null=True, blank=True)
    #teaching_inst2  = models.ForeignKey(instrument, related_name="teaching_inst2",  on_delete=models.CASCADE, null=True, blank=True)
    #teaching_inst3  = models.ForeignKey(instrument, related_name="teaching_inst3",  on_delete=models.CASCADE, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    revel = models.IntegerField(null=True, blank=True)
class teaching_langage(models.Model):    
    teaching_lang = models.ForeignKey(language, on_delete=models.CASCADE) 

#class teacher_picture
#    image = models.ImageField(_('image'), blank=True, null=True)    

class  Teacher(models.Model):
    movie = models.URLField(max_length=200, null=True, blank=True)
    #fee = models.IntegerField()
    #fee = models.IntegerField()
    #この場合、feeには0から3までの数値だけ入力が許される。
    fee = models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(3)] , null=True, blank=True)
    academic = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    certificate = models.TextField(max_length=500)
    #reputation = models.TextField(max_length=500)
    message = models.TextField(max_length=500)
    oneword = models.TextField(max_length=500)
    lang = models.ForeignKey(teaching_langage, on_delete=models.CASCADE, null=True, blank=True)
    inst = models.ForeignKey(teaching_inst, on_delete=models.CASCADE, null=True, blank=True)
    #pic = models.ForeignKey(teacher_picture, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='email')

