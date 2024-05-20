from django.contrib import admin
from nivel5.models import Nivel5

@admin.register(Nivel5)
class Nivel5Admin(admin.ModelAdmin):
    list_display = ('id', 'name')