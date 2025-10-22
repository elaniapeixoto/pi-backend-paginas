from abc import ABC, abstractmethod
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse


class BaseModelFormView(ABC):
    """
    ESQUELETO PARA VIEWS DE FORMULÁRIO (CADASTRO/EDIÇÃO).
    SUBCLASSES PODEM SOBRESCREVER HOOKS SEM ALTERAR A ESTRUTURA.
    """

    # --- MÉTODOS ABSTRATOS (OBRIGATÓRIOS) ---
    # Devem ser implementados pelas subclasses

    @abstractmethod
    def get_model_class(self):  # CORRIGIDO: de GET_MODEL_CLASS para get_model_class
        """HOOK OBRIGATÓRIO: retorna o modelo (ex: Pessoa, Funcionario)."""
        pass

    @abstractmethod
    def get_template_name(
        self,
    ):  # CORRIGIDO: de GET_TEMPLATE_NAME para get_template_name
        """HOOK OBRIGATÓRIO: retorna o template a ser renderizado."""
        pass

    @abstractmethod
    def get_success_url(self):  # CORRIGIDO: de GET_SUCCESS_URL para get_success_url
        """HOOK OBRIGATÓRIO: URL para redirecionamento após sucesso."""
        pass

    @abstractmethod
    def clean_and_apply_data(
        self, request, instance
    ):  # CORRIGIDO: de CLEAN_AND_APPLY_DATA para clean_and_apply_data
        """HOOK OBRIGATÓRIO: aplica os dados do POST na instância."""
        pass

    # --- MÉTODOS CONCRETOS (HOOKS OPCIONAIS) ---
    # Podem ser sobrescritos pelas subclasses

    def get_object(self, **kwargs):
        """Retorna objeto existente ou cria novo."""
        pk = kwargs.get("id")
        Model = self.get_model_class()  # CORRIGIDO: Chama get_model_class (minúsculas)

        if pk:
            try:
                return Model.objects.get(id=pk)
            except Model.DoesNotExist:
                return None
        return Model()

    def get_context_data(self, request, instance=None, **kwargs):
        """Prepara contexto do template."""
        context = kwargs.copy()
        if instance and instance.pk:
            context["object"] = instance
        return context

    def after_save(self, request, instance):  # CORRIGIDO: de AFTER_SAVE para after_save
        """HOOK PÓS-SAVE: executado após salvar o objeto no banco."""
        pass

    # --- TEMPLATE METHOD (NÃO ALTERAR) ---
    # Define a sequência fixa do algoritmo

    def dispatch(self, request: HttpRequest, **kwargs) -> HttpResponse:
        instance = self.get_object(**kwargs)

        # Se objeto não encontrado em edição, redireciona
        if not instance and kwargs.get("id"):
            return redirect(
                self.get_success_url()
            )  # CORRIGIDO: Chama get_success_url (minúsculas)

        if request.method == "POST":
            # Aplica dados via hook obrigatório
            self.clean_and_apply_data(
                request, instance
            )  # CORRIGIDO: Chama clean_and_apply_data (minúsculas)

            # Salva objeto
            instance.save()

            # CHAMA O HOOK PÓS-SAVE (IMPORTANTE)
            self.after_save(
                request, instance
            )  # CORRIGIDO: Chama after_save (minúsculas)

            # Redireciona após sucesso
            return redirect(
                self.get_success_url()
            )  # CORRIGIDO: Chama get_success_url (minúsculas)

        # Renderiza formulário (GET)
        context = self.get_context_data(request, instance=instance, **kwargs)
        return render(
            request, self.get_template_name(), context
        )  # CORRIGIDO: Chama get_template_name (minúsculas)


# Wrapper para urls.py
def base_view_wrapper(ViewClass):
    """Transforma classe em view com login obrigatório."""

    @login_required
    def view_func(request, *args, **kwargs):
        return ViewClass().dispatch(request, **kwargs)

    return view_func
