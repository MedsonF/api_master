from django.contrib import admin
from categoria.models import PlanoFinanceiro


@admin.register(PlanoFinanceiro)
class PlanoFinanceiroModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'plano_fin', 'nivel1', 'nivel2', 'nivel3', 'nivel4', 'nivel5')