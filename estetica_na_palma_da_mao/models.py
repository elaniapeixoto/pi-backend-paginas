from django.db import models

class clientes(models.Model):
    
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
    
    
    # TODO CRIAR CLASSE AFILIADOS QUE HERDA DE CLIENTE 
    nome = models.CharField(("nome"), max_length=50, null= False)
    cpf = models.CharField("cpf", max_length=11, null= False )
    numero = models.IntegerField("número para contato")
    data_nascimento = models.DateField(("data de nascimento"), auto_now=False, auto_now_add=False, null= False)
    email = models.EmailField(("email"), max_length=100)
    cep = models.CharField(("cep"), max_length=8)
    rua = models.CharField(("rua"), max_length=100)
    cidade = models.CharField(("cidade"), max_length=35)
    estado = models.CharField(("estado"), choices= ESTADOS)
    observacoes = models.TextField(("observações"))
    