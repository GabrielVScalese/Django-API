# Deploy no Heroku + PostgreSQL

- Instalar pela venv: 'django-heroku', 'psycopg2', 'gunicorn' e 'whitenoise'
- Criar arquivo runtime.txt
- Criar arquivo Procfile
- Criar aplicação no Heroku e adicionar database
- No settings.py: definir credenciais de acesso ao database; criar variável 'STATIC_ROOT'; configurar integração do django com Heroku e definir 'ALLOWED_HOSTS' com a rota da sua aplicação Heroku'
- Rodar 'python manage.py makemigrations' e 'python manage.py migrate', inicializando migrations no database
- Por fim, realizar deploy do projeto pelo próprio Heroku



