💇‍♀️ Projeto Integrador – Backend com Django

Data de Criação: 13 de maio de 2025

Status do Projeto: 🚧 Em desenvolvimento

Este repositório contém o código do backend com páginas web desenvolvido em Django, como parte do Projeto Integrador do curso de Tecnologia em Análise e Desenvolvimento de Sistemas.

🧩 Objetivo

Desenvolver um sistema de fácil utilização para coletar, armazenar e distribuir dados em tempo real, melhorando a gestão e a qualidade dos serviços prestados na área estética, tendo um controle financeiro eficiente e um melhor gerenciamento de serviços e produtos

🛠 Funcionalidades previstas

Página inicial

Cadastro de clientes

Agendamento de serviços

Cadastro de procedimentos

Cadastro de fornecedores

Login e menu principal

🖥 Tecnologias utilizadas

Python 3.12+

Django 5.x

HTML e Templates com herança (template base)

Git/GitHub para versionamento

👥 Equipe

Bruna Soto Cardoso dos Santos

Elania Cristina Peixoto

Graciely Ferreira

Rafael Souza dos Santos

📌 Observações

Este projeto está sendo desenvolvido em grupo e faz parte das atividades avaliativas da disciplina de Programação Back-end.
Todos os membros estão contribuindo por meio de commits individuais no GitHub.
Para acessar o login 
-Usuario = admin
-Senha = admin


## 🧠 Atualização – Implementação do Padrão Template Method  
📅 **Data:** 24 de outubro de 2025  

Foi implementado o **padrão de projeto Template Method** no backend para padronizar o fluxo de criação e edição das entidades principais (**Pessoa**, **Funcionário** e **Usuário**) nas views do Django.  

Essa implementação torna o código mais organizado, fácil de manter e reaproveitar.

### 🔹 Estrutura da Implementação

```python
gerencia/
├── base_views.py # Classe Abstrata (BaseModelFormView) define o fluxo principal (Template Method).
└── views.py    # Subclasses (PessoaView, FuncionarioView, etc.) implementam os hooks específicos.
---

### 📘 Explicação do Padrão

Essa implementação segue o **padrão de design comportamental Template Method**, que define o esqueleto de um algoritmo na superclasse, mas permite que as subclasses substituam etapas específicas sem alterar sua estrutura geral.


No contexto do projeto:
- A classe `BaseModelFormView` define métodos como `get_model_class()`, `get_template_name()` e `get_success_url()` (abstratos).
- As subclasses (`PessoaView`, `FuncionarioView`, `UsuarioView`) implementam esses métodos, mantendo o mesmo fluxo geral de criação/edição.

---

### 📊 Diagrama UML Simplificado

Um diagrama UML foi criado para representar visualmente **a herança da classe abstrata e a relação entre as subclasses**, incluindo associações como a vinculação de `Funcionario` e `Usuario` com `Pessoa`.  


### ✅ Benefícios

- Código mais organizado, reutilizável e fácil de manter  
- Redução de duplicidade 
- Facilidade para criar novas views seguindo o mesmo modelo das subclasses. 

---
