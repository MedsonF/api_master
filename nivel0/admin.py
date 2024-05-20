from django.contrib import admin
from nivel0.models import Nivel0

@admin.register(Nivel0)
class Nivel0Admin(admin.ModelAdmin):
    list_display = ('id', 'name')