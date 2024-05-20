from django.contrib import admin
from nivel3.models import Nivel3

@admin.register(Nivel3)
class Nivel3Admin(admin.ModelAdmin):
    list_display = ('id', 'name')