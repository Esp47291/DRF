from django.core.management.base import BaseCommand
from users.models import User, Payment
from materials.models import Course, Lesson

class Command(BaseCommand):
    help = 'Создает тестовые платежи'

    def handle(self, *args, **options):
        user = User.objects.first()
        course = Course.objects.first()
        lesson = Lesson.objects.first()

        if not user:
            self.stdout.write(self.style.ERROR('Нет пользователей. Сначала создай пользователя.'))
            return

        if not course:
            self.stdout.write(self.style.WARNING('Нет курсов. Платеж за курс создан не будет.'))
        if not lesson:
            self.stdout.write(self.style.WARNING('Нет уроков. Платеж за урок создан не будет.'))

        # Платеж за курс
        if course:
            Payment.objects.get_or_create(
                user=user,
                paid_course=course,
                defaults={
                    'amount': 5000,
                    'payment_method': 'transfer'
                }
            )
            self.stdout.write(f'Платеж за курс "{course.title}" создан.')

        # Платеж за урок
        if lesson:
            Payment.objects.get_or_create(
                user=user,
                paid_lesson=lesson,
                defaults={
                    'amount': 1500,
                    'payment_method': 'cash'
                }
            )
            self.stdout.write(f'Платеж за урок "{lesson.title}" создан.')

        self.stdout.write(self.style.SUCCESS('Готово!'))