from django.contrib.auth.models import User
from django.db import models


ESTADOS = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapa",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceara",
    "DF": "Distrito Federal",
    "ES": "Espirito Santo",
    "GO": "Goias",
    "MA": "Maranhao",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Para",
    "PB": "Paraiba",
    "PR": "Parana",
    "PE": "Pernambuco",
    "PI": "Piaui",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondonia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "Sao Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins",
}


class Pessoa(models.Model):
    TIPO = [("FUNCIONARIO", "Funcionario"), ("LOCADOR", "Locador")]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField("nome", max_length=80)
    cpf = models.CharField("cpf", max_length=14)
    numero = models.CharField("numero para contato", max_length=20)
    data_nascimento = models.DateField("data de nascimento", null=True, blank=True)
    email = models.EmailField("email", max_length=100, null=True, blank=True)
    cep = models.CharField("cep", max_length=9, null=True, blank=True)
    cidade = models.CharField("cidade", max_length=35, null=True, blank=True)
    estado = models.CharField("estado", max_length=2, choices=ESTADOS, null=True, blank=True)
    tipo = models.CharField("tipo", max_length=12, choices=TIPO, null=True, blank=True)
    observacoes = models.TextField("observacoes", null=True, blank=True)

    class Meta:
        ordering = ["nome_completo"]

    def __str__(self):
        return self.nome_completo


class Funcionario(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        verbose_name="pessoa",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    cargo = models.CharField("cargo", max_length=50, null=True, blank=True)
    salario = models.DecimalField(
        "salario", max_digits=10, decimal_places=2, null=True, blank=True
    )
    pis = models.CharField("pis", max_length=13)
    entrada = models.DateField("data de entrada", auto_now_add=True)
    saida = models.DateField("data de saida", null=True, blank=True)

    def __str__(self):
        return f"{self.pessoa} - {self.cargo}" if self.pessoa else self.cargo


class Locador(models.Model):
    pessoa = models.OneToOneField(Pessoa, verbose_name="locador", on_delete=models.CASCADE)
    valor_aluguel = models.DecimalField("valor do aluguel", max_digits=10, decimal_places=2)
    inicio_contrato = models.DateField("inicio do contrato")
    fim_contrato = models.DateField("fim do contrato")

    def __str__(self):
        return str(self.pessoa)


class Procedimento(models.Model):
    procedimento = models.CharField("procedimento", max_length=80, unique=True)
    valor = models.DecimalField("valor", max_digits=10, decimal_places=2)
    tempo_medio = models.DurationField("tempo medio do procedimento", null=True, blank=True)

    class Meta:
        ordering = ["procedimento"]

    def __str__(self):
        return self.procedimento


class Agendamento(models.Model):
    pessoa = models.ForeignKey(
        Pessoa, verbose_name="pessoa", on_delete=models.CASCADE, null=True, blank=True
    )
    procedimento = models.ForeignKey(
        Procedimento, verbose_name="procedimento", on_delete=models.CASCADE
    )
    data_hora = models.DateTimeField("data e hora do agendamento")
    observacoes = models.TextField("observacoes", null=True, blank=True)

    class Meta:
        ordering = ["data_hora"]

    def __str__(self):
        return f"{self.pessoa} - {self.procedimento} em {self.data_hora:%d/%m/%Y %H:%M}"


class MovimentoCaixa(models.Model):
    TIPOS = [
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saida"),
    ]

    tipo = models.CharField("tipo", max_length=7, choices=TIPOS)
    descricao = models.CharField("descricao", max_length=120)
    valor = models.DecimalField("valor", max_digits=10, decimal_places=2)
    data = models.DateField("data")
    observacoes = models.TextField("observacoes", null=True, blank=True)

    class Meta:
        ordering = ["-data", "-id"]

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.descricao}"


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

    codigo = models.CharField("codigo do produto", max_length=20, unique=True)
    nome = models.CharField("nome do produto", max_length=100)
    unidade = models.CharField("unidade", max_length=10, choices=UNIDADES)
    fabricante = models.CharField("fabricante", max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        verbose_name="categoria",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nome
