from django.contrib import admin
from .models import instrument, language, teaching_inst, teaching_language

admin.site.register(instrument)
admin.site.register(language)
admin.site.register(teaching_inst)
admin.site.register(teaching_language)

# Register your models here.
