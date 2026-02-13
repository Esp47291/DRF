from rest_framework import viewsets, generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

# CourseViewSet остаётся без изменений
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# ---- Generic-классы для Lesson ----

class LessonListAPIView(generics.ListAPIView):
    """
    Получение списка уроков
    GET /lessons/
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Создание урока
    POST /lessons/create/
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получение одного урока
    GET /lessons/{id}/
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление урока
    PUT /lessons/{id}/update/  (полное обновление)
    PATCH /lessons/{id}/update/ (частичное обновление)
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление урока
    DELETE /lessons/{id}/delete/
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer