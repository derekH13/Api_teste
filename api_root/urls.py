
from django.contrib import admin
from django.urls import path, include

#quando o caminho estiver na url ele busca os arquivos
urlpatterns = [
    path('admin/', admin.site.urls),
    #direciona para a pasta api_rest arquivo urls
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
]
