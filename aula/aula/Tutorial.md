# criando o projeto
django-admin.py startproject aula
cd aula/

# Rodando o servidor
python manage.py runserver

## Configurando o projeto

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'jc1122',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# instalando o MySQL
sudo apt-get update
pip install mysql-python

# criando o BD
mysql -u root -p
jc1122
mysql> create database django;
mysql>exit
workon cv
sudo apt-get install python3-dev

# Criando seu primeiro aplicativo
python manage.py startapp meuslivros

# criando as tabelas
python manage.py syncdb -- substituido
python manage.py imgrate
python manage.py makemigrations
python manage.py migrate

# criando o super usuário
python manage.py createsuperuser
jczars
d4jp1o9s4

# Criando uma página inicial
urls.py

# Adicionando apps no Admin
admin.site.register(meuslivros)

