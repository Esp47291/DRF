from rest_framework import serializers
from users.models import User, Payment
from materials.serializers import CourseSerializer, LessonSerializer


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для платежей с детальной информацией
    """
    # Добавляем детальную информацию о курсе и уроке
    user_email = serializers.EmailField(source='user.email', read_only=True)
    paid_course_detail = CourseSerializer(source='paid_course', read_only=True)
    paid_lesson_detail = LessonSerializer(source='paid_lesson', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'user_email',
            'payment_date',
            'amount',
            'payment_method',
            'paid_course',
            'paid_course_detail',
            'paid_lesson',
            'paid_lesson_detail',
        ]
        read_only_fields = ['payment_date']


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя с историей платежей (дополнительное задание)
    """
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments']