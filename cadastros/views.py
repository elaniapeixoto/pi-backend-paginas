from django.shortcuts import render

def cadastro_pessoa(request):
    return render(request, "cadastros/cadastro_pessoa.html")

def cadastro_fornecedor(request):
    return render(request, "cadastros/cadastro_fornecedor.html")

def agendamento(request):
    return render(request, "cadastros/agendamento.html")

def cadastro_procedimento(request):
    return render(request, "index.html")

def cadastro_fornecedor(request):
    estados = [
        "AC",
        "AL",
        "AP",
        "AM",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MT",
        "MS",
        "MG",
        "PA",
        "PB",
        "PR",
        "PE",
        "PI",
        "RJ",
        "RN",
        "RS",
        "RO",
        "RR",
        "SC",
        "SP",
        "SE",
        "TO",
    ]
    context = {
        "estados": estados,
    }
    return render(request, "cadastros/cadastro_fornecedor.html", context)

