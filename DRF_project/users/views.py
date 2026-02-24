from rest_framework import generics
from users.models import Payment
from users.serializers import PaymentSerializer

class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer