from django.contrib.auth.models import User
from django.db import models


"""
Classes necessárias:
    usuario
    clientes 
    funcionarios
    locador
    fornecedores
    produtos
    vendas
    agenda
    procedimentos
   
"""


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    ESTADOS = {
        "AC" : "Acre",
        "AL" : "Alagoas",
        "AP" : "Amapá",
        "AM" : "Amazonas",
        "BA" : "Bahia",
        "CE" : "Ceará",
        "DF" : "Distrito Federal",
        "ES" : "Espírito Santo",
        "GO" : "Goiás",
        "MA" : "Maranhão",
        "MT" : "Mato Grosso",
        "MS" : "Mato Grosso do Sul",
        "MG" : "Minas Gerais",
        "PA" : "Pará",
        "PB" : "Paraíba",
        "PR" : "Paraná",
        "PE" : "Pernambuco",
        "PI" : "Piauí",
        "RJ" : "Rio de Janeiro",
        "RN" : "Rio Grande do Norte",
        "RS" : "Rio Grande do Sul",
        "RO" : "Rondônia",
        "RR" : "Roraima",
        "SC" : "Santa Catarina",
        "SP" : "São Paulo",
        "SE" : "Sergipe",
        "TO" : "Tocantins"
    }
    
    TIPO = [
        ("FUNCIONARIO", "Funcionario"),
        ("LOCADOR", "Locador")
    ]
    
    nome = models.CharField(("nome"), max_length=50, null= False)
    cpf = models.CharField("cpf", max_length=11, null= False )
    numero = models.IntegerField("número para contato")
    data_nascimento = models.DateField(("data de nascimento"), auto_now=False, auto_now_add=False, null= False)
    email = models.EmailField(("email"), max_length=100)
    cep = models.CharField(("cep"), max_length=8)
    rua = models.CharField(("rua"), max_length=100)
    cidade = models.CharField(("cidade"), max_length=35)
    # UTILIZANDO ARRAY AFIM DE TESTAR A FUNCIONABILIDADE DO DJANGO 
    # E COMO SERA O USO DO ARMAZENAMENTO COMPARADO AO INT
    estado = models.CharField(("estado"), choices= ESTADOS)
    tipo = models.CharField(("tipo"), choices= TIPO, null= True)
    observacoes = models.TextField(("observações"))
    
    # TEM MUITOS CARGOS? TEM VARIAÇÃO DE PERMISSÕES ENTRE CARGOS?
class Funcionario(models.Model):
    cliente = models.OneToOneField("Cliente", verbose_name=("cliente"), on_delete=models.CASCADE)
    cargo = models.CharField(("cargo"), max_length=50)
    salario = models.DecimalField(("salário"), max_digits=5, decimal_places=2)
    pis = models.CharField(("pis"), max_length=13)
    entrada = models.DateField(("data de entrada"), auto_now=False, auto_now_add=True)
    saida = models.DateField(("data de saida"), auto_now=False, auto_now_add=False)
    
class Locador(models.Model):
    cliente = models.OneToOneField( Cliente, verbose_name=("locador"), on_delete=models.CASCADE)
    valor_aluguel = models.DecimalField(("valor do aluguel"), max_digits=5, decimal_places=2)
    inicio_contrato = models.DateField(("inicio do contrato"), auto_now=False, auto_now_add=False)
    fim_contrato = models.DateField(("fim do contrato"), auto_now=False, auto_now_add=False)
    
class Procedimento(models.Model):

    procedimento = models.CharField(("procedimento"), max_length=50, unique=True, null=False)
    valor = models.DecimalField(("valor"), max_digits=5, decimal_places=2)
    profissionais = models.ManyToManyField(Funcionario, related_name="profissional_que_realiza", null=False) 
    tempo_medio = models.DurationField(("Tempo Médio do Procedimento"), null=True, blank=True)

class Agendamento(models.Model):

    cliente = models.ForeignKey(Cliente, verbose_name=("cliente"), on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, verbose_name=("procedimento"), on_delete=models.CASCADE)
    data_hora = models.DateTimeField(("data e hora do agendamento"), auto_now=False, auto_now_add=False, null=False)
    observacoes = models.TextField(("observações"), null=True, blank=True)