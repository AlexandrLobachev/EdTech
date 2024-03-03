from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from products.models import Course, Lesson

User = get_user_model()


class CourseSerializer(ModelSerializer):
    """Вывод списка курсов."""

    qty_lessons = SerializerMethodField()
    qty_students = SerializerMethodField()
    filling = SerializerMethodField()
    popularity = SerializerMethodField()

    class Meta:
        fields = (
            'name',
            'description',
            'start_date',
            'price',
            'qty_lessons',
            'qty_students',
            'filling',
            'popularity',
        )
        model = Course

    def get_qty_lessons(self, obj):
        return obj.lessons.count()

    def get_qty_students(self, obj):
        return obj.student.count()

    def get_filling(self, obj):
        qty_groups = obj.group_set.count()
        if qty_groups == 0:
            return 'Групп не сформировано'
        return (((obj.student.count() / qty_groups)
                / obj.max_qty_students) * 100)

    def get_popularity(self, obj):
        qtu_users = User.objects.count()
        if qtu_users == 0:
            return 'Нет ни одного пользователя'
        return (obj.enrollment_set.count() / User.objects.count()) * 100


class LessonSerializer(ModelSerializer):
    """Вывод списка уроков."""

    class Meta:
        fields = (
            'name',
        )
        model = Lesson