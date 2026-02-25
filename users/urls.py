from django.urls import path
from users.views import PaymentListAPIView, UserProfileAPIView

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('users/<int:pk>/', UserProfileAPIView.as_view(), name='user-profile'),
]