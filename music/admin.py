from django.contrib import admin
from .models import instrument, language, teaching_inst, tl, fee, academic, experience, certificate, reputation, message, oneword

admin.site.register(instrument)
admin.site.register(language)
admin.site.register(teaching_inst)
admin.site.register(tl)
admin.site.register(fee)
admin.site.register(academic)
admin.site.register(experience)
admin.site.register(certificate)
admin.site.register(reputation)
admin.site.register(message)
admin.site.register(oneword)

#admin.site.register()

# Register your models here.
