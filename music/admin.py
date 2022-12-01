from django.contrib import admin
from .models import instrument, teaching_inst, teaching_langage, User, language

admin.site.register(instrument)
admin.site.register(language)
admin.site.register(teaching_inst)
admin.site.register(teaching_langage)
admin.site.register(User)

# Register your models here.
