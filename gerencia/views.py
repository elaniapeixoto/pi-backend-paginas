from datetime import timedelta
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .base_views import BaseModelFormView, base_view_wrapper
from .models import (
    ESTADOS,
    Agendamento,
    Funcionario,
    Locador,
    MovimentoCaixa,
    Pessoa,
    Procedimento,
)


estados = ESTADOS.items()


def decimal_or_zero(value):
    return Decimal(value or "0")


def parse_duration(value):
    if not value:
        return None

    parts = value.split(":")
    if len(parts) == 2:
        hours = int(parts[0])
        minutes = int(parts[1])
        return timedelta(hours=hours, minutes=minutes)

    return timedelta(minutes=int(value))


@login_required
def index(request):
    hoje = timezone.localdate()
    agendamentos_hoje = Agendamento.objects.filter(data_hora__date=hoje).select_related(
        "pessoa", "procedimento"
    )
    total_entradas = (
        MovimentoCaixa.objects.filter(tipo="ENTRADA").aggregate(total=Sum("valor"))["total"]
        or Decimal("0")
    )
    total_saidas = (
        MovimentoCaixa.objects.filter(tipo="SAIDA").aggregate(total=Sum("valor"))["total"]
        or Decimal("0")
    )
    context = {
        "total_pessoas": Pessoa.objects.count(),
        "total_funcionarios": Funcionario.objects.count(),
        "total_locadores": Locador.objects.count(),
        "total_procedimentos": Procedimento.objects.count(),
        "agendamentos_hoje": agendamentos_hoje,
        "saldo_caixa": total_entradas - total_saidas,
    }
    return render(request, "gerencia/index.html", context)


@login_required
def lista_pessoa(request):
    pessoas = Pessoa.objects.all()
    return render(request, "lista_pessoa.html", {"pessoas": pessoas})


class PessoaView(BaseModelFormView):
    def get_model_class(self):
        return Pessoa

    def get_template_name(self):
        return "cadastro_pessoa.html"

    def get_success_url(self):
        return "lista_pessoa"

    def clean_and_apply_data(self, request, instance):
        campos = [
            "nome_completo",
            "cpf",
            "numero",
            "email",
            "data_nascimento",
            "cep",
            "cidade",
            "estado",
            "observacoes",
        ]
        for campo in campos:
            valor = request.POST.get(campo)
            setattr(instance, campo, valor if valor else None)
        return instance

    def get_context_data(self, request, instance=None, **kwargs):
        context = super().get_context_data(request, instance=instance, **kwargs)
        context["estados"] = estados
        context["pessoa"] = instance
        return context


cadastro_pessoa = base_view_wrapper(PessoaView)


class PessoaEditView(PessoaView):
    def get_object(self, **kwargs):
        return get_object_or_404(Pessoa, id=kwargs.get("id"))


editar_pessoa = base_view_wrapper(PessoaEditView)


@login_required
def deletar_pessoa(request, id):
    get_object_or_404(Pessoa, id=id).delete()
    messages.success(request, "Pessoa removida com sucesso.")
    return redirect("lista_pessoa")


@login_required
def lista_funcionario(request):
    funcionarios = Funcionario.objects.select_related("pessoa").all()
    return render(request, "lista_funcionario.html", {"funcionarios": funcionarios})


class FuncionarioView(BaseModelFormView):
    def get_model_class(self):
        return Funcionario

    def get_template_name(self):
        return "cadastro_funcionario.html"

    def get_success_url(self):
        return "lista_funcionario"

    def clean_and_apply_data(self, request, instance):
        pessoa_id = request.POST.get("pessoa")
        instance.pessoa = Pessoa.objects.get(id=pessoa_id) if pessoa_id else None
        instance.cargo = request.POST.get("cargo") or None
        instance.salario = decimal_or_zero(request.POST.get("salario"))
        instance.pis = request.POST.get("pis") or ""
        instance.saida = request.POST.get("saida") or None
        return instance

    def after_save(self, request, instance):
        if instance.pessoa:
            instance.pessoa.tipo = "FUNCIONARIO"
            instance.pessoa.save()

    def get_context_data(self, request, instance=None, **kwargs):
        context = super().get_context_data(request, instance=instance, **kwargs)
        funcionario_id = instance.id if instance and instance.pk else None
        pessoas_ocupadas_ids = Funcionario.objects.exclude(
            id=funcionario_id
        ).values_list("pessoa_id", flat=True)
        context["pessoas"] = Pessoa.objects.exclude(id__in=pessoas_ocupadas_ids)
        context["funcionario"] = instance
        return context


cadastro_funcionario = base_view_wrapper(FuncionarioView)


class FuncionarioEditView(FuncionarioView):
    def get_object(self, **kwargs):
        return get_object_or_404(Funcionario, id=kwargs.get("id"))


editar_funcionario = base_view_wrapper(FuncionarioEditView)


@login_required
def deletar_funcionario(request, id):
    get_object_or_404(Funcionario, id=id).delete()
    messages.success(request, "Funcionario removido com sucesso.")
    return redirect("lista_funcionario")


@login_required
def lista_locador(request):
    locadores = Locador.objects.select_related("pessoa").all()
    return render(request, "lista_locador.html", {"locadores": locadores})


@login_required
def cadastro_locador(request, id=None):
    locador = get_object_or_404(Locador, id=id) if id else None
    locador_id = locador.id if locador else None
    pessoas_ocupadas = Locador.objects.exclude(id=locador_id).values_list(
        "pessoa_id", flat=True
    )

    if request.method == "POST":
        pessoa = get_object_or_404(Pessoa, id=request.POST.get("pessoa"))
        locador = locador or Locador()
        locador.pessoa = pessoa
        locador.valor_aluguel = decimal_or_zero(request.POST.get("valor_aluguel"))
        locador.inicio_contrato = request.POST.get("inicio_contrato")
        locador.fim_contrato = request.POST.get("fim_contrato")
        locador.save()
        pessoa.tipo = "LOCADOR"
        pessoa.save()
        messages.success(request, "Locador salvo com sucesso.")
        return redirect("lista_locador")

    return render(
        request,
        "cadastro_locador.html",
        {
            "locador": locador,
            "pessoas": Pessoa.objects.exclude(id__in=pessoas_ocupadas),
        },
    )


@login_required
def deletar_locador(request, id):
    get_object_or_404(Locador, id=id).delete()
    messages.success(request, "Locador removido com sucesso.")
    return redirect("lista_locador")


@login_required
def lista_procedimento(request):
    procedimentos = Procedimento.objects.all()
    return render(
        request, "lista_procedimento.html", {"procedimentos": procedimentos}
    )


@login_required
def cadastro_procedimento(request, id=None):
    procedimento = get_object_or_404(Procedimento, id=id) if id else None

    if request.method == "POST":
        procedimento = procedimento or Procedimento()
        procedimento.procedimento = request.POST.get("procedimento")
        procedimento.valor = decimal_or_zero(request.POST.get("valor"))
        procedimento.tempo_medio = parse_duration(request.POST.get("tempo_medio"))
        procedimento.save()
        messages.success(request, "Procedimento salvo com sucesso.")
        return redirect("lista_procedimentos")

    return render(
        request,
        "cadastro_procedimento.html",
        {"procedimento": procedimento},
    )


@login_required
def deletar_procedimento(request, id):
    get_object_or_404(Procedimento, id=id).delete()
    messages.success(request, "Procedimento removido com sucesso.")
    return redirect("lista_procedimentos")


@login_required
def lista_agendamento(request):
    agendamentos = Agendamento.objects.select_related("pessoa", "procedimento").all()
    return render(
        request, "lista_agendamento.html", {"agendamentos": agendamentos}
    )


@login_required
def cadastro_agendamento(request, id=None):
    agendamento = get_object_or_404(Agendamento, id=id) if id else None

    if request.method == "POST":
        agendamento = agendamento or Agendamento()
        pessoa_id = request.POST.get("pessoa")
        agendamento.pessoa = Pessoa.objects.get(id=pessoa_id) if pessoa_id else None
        agendamento.procedimento = get_object_or_404(
            Procedimento, id=request.POST.get("procedimento")
        )
        agendamento.data_hora = request.POST.get("data_hora")
        agendamento.observacoes = request.POST.get("observacoes") or None
        agendamento.save()
        messages.success(request, "Agendamento salvo com sucesso.")
        return redirect("lista_agendamento")

    return render(
        request,
        "cadastro_agendamento.html",
        {
            "agendamento": agendamento,
            "pessoas": Pessoa.objects.all(),
            "procedimentos": Procedimento.objects.all(),
        },
    )


@login_required
def deletar_agendamento(request, id):
    get_object_or_404(Agendamento, id=id).delete()
    messages.success(request, "Agendamento removido com sucesso.")
    return redirect("lista_agendamento")


@login_required
def lista_caixa(request):
    movimentos = MovimentoCaixa.objects.all()
    entradas = (
        MovimentoCaixa.objects.filter(tipo="ENTRADA").aggregate(total=Sum("valor"))[
            "total"
        ]
        or Decimal("0")
    )
    saidas = (
        MovimentoCaixa.objects.filter(tipo="SAIDA").aggregate(total=Sum("valor"))[
            "total"
        ]
        or Decimal("0")
    )
    return render(
        request,
        "lista_caixa.html",
        {
            "movimentos": movimentos,
            "entradas": entradas,
            "saidas": saidas,
            "saldo": entradas - saidas,
        },
    )


@login_required
def cadastro_caixa(request, id=None):
    movimento = get_object_or_404(MovimentoCaixa, id=id) if id else None

    if request.method == "POST":
        movimento = movimento or MovimentoCaixa()
        movimento.tipo = request.POST.get("tipo")
        movimento.descricao = request.POST.get("descricao")
        movimento.valor = decimal_or_zero(request.POST.get("valor"))
        movimento.data = request.POST.get("data")
        movimento.observacoes = request.POST.get("observacoes") or None
        movimento.save()
        messages.success(request, "Movimento de caixa salvo com sucesso.")
        return redirect("lista_caixa")

    return render(
        request,
        "cadastro_caixa.html",
        {"movimento": movimento, "tipos": MovimentoCaixa.TIPOS},
    )


@login_required
def deletar_caixa(request, id):
    get_object_or_404(MovimentoCaixa, id=id).delete()
    messages.success(request, "Movimento removido com sucesso.")
    return redirect("lista_caixa")


@login_required
def lista_usuario(request):
    usuarios = get_user_model().objects.all()
    return render(request, "lista_usuario.html", {"usuarios": usuarios})


@login_required
def cadastro_usuario(request):
    if request.method == "POST":
        User = get_user_model()
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            email=request.POST.get("email"),
        )
        pessoa = get_object_or_404(Pessoa, id=request.POST.get("pessoa_id"))
        pessoa.user = user
        pessoa.save()
        messages.success(request, "Usuario cadastrado e vinculado com sucesso.")
        return redirect("lista_usuario")

    pessoas = Pessoa.objects.filter(user__isnull=True)
    return render(request, "cadastro_usuario.html", {"pessoas": pessoas})
