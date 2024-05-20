from django.db import models
from nivel0.models import Nivel0
from nivel1.models import Nivel1
from nivel2.models import Nivel2
from nivel3.models import Nivel3
from nivel4.models import Nivel4
from nivel5.models import Nivel5

class PlanoFinanceiro(models.Model):
    codigo = models.CharField(max_length=25)
    plano_fin = models.ForeignKey(Nivel0, on_delete=models.PROTECT, related_name='nivel0')
    nivel1 = models.ForeignKey(Nivel1, on_delete=models.PROTECT, related_name='nivel1')
    nivel2 = models.ForeignKey(Nivel2, on_delete=models.PROTECT, related_name='nivel2')
    nivel3 = models.ForeignKey(Nivel3, on_delete=models.PROTECT, related_name='nivel3')
    nivel4 = models.ForeignKey(Nivel4, on_delete=models.PROTECT, related_name='nivel4')
    nivel5 = models.ForeignKey(Nivel5, on_delete=models.PROTECT, related_name='nivel5', null=True, blank=True)

    def __str__(self):
        return f'{self.codigo} - {self.plano_fin}'