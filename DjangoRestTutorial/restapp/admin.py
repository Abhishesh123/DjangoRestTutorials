from django.contrib import admin


from restapp.models import *

admin.site.register(Question)

class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ('id','question','choice_text','votes',)
admin.site.register(Choice,ChoiceAdmin)
