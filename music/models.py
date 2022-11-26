from django.db import models

class instrument(models .Model):
    inst_name = models.CharField(max_length=50)
    inst_image = models.ImageField(blank=True, null=True)
# Create your models here.
