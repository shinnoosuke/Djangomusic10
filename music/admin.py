from django.contrib import admin
from .models import instrument, teaching_inst, teaching_langage, Teacher, language

admin.site.register(instrument)
admin.site.register(language)
admin.site.register(teaching_inst)
admin.site.register(teaching_langage)
admin.site.register(Teacher)
#admin.site.register(teacher_picture)

# Register your models here.
