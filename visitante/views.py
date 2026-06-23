from django.shortcuts import render
from django.utils import timezone

from gerencia.models import Agendamento, Procedimento


def index(request):
    procedimentos = Procedimento.objects.all()
    proximos_agendamentos = Agendamento.objects.filter(
        data_hora__gte=timezone.now()
    ).select_related("procedimento")[:10]
    return render(
        request,
        "visitante/index.html",
        {
            "procedimentos": procedimentos,
            "proximos_agendamentos": proximos_agendamentos,
        },
    )


def procedimentos(request):
    return render(
        request,
        "visitante/procedimentos.html",
        {"procedimentos": Procedimento.objects.all()},
    )


def agenda(request):
    agendamentos = Agendamento.objects.filter(data_hora__gte=timezone.now()).select_related(
        "procedimento"
    )
    return render(request, "visitante/agenda.html", {"agendamentos": agendamentos})


def sobre(request):
    return render(request, "sobre.html")
