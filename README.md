# Bloco de Notas

Um sistema de notas simples feito em Django, com suporte a usuários, favoritos, busca e modo escuro.

---

## Funcionalidades

- Criar, editar e deletar notas
- Marcar notas como favoritas
- Buscar notas por título ou conteúdo
- Modo escuro/normal
- Login e logout de usuários

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/gabrielbastosg/Bloco-de-Notas.git
cd Bloco-de-Notas

Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Rode as migrations:

python manage.py migrate

Crie um superusuário (opcional, para acessar o admin do Django):

python manage.py createsuperuser

Rode o servidor local:

python manage.py runserver

Acesse http://127.0.0.1:8000/ no navegador.

Tecnologias

Python 3.x

Django 5.2

HTML, CSS (com modo escuro)

Bootstrap 5 (se houver)

Observações

Banco de dados SQLite local

Recomenda-se usar .env ou python-decouple para informações sensíveis

Repositório pronto para deploy com Gunicorn e WhiteNoise

Autor

Gabriel Bastos
