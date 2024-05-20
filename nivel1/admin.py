from django.contrib import admin
from nivel1.models import Nivel1

@admin.register(Nivel1)
class Nivel1Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
