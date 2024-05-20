from django.contrib import admin
from nivel4.models import Nivel4

@admin.register(Nivel4)
class Nivel4Admin(admin.ModelAdmin):
    list_display = ('id', 'name')