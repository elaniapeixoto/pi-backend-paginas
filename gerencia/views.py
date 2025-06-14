from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *

estados = {
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
estados = estados.items()


@login_required
def index(request):
    return render(request, "gerencia/index.html")


@login_required
def lista_pessoa(request):
    pessoas = Pessoa.objects.all()

    return render(request, "lista_pessoa.html", {"pessoas": pessoas})


@login_required
def cadastro_pessoa(request):
    # RECEBE O REQUEST PARA SALVAR OS DADOS DA PESSOA E RETORNA A LISTA
    if request.method == "POST":
        dados = request.POST.dict()
        pessoa = Pessoa()
        # VERIFICA CAMPOS VAZIOS
        for campo in [
            "nome_completo",
            "cpf",
            "numero",
            "email",
            "data_nascimento",
            "cep",
            "cidade",
            "estado",
            "observacoes",
        ]:
            valor = dados.get(campo)
            setattr(pessoa, campo, valor if valor != "" else None)

        pessoa.save()
        return redirect("lista_pessoa")

    return render(request, "cadastro_pessoa.html", {"estados": estados})


def editar_pessoa(request, id):
    # BUSCA PESSOA PELO ID, SE NAO ENCONTRAR RETORNA PARA A LISTA
    try:
        pessoa = Pessoa.objects.get(id=id)
    except Pessoa.DoesNotExist:
        return render(request, "lista_pessoa.html", {"warning": True})

    # SE FOR UM REQUEST VAI EDITAR OS DADOS DA PESSOA
    if request.method == "POST":
        dados = request.POST.dict()
        # VERIFICA CAMPOS VAZIOS
        for campo in [
            "nome_completo",
            "cpf",
            "numero",
            "email",
            "data_nascimento",
            "cep",
            "cidade",
            "estado",
            "observacoes",
        ]:
            valor = dados.get(campo)
            setattr(pessoa, campo, valor if valor != "" else None)
        pessoa.save()
        return redirect("lista_pessoa")

    # MOSTRA A TELA DE EDIÇÃO COM AS INFORMAÇÕES DA PESSOA
    return render(
        request, "cadastro_pessoa.html", {"pessoa": pessoa, "estados": estados}
    )


# @login_required
# def cadastro_usuario(request):
#     return render(request, "usuario/cadastro_usuario.html")


@login_required
def cadastro_agendamento(request):
    return render(request, "agendamento.html")


@login_required
def cadastro_procedimento(request):
    return render(request, "index.html")


@login_required
def lista_funcionario(request):
    funcionarios = Funcionario.objects.select_related("pessoa").all()
    return render(request, "lista_funcionario.html", {"funcionarios": funcionarios})


@login_required
def cadastro_funcionario(request):
    pessoas_disponiveis = Pessoa.objects.exclude(
        id__in=Funcionario.objects.values_list("pessoa_id", flat=True)
    )

    if request.method == "POST":
        dados = request.POST.dict()
        funcionario = Funcionario()

        pessoa_id = dados.get("pessoa")
        funcionario.pessoa = Pessoa.objects.get(id=pessoa_id) if pessoa_id else None

        for campo in ["cargo", "salario", "pis", "entrada", "saida"]:
            valor = dados.get(campo)
            setattr(funcionario, campo, valor if valor != "" else None)

        funcionario.save()
        return redirect("lista_funcionario")

    return render(
        request, "cadastro_funcionario.html", {"pessoas": pessoas_disponiveis}
    )


@login_required
def editar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except Funcionario.DoesNotExist:
        return redirect("lista_funcionario")

    if request.method == "POST":
        dados = request.POST.dict()

        pessoa_id = dados.get("pessoa")
        funcionario.pessoa = Pessoa.objects.get(id=pessoa_id) if pessoa_id else None

        for campo in ["cargo", "salario", "pis", "entrada", "saida"]:
            valor = dados.get(campo)
            setattr(funcionario, campo, valor if valor != "" else None)

        funcionario.save()
        return redirect("lista_funcionario")

    pessoas_disponiveis = Pessoa.objects.exclude(
        id__in=Funcionario.objects.exclude(id=funcionario.id).values_list(
            "pessoa_id", flat=True
        )
    )
    return render(
        request,
        "cadastro_funcionario.html",
        {"funcionario": funcionario, "pessoas": pessoas_disponiveis},
    )
