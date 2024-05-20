from django.contrib import admin
from nivel2.models import Nivel2

@admin.register(Nivel2)
class Nivel2Admin(admin.ModelAdmin):
    list_display = ('id', 'name')