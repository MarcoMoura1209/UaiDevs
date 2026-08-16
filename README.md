<img src="assets/img/LogoUaiDevs.png" width="600" alt="Logo da Uai devs">

# Uaidevs Landing Page

Landing page desenvolvida para a empresa Uaidevs, focada em automação de atendimento através de agentes inteligentes integrados ao WhatsApp e sistemas CRM.

O projeto foi desenvolvido durante meu estágio utilizando Django Templates no back-end e tecnologias web no front-end.

## Tecnologias utilizadas

- Python
- Django
- PostgreSQL
- HTML5
- CSS3
- JavaScript
- Docker

## Funcionalidades

- Landing page responsiva
- Integração com formulários
- Estrutura otimizada para conversão
- Integração com banco de dados PostgreSQL
- Sistema desenvolvido com Django Templates

## Estrutura do projeto

```bash
├── UaiDevs  
│   ├── settings  
│   │   ├── __init__.py  
│   │   ├── base.py  
│   │   ├── local.py  
│   │   └── production.py  
│   ├── __init__.py  
│   ├── asgi.py  
│   ├── urls.py  
│   └── wsgi.py  
├── assets  
│   ├── css  
│   │   ├── base.css  
│   │   ├── components.css  
│   │   ├── responsive.css  
│   │   ├── root.css  
│   │   ├── sections.css  
│   │   └── style.css  
│   ├── img  
│   │   ├── LogoUaiDevs-50x.png  
│   │   ├── LogoUaiDevs-75x.png  
│   │   └── LogoUaiDevs.png  
│   └── js  
│       ├── carrossel-feedback.js  
│       └── menu-toggle.js  
├── core  
│   ├── migrations  
│   │   ├── 0001_initial.py  
│   │   └── __init__.py  
│   ├── templates  
│   │   └── core  
│   │       └── pages  
│   │           └── home.html  
│   ├── tests  
│   │   ├── __init__.py  
│   │   ├── test_form_core.py  
│   │   ├── test_integration_server.py  
│   │   ├── test_model_core.py  
│   │   ├── test_security_core.py  
│   │   ├── test_url_core.py  
│   │   └── test_views_core.py  
│   ├── __init__.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── forms.py  
│   ├── models.py  
│   ├── urls.py  
│   └── views.py  
├── .env.example  
├── .gitignore  
├── manage.py  
├── pytest.ini  
└── requirements.txt  
```

## Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

## Aviso

Este projeto foi desenvolvido para fins profissionais durante estágio supervisionado e está disponível apenas para demonstração de portfólio.
