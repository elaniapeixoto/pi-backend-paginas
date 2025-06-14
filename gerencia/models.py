from django.contrib.auth.models import User
from django.db import models


"""
Classes necessárias:
    usuario   
    pessoas   #feito
    funcionarios   #feito
    locador  #feito
    fornecedores #Feito
    produtos #feito
    vendas 
    agenda  #feito
    procedimentos  #feito
   
"""
ESTADOS = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins",
}


class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    TIPO = [("FUNCIONARIO", "Funcionario"), ("LOCADOR", "Locador")]

    nome_completo = models.CharField(("nome"), max_length=50)
    cpf = models.CharField("cpf", max_length=11)
    numero = models.IntegerField("número para contato")
    data_nascimento = models.DateField(
        ("data de nascimento"), auto_now=False, auto_now_add=False, null=True
    )
    email = models.EmailField(("email"), max_length=100, null=True, blank=True)
    cep = models.CharField(("cep"), max_length=8, null=True, blank=True)
    cidade = models.CharField(("cidade"), max_length=35, null=True, blank=True)
    # UTILIZANDO ARRAY AFIM DE TESTAR A FUNCIONABILIDADE DO DJANGO
    # E COMO SERA O USO DO ARMAZENAMENTO COMPARADO AO INT(4)
    estado = models.CharField(("estado"), choices=ESTADOS, null=True, blank=True)
    tipo = models.CharField(("tipo"), choices=TIPO, null=True, blank=True)
    observacoes = models.TextField(("observações"), null=True, blank=True)


class Funcionario(models.Model):
    pessoa = models.OneToOneField(
        "Pessoa",
        verbose_name=("pessoa"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    cargo = models.CharField(("cargo"), max_length=50)
    salario = models.DecimalField(("salário"), max_digits=5, decimal_places=2)
    pis = models.CharField(("pis"), max_length=13)
    entrada = models.DateField(("data de entrada"), auto_now=False, auto_now_add=True)
    saida = models.DateField(("data de saida"), auto_now=False, auto_now_add=False)


class Locador(models.Model):
    pessoa = models.OneToOneField(
        Pessoa, verbose_name=("locador"), on_delete=models.CASCADE
    )
    valor_aluguel = models.DecimalField(
        ("valor do aluguel"), max_digits=5, decimal_places=2
    )
    inicio_contrato = models.DateField(
        ("inicio do contrato"), auto_now=False, auto_now_add=False
    )
    fim_contrato = models.DateField(
        ("fim do contrato"), auto_now=False, auto_now_add=False
    )


class Procedimento(models.Model):

    procedimento = models.CharField(
        ("procedimento"), max_length=50, unique=True, null=False
    )
    valor = models.DecimalField(("valor"), max_digits=5, decimal_places=2)
    profissionais = models.OneToOneField(
        Funcionario,
        related_name="profissional_que_realiza",
        null=True,
        on_delete=models.CASCADE,
    )
    tempo_medio = models.DurationField(
        ("tempo médio do procedimento"), null=True, blank=True
    )


class Agendamento(models.Model):

    pessoa = models.ForeignKey(
        Pessoa, verbose_name=("pessoa"), on_delete=models.CASCADE, null=True, blank=True
    )
    procedimento = models.ForeignKey(
        Procedimento, verbose_name=("procedimento"), on_delete=models.CASCADE
    )
    data_hora = models.DateTimeField(
        ("data e hora do agendamento"), auto_now=False, auto_now_add=False, null=False
    )
    observacoes = models.TextField(("observações"), null=True, blank=True)


class Categoria(models.Model):
    nome = models.CharField("nome da categoria", max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    UNIDADES = [
        ("ml", "Mililitro"),
        ("kg", "Quilograma"),
        ("un", "Unidade"),
        ("pac", "Pacote"),
    ]
    codigo = models.CharField("código do produto", max_length=20, unique=True)
    nome = models.CharField("nome do produto", max_length=100)
    unidade = models.CharField(
        "unidade", max_length=10, choices=UNIDADES
    )  # tipo de medida
    fabricante = models.CharField("fabricante", max_length=100)
    fornecedor = models.ForeignKey(
        "fornecedor", verbose_name="fornecedor", on_delete=models.CASCADE
    )
    categoria = models.ForeignKey(
        Categoria,
        verbose_name="categoria",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
