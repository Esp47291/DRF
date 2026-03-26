from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from materials.models import Course, Lesson


class CustomUserManager(BaseUserManager):
    """Менеджер для модели User, где email используется для аутентификации."""

    def create_user(self, email, password=None, **extra_fields):
        """Создаёт обычного пользователя."""
        if not email:
            raise ValueError('Email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создаёт суперпользователя."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


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

    objects = CustomUserManager()  # подключаем кастомный менеджер

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payment(models.Model):
    """Модель платежа"""
    # ... остаётся без изменений