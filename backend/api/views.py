from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from django.shortcuts import get_object_or_404

from products.models import Course, Lesson, Enrollment
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ListModelMixin, GenericViewSet):
    """Вывод списка продуктов(курсов.)"""

    queryset = Course.objects.prefetch_related('lessons', 'group_set', 'student', 'enrollment_set')
    serializer_class = CourseSerializer


class LessonViewSet(ListModelMixin, GenericViewSet):
    """Вывод списка уроков по выбранному продукту(курсу.)"""

    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)

    def get_course(self):
        return get_object_or_404(
            Course,
            enrollment__course=self.kwargs.get('course_id'),
            enrollment__student=self.request.user,
            enrollment__enrolled=True
        )

    def get_queryset(self):
        return self.get_course().lessons.all()


