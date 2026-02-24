from rest_framework import serializers
from users.models import User, Payment
from rest_framework import generics
from users.models import User

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)  # вложенные платежи

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments']  # добавляем payments


class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # можно ограничить доступ, например, только свой профиль