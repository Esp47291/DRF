# materials/serializers.py

from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для урока
    """

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для курса с вложенными уроками
    """
    # Добавляем поле lessons, которое будет содержать все уроки этого курса
    lessons = LessonSerializer(many=True, read_only=True)
    # many=True - потому что уроков много
    # read_only=True - чтобы нельзя было создать урок через курс

    # Можно добавить количество уроков для статистики
    lessons_count = serializers.IntegerField(source='lessons.count', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'  # теперь сюда входит и lessons