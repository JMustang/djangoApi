# Django API

## Funcionamento básico de Django

- Criando ambiente virtual no **python**

```bash
python3 -m venv meu_ambiente_virtual
```

- Iniciando ambiente o virtual

```bash
source meu_ambiente_virtual/bin/activate
```

- No ambiente virtual o pip vem desatualizado.
  atualize a versão do pip com o comando abaixo.

```bash
pip install --upgrade pip
```

- Instale as dependências necessárias do **Django**.

```bash
pip install django
```

- Use o comando **django-admin** com a **flag** **startproject**, para iniciar o seu projeto.

```bash
django-admin startproject nome_do_projeto
```

- Para rodar o servidor do **Django** use o comando:

```bash
python manage.py runserver
```

- **manage.py**: É um utilitário de linha de comando que permite interagir com este projeto Django de várias maneiras.

## Padrão de projeto

- **Django** utiliza a arquitetura **MVT**, Models, Views e Templates.

  1.Models: Models lida com o banco de dados, tudo que for relacionado ao banco de dados
  o model é responsável. Criar tabela, modificar tabela, etc, ficara dentro do arquivo **models.py**.
  2.Views: Views é onde vai ficar a logica da aplicação, funções em python que faz x, y, z, toda a logica da aplicação vai ficar dentro do arquivo **views.py**.
  3.Templates: Templates, é a camada de interface com o usuário,
  a parte "frontend" do **Django**.
