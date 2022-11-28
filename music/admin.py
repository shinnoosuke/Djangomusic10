from django.contrib import admin
from .models import instrument, teaching_inst, teaching_langage, fee, academic, experience, certificate, reputation, message, oneword, language

admin.site.register(instrument)
admin.site.register(language)
admin.site.register(teaching_inst)
admin.site.register(teaching_langage)
admin.site.register(fee)
admin.site.register(academic)
admin.site.register(experience)
admin.site.register(certificate)
admin.site.register(reputation)
admin.site.register(message)
admin.site.register(oneword)

#admin.site.register()

# Register your models here.
