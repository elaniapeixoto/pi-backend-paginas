from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from .models import Pessoa, Funcionario, Procedimento

# Importa o Template Method base
from .base_views import BaseModelFormView, base_view_wrapper


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


# ----------------------------------------------------------------------
# VIEWS DE PESSOA USANDO TEMPLATE METHOD
# ----------------------------------------------------------------------


class PessoaView(BaseModelFormView):
    # Métodos Abstratos
    def get_model_class(self):
        return Pessoa

    def get_template_name(self):
        return "cadastro_pessoa.html"

    def get_success_url(self):
        return "lista_pessoa"

    # hook: método que aplica os dados específicos da pessoa
    def clean_and_apply_data(self, request, instance):
        dados = request.POST.dict()
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
            valor = dados.get(campo)
            setattr(instance, campo, valor if valor != "" else None)
        return instance

    # Hook: Adiciona 'estados' ao contexto
    def get_context_data(self, request, instance=None, **kwargs):
        context = super().get_context_data(request, instance=instance, **kwargs)
        context["estados"] = estados
        return context


cadastro_pessoa = base_view_wrapper(PessoaView)


class PessoaEditView(PessoaView):
    # Hook: Sobrescreve a busca para Edição
    def get_object(self, **kwargs):
        pk = kwargs.get("id")
        if pk:
            try:
                return self.get_model_class().objects.get(id=pk)
            except self.get_model_class().DoesNotExist:
                return None
        return None


editar_pessoa = base_view_wrapper(PessoaEditView)


def deletar_pessoa(request, id):
    try:
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
    except Pessoa.DoesNotExist:
        messages.error(request, "Pessoa não encontrada.")
    return redirect("lista_pessoa")


# ----------------------------------------------------------------------
# VIEWS FIXAS (Agendamento, Procedimento)
# ----------------------------------------------------------------------


@login_required
def cadastro_agendamento(request):
    return render(request, "agendamento.html")


@login_required
def cadastro_procedimento(request):
    return render(request, "index.html")


@login_required
def lista_procedimento(request):
    return render(request, "index.html")


@login_required
def editar_procedimento(request):
    return render(request, "index.html")


# ----------------------------------------------------------------------
# VIEWS REFATORADAS COM TEMPLATE METHOD (FUNCIONÁRIO)
# ----------------------------------------------------------------------


@login_required
def lista_funcionario(request):
    funcionarios = Funcionario.objects.select_related("pessoa").all()
    return render(request, "lista_funcionario.html", {"funcionarios": funcionarios})


class FuncionarioView(BaseModelFormView):
    # Métodos Abstratos
    def get_model_class(self):
        return Funcionario

    def get_template_name(self):
        return "cadastro_funcionario.html"

    def get_success_url(self):
        return "lista_funcionario"

    # Hook: Aplica dados (incluindo FK)
    def clean_and_apply_data(self, request, instance):
        dados = request.POST.dict()

        pessoa_id = dados.get("pessoa")
        if pessoa_id:
            instance.pessoa = Pessoa.objects.get(id=pessoa_id)

        campos = ["cargo", "salario", "pis", "entrada", "saida"]
        for campo in campos:
            valor = dados.get(campo)
            setattr(instance, campo, valor if valor != "" else None)

        return instance

    # hook pós-save: atualiza o tipo da pessoa (lógica original)
    def after_save(self, request, instance):  # CORREÇÃO: Assinatura correta
        if instance.pessoa:
            pessoa = instance.pessoa
            pessoa.tipo = "FUNCIONARIO"
            pessoa.save()

    # hook: insere as pessoas disponíveis no contexto
    def get_context_data(self, request, instance=None, **kwargs):
        context = super().get_context_data(request, instance=instance, **kwargs)

        funcionario_id = instance.id if instance and instance.pk else None
        pessoas_ocupadas_ids = Funcionario.objects.exclude(
            id=funcionario_id
        ).values_list("pessoa_id", flat=True)

        context["pessoas"] = Pessoa.objects.exclude(id__in=pessoas_ocupadas_ids)

        if instance and instance.pk:
            context["funcionario"] = instance

        return context


cadastro_funcionario = base_view_wrapper(FuncionarioView)


class FuncionarioEditView(FuncionarioView):
    def get_object(self, **kwargs):
        pk = kwargs.get("id")
        if pk:
            try:
                return self.get_model_class().objects.get(id=pk)
            except self.get_model_class().DoesNotExist:
                return None
        return None


editar_funcionario = base_view_wrapper(FuncionarioEditView)


def deletar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
        funcionario.delete()
    except Funcionario.DoesNotExist:
        pass
    return redirect("lista_funcionario")


# ----------------------------------------------------------------------
# VIEWS REFETORADAS COM TEMPLATE METHOD (Usuário) - CORRIGIDA E FINALIZADA
# ----------------------------------------------------------------------


@login_required
def lista_usuario(request):
    User = get_user_model()
    usuarios = User.objects.all()
    return render(request, "lista_usuario.html", {"usuarios": usuarios})


class UsuarioView(BaseModelFormView):
    """Implementa o Template Method para Cadastro de Usuários e vínculo com Pessoa."""

    # Métodos Abstratos
    def get_model_class(self):
        return get_user_model()

    def get_template_name(self):
        return "cadastro_usuario.html"

    def get_success_url(self):
        return "alguma_view_de_sucesso"

    # hook principal: salva e vincula aqui
    def clean_and_apply_data(self, request, user_instance):
        dados = request.POST.dict()
        username = dados.get("username")
        password = dados.get("password")
        email = dados.get("email")
        pessoa_id = dados.get("pessoa_id")

        User = get_user_model()

        # lógica de try/except e criação/vínculo mantidas aqui
        try:
            user = User.objects.create_user(
                username=username, password=password, email=email
            )

            pessoa = Pessoa.objects.get(id=pessoa_id)
            # CORREÇÃO CRÍTICA: Mudar de 'pessoa.usuario' para 'pessoa.user'
            # (para casar com o models.py)
            pessoa.user = user
            pessoa.save()

            messages.success(
                request, "Usuário cadastrado com sucesso e vinculado à pessoa!"
            )

        except Pessoa.DoesNotExist:
            messages.error(request, "Pessoa não encontrada.")
            raise
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar: {str(e)}")
            raise

        return user_instance

    # hook pós-save: sobrescreve salvamento padrão do template method
    def after_save(self, request, instance):  # CORREÇÃO: Assinatura correta
        pass

    # Hook Contexto: Adiciona Pessoas disponíveis para vínculo
    def get_context_data(self, request, instance=None, **kwargs):
        context = super().get_context_data(request, instance=instance, **kwargs)
        # CORREÇÃO CRÍTICA: Mudar de 'usuario__isnull' para 'user__isnull'
        context["pessoas"] = Pessoa.objects.filter(user__isnull=True)
        return context


# Substitui a função 'cadastro_usuario' antiga
cadastro_usuario = base_view_wrapper(UsuarioView)
