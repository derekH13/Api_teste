from django.db import models

#class dos usuarios
class User(models.Model):
    
    #campos do banco de dados e suas propriedades
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    #metodo magico
    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'

#para criar o modelo no banco de dados é py manage.py makemigrations, py manage.py migrate



class UserTasks(models.Model):
    user_nickname = models.CharField(max_length=100, default='')
    user_task = models.CharField(max_length=255, default='')
