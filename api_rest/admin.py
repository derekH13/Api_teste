from django.contrib import admin

#importar os models 
from .models import User

#registrando a class que foi criada
admin.site.register(User)

#registrar um super usuario py manage.py createsuperuser