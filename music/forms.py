from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    model = Teacher
    fields = ["movie","fee","academic","experience","certificate","reputation","message","oneword","lang","inst","year","revel","pic"] #TODO: ここにTeacherのバリデーション対象のフィールドを書く
