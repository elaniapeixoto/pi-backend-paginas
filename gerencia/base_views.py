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
    def GET_MODEL_CLASS(self):
        """HOOK OBRIGATÓRIO: retorna o modelo (ex: Pessoa, Funcionario)."""
        pass

    @abstractmethod
    def GET_TEMPLATE_NAME(self):
        """HOOK OBRIGATÓRIO: retorna o template a ser renderizado."""
        pass

    @abstractmethod
    def GET_SUCCESS_URL(self):
        """HOOK OBRIGATÓRIO: URL para redirecionamento após sucesso."""
        pass

    @abstractmethod
    def CLEAN_AND_APPLY_DATA(self, request, instance):
        """HOOK OBRIGATÓRIO: aplica os dados do POST na instância."""
        pass

    # --- MÉTODOS CONCRETOS (HOOKS OPCIONAIS) ---
    # Podem ser sobrescritos pelas subclasses

    def get_object(self, **kwargs):
        """Retorna objeto existente ou cria novo."""
        pk = kwargs.get("id")
        Model = self.GET_MODEL_CLASS()

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

    def AFTER_SAVE(self, request, instance):
        """HOOK PÓS-SAVE: executado após salvar o objeto no banco."""
        pass

    # --- TEMPLATE METHOD (NÃO ALTERAR) ---
    # Define a sequência fixa do algoritmo

    def dispatch(self, request: HttpRequest, **kwargs) -> HttpResponse:
        instance = self.get_object(**kwargs)

        # Se objeto não encontrado em edição, redireciona
        if not instance and kwargs.get("id"):
            return redirect(self.GET_SUCCESS_URL())

        if request.method == "POST":
            # Aplica dados via hook obrigatório
            self.CLEAN_AND_APPLY_DATA(request, instance)

            # Salva objeto
            instance.save()

            # CHAMA O HOOK PÓS-SAVE (IMPORTANTE)
            self.AFTER_SAVE(request, instance)

            # Redireciona após sucesso
            return redirect(self.GET_SUCCESS_URL())

        # Renderiza formulário (GET)
        context = self.get_context_data(request, instance=instance, **kwargs)
        return render(request, self.GET_TEMPLATE_NAME(), context)


# Wrapper para urls.py
def base_view_wrapper(ViewClass):
    """Transforma classe em view com login obrigatório."""

    @login_required
    def view_func(request, *args, **kwargs):
        return ViewClass().dispatch(request, **kwargs)

    return view_func
