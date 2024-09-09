
from django.contrib import admin
from django.urls import path

from . import views

# agr em api/ ele busca a função de views get_users
#essas urls vem todas depois de api/
urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nick),
    #a url usada disso é data/?user=<nick>
    path('data/', views.user_manager), #todo o crud vai estar aqui
]
