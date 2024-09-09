from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # aqui será escolhido qual o campo que será serializado para json
        model = User
        # e aqui diz o campo (nesse caso todos)
        fields = '__all__'
