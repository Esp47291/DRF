from django.db import models


class Course(models.Model):
    """
    Модель курса
    """
    title = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='courses/', verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']  # сортировка по убыванию даты создания

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Модель урока. Связана с курсом (ForeignKey)
    """
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lessons/', verbose_name='Превью', blank=True, null=True)
    video_link = models.URLField(verbose_name='Ссылка на видео', max_length=500)

    # Связь с курсом: один курс - много уроков
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,  # при удалении курса удаляются все его уроки
        related_name='lessons',  # позволяет обращаться course.lessons.all()
        verbose_name='Курс'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['title']  # сортировка по названию

    def __str__(self):
        return self.title