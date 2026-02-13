from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    Наследуемся от AbstractUser, чтобы взять всё от обычного User,
    но меняем поле для авторизации на email.
    """
    username = None  # убираем поле username
    email = models.EmailField(unique=True, verbose_name='Email')

    # Добавляем новые поля
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='Город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', blank=True, null=True)

    # Указываем, что поле email будет использоваться для входа
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # обязательные поля при createsuperuser (кроме email)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email