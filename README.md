# Projeto Integrador – Backend com Django

**Data de Criação:** 13 de maio de 2025  
**Status:** Em desenvolvimento  

Este repositório contém o backend com páginas web desenvolvido em Django, como parte do Projeto Integrador do curso de Tecnologia em Análise e Desenvolvimento de Sistemas.

---

## Objetivo

Desenvolver um sistema de fácil utilização para:

- Coletar, armazenar e distribuir dados em tempo real  
- Melhorar a gestão de serviços na área estética  
- Proporcionar controle financeiro eficiente  
- Otimizar o gerenciamento de serviços e produtos  

---

## Funcionalidades

- Página inicial  
- Cadastro de clientes  
- Agendamento de serviços  
- Cadastro de procedimentos  
- Cadastro de fornecedores  
- Sistema de login  
- Menu principal  

---

## Tecnologias Utilizadas

- Python 3.12+  
- Django 5.x  
- HTML (Templates com herança)  
- Git e GitHub  

---

## Equipe

- Bruna Soto Cardoso dos Santos  
- Elania Cristina Peixoto  
- Graciely Ferreira  
- Rafael Souza dos Santos  

---

## Acesso ao Sistema
Usuário: admin
Senha: admin
---

## Atualização – Padrão Template Method

**Data:** 24 de outubro de 2025  

Foi implementado o padrão de projeto Template Method para padronizar o fluxo de criação e edição das entidades principais:

- Pessoa  
- Funcionário  
- Usuário  

---

## Estrutura


gerencia/
├── base_views.py # Classe abstrata (BaseModelFormView)
└── views.py # Subclasses (PessoaView, FuncionarioView, etc.)


---

## Explicação

O padrão Template Method define o esqueleto de um algoritmo na superclasse, permitindo que as subclasses sobrescrevam etapas específicas sem alterar a estrutura geral.

### Aplicação no projeto

- `BaseModelFormView` define métodos abstratos:
  - `get_model_class()`
  - `get_template_name()`
  - `get_success_url()`

- Subclasses implementam:
  - `PessoaView`
  - `FuncionarioView`
  - `UsuarioView`

---

## Diagrama UML

Foi criado um diagrama UML representando:

- Herança da classe abstrata  
- Relação entre as subclasses  
- Associação entre Pessoa, Funcionário e Usuário  

---

## Benefícios

- Código mais organizado  
- Reutilização de lógica  
- Redução de duplicidade  
- Facilidade de manutenção  
- Padronização das views  

---

## Observações

Este projeto está sendo desenvolvido em grupo como atividade avaliativa da disciplina de Programação Back-end e Padrões de Projetos.

Todos os integrantes contribuem com commits individuais no GitHub.
