# Generated manually to finish the salon management modules.

import django.db.models.deletion
from django.db import migrations, models


ESTADOS = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapa"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceara"),
    ("DF", "Distrito Federal"),
    ("ES", "Espirito Santo"),
    ("GO", "Goias"),
    ("MA", "Maranhao"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Para"),
    ("PB", "Paraiba"),
    ("PR", "Parana"),
    ("PE", "Pernambuco"),
    ("PI", "Piaui"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondonia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "Sao Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
]


class Migration(migrations.Migration):

    dependencies = [
        ("gerencia", "0002_rename_cliente_pessoa_rename_cliente_locador_pessoa_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pessoa",
            name="rua",
        ),
        migrations.RemoveField(
            model_name="procedimento",
            name="profissionais",
        ),
        migrations.AlterModelOptions(
            name="pessoa",
            options={"ordering": ["nome_completo"]},
        ),
        migrations.AlterModelOptions(
            name="agendamento",
            options={"ordering": ["data_hora"]},
        ),
        migrations.AlterModelOptions(
            name="procedimento",
            options={"ordering": ["procedimento"]},
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="nome_completo",
            field=models.CharField(max_length=80, verbose_name="nome"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="cpf",
            field=models.CharField(max_length=14, verbose_name="cpf"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="numero",
            field=models.CharField(max_length=20, verbose_name="numero para contato"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="data_nascimento",
            field=models.DateField(blank=True, null=True, verbose_name="data de nascimento"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="cep",
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name="cep"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="cidade",
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name="cidade"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="estado",
            field=models.CharField(blank=True, choices=ESTADOS, max_length=2, null=True, verbose_name="estado"),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="tipo",
            field=models.CharField(
                blank=True,
                choices=[("FUNCIONARIO", "Funcionario"), ("LOCADOR", "Locador")],
                max_length=12,
                null=True,
                verbose_name="tipo",
            ),
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="observacoes",
            field=models.TextField(blank=True, null=True, verbose_name="observacoes"),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="cargo",
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="cargo"),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="salario",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="salario"
            ),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="saida",
            field=models.DateField(blank=True, null=True, verbose_name="data de saida"),
        ),
        migrations.AlterField(
            model_name="locador",
            name="valor_aluguel",
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name="valor do aluguel"),
        ),
        migrations.AlterField(
            model_name="procedimento",
            name="procedimento",
            field=models.CharField(max_length=80, unique=True, verbose_name="procedimento"),
        ),
        migrations.AlterField(
            model_name="procedimento",
            name="valor",
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name="valor"),
        ),
        migrations.AlterField(
            model_name="procedimento",
            name="tempo_medio",
            field=models.DurationField(blank=True, null=True, verbose_name="tempo medio do procedimento"),
        ),
        migrations.AlterField(
            model_name="agendamento",
            name="observacoes",
            field=models.TextField(blank=True, null=True, verbose_name="observacoes"),
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=50, unique=True, verbose_name="nome da categoria")),
            ],
        ),
        migrations.CreateModel(
            name="MovimentoCaixa",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "tipo",
                    models.CharField(
                        choices=[("ENTRADA", "Entrada"), ("SAIDA", "Saida")],
                        max_length=7,
                        verbose_name="tipo",
                    ),
                ),
                ("descricao", models.CharField(max_length=120, verbose_name="descricao")),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="valor")),
                ("data", models.DateField(verbose_name="data")),
                ("observacoes", models.TextField(blank=True, null=True, verbose_name="observacoes")),
            ],
            options={"ordering": ["-data", "-id"]},
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("codigo", models.CharField(max_length=20, unique=True, verbose_name="codigo do produto")),
                ("nome", models.CharField(max_length=100, verbose_name="nome do produto")),
                (
                    "unidade",
                    models.CharField(
                        choices=[("ml", "Mililitro"), ("kg", "Quilograma"), ("un", "Unidade"), ("pac", "Pacote")],
                        max_length=10,
                        verbose_name="unidade",
                    ),
                ),
                ("fabricante", models.CharField(max_length=100, verbose_name="fabricante")),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="gerencia.categoria",
                        verbose_name="categoria",
                    ),
                ),
            ],
        ),
    ]
