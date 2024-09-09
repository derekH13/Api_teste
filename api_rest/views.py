from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json


# só a requsição lista de usuarios
@api_view(['GET'])
def get_users(request):

    # verificar se é get
    if request.method == 'GET':

        # devolve todos os objetos de Users
        users = User.objects.all()

        # pega os objetos que foram retornados e serializa eles, por ser mais de um (many=True)
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    # fora do if, se for algo q não seja get
    return Response(status=status.HTTP_400_BAD_REQUEST)


# exemplo de como pegar a varivel passada pela url(nick)**
@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):

    try:
        # consulta um objetos de User que coresponde a 'pk' = nick
        user = User.objects.get(pk=nick)

    except:
        # se try der erro
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # transforma o bjeto em json
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # fazendo a parte de edição de dados
    if request.method == 'PUT':
        # user esse que é a pk, ja consultada, e passa a informação passada para edição
        serializer = UserSerializer(user, data=request.data)

        # verifica se a informação é valid
        if serializer.is_valid():
            # salva no banco de dados
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        # aqui esta fora do if
        return Response(status=status.HTTP_400_BAD_REQUEST)


















# CRUDZAO DA MASSA
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    # ACESSOS

    if request.method == 'GET':

        try:
            # verifica se existe um paramtro chamado 'user' (/?user=xxxx&...)
            if request.GET['user']:

                # pega o valor do parametro
                user_nickname = request.GET['user']

                try:
                    # consulta um objeto em banco de dados user com pk = user_nickname
                    user = User.objects.get(pk=user_nickname)

                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                # serializa o objeto data em json
                serializer = UserSerializer(user)
                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# CRIANDO DADOS

    # sempre conffirma o method
    if request.method == 'POST':

        # pega os dados que foram enviados
        new_user = request.data

        # diferente de serializar objetos, estamos serializando dados no parametro (data=<dados>)
        # é importante que os dados tenha os mesmos campos que o modelo feito em model
        serializer = UserSerializer(data=new_user)

        # função is_valid() verifica se os dados são validos
        if serializer.is_valid():
            # salva no banco de dados
            serializer.save()
            # retorna o proprio objeto e o status
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # se não entrar no if
        return Response(status=status.HTTP_400_BAD_REQUEST)


# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        # nos dados do request, no objeto pega a propriedade user_nickname (pk)
        nickname = request.data['user_nickname']

        try:
            # faz a consulta
            updated_user = User.objects.get(pk=nickname)
        except:
            # se a consulta do pk der errado
            return Response(status=status.HTTP_404_NOT_FOUND)

        # serializa o objeto/request data
        # no parametro dizemos o objeto que será editado, ele pega o primeiro parametro e coloca os dados do segundo
        serializer = UserSerializer(updated_user, data=request.data)

        # se for valido vai entrar no if e salvar no banco de dados
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            #tenta fazer a busca no banco de dados pela propriedades user_nickname do request
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            #ao achar não é preciso confirmar a validação (não tem logica), só deletar
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)