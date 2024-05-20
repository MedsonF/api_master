import csv
from django.core.management.base import BaseCommand
from categoria.models import PlanoFinanceiro
from nivel0.models import Nivel0
from nivel1.models import Nivel1
from nivel2.models import Nivel2
from nivel3.models import Nivel3
from nivel4.models import Nivel4
from nivel5.models import Nivel5


class Command(BaseCommand):
    help = 'Comando para importar lista de Planos Financeiros.'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Nome do arquivo CSV na raiz do projeto.')

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                codigo = row['\ufeffcategoria']
                plano_fin_nome = row['plano_fin']
                nivel1_nome = row['nivel1']
                nivel2_nome = row['nivel2']
                nivel3_nome = row['nivel3']
                nivel4_nome = row['nivel4']
                nivel5_nome = row['nivel5']

                self.stdout.write(self.style.NOTICE(codigo))

                plano_fin, created = Nivel0.objects.get_or_create(name=plano_fin_nome)
                nivel1, created = Nivel1.objects.get_or_create(name=nivel1_nome)
                nivel2, created = Nivel2.objects.get_or_create(name=nivel2_nome)
                nivel3, created = Nivel3.objects.get_or_create(name=nivel3_nome)
                nivel4, created = Nivel4.objects.get_or_create(name=nivel4_nome)
                nivel5 = None
                if nivel5_nome:
                    nivel5, created = Nivel5.objects.get_or_create(name=nivel5_nome)

                PlanoFinanceiro.objects.create(codigo=codigo, plano_fin=plano_fin, 
                                               nivel1=nivel1, nivel2=nivel2, nivel3=nivel3, 
                                               nivel4=nivel4, nivel5=nivel5)

            self.stdout.write(self.style.SUCCESS('PLANOS FINANCEIROS IMPORTADOS COM SUCESSO!'))



