import datetime
import numpy as np

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

User = get_user_model()


class Course(models.Model):
    name = models.CharField('Курс', max_length=20)
    teacher = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Преподаватель',
    )
    price = models.PositiveSmallIntegerField('Стоимость')
    start_date = models.DateTimeField('Дата и время старта')
    description = models.TextField('Описание')
    min_qty_students = models.PositiveSmallIntegerField(
        'Минимальное количество студентов в группе'
    )
    max_qty_students = models.PositiveSmallIntegerField(
        'Максимальное количество студентов в группе'
    )
    student = models.ManyToManyField(
        User,
        verbose_name='Студент',
        related_name='courses',
        through='Enrollment',
    )

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'

    )
    enrolled = models.BooleanField()

    class Meta:
        verbose_name = 'Зачисление'
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'course'), name='unique_student_on_course',
            )]


class Lesson(models.Model):
    name = models.CharField('Урок', max_length=30)
    link_video = models.URLField('Ссылка на урок')
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
        related_name= 'lessons'
    )

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(
        'Группа',
        max_length=20,
        blank=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
    )
    student = models.ManyToManyField(
        User,
        verbose_name='Студент',)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Group)
def get_name(sender, instance, **kwargs):
    instance.name = f'{instance.course}-{instance.course.group_set.count() + 1}'


@receiver(post_save, sender=Enrollment)
def distribution_by_groups(sender, instance, **kwargs):
    if (datetime.datetime.now(datetime.timezone.utc)
            > instance.course.start_date):
        return

    student = User.objects.get(username=instance.student)
    course = Course.objects.get(name=instance.course)
    students = course.student.all()
    qty_students = students.count()

    if qty_students == instance.course.min_qty_students:
        group = Group.objects.create(course=instance.course)
        group.student.set(students)

    elif (instance.course.min_qty_students < qty_students
          <= instance.course.max_qty_students):
        group = Group.objects.get(course=instance.course)
        group.student.add(student.id)

    elif qty_students > instance.course.max_qty_students:
        groups = course.group_set.all()
        qty_groups = groups.count()
        if (qty_students / qty_groups) > qty_groups:
            Group.objects.create(course=course)
            groups = course.group_set.all()
            qty_groups += 1
        groups_students = np.array_split(students, qty_groups)
        for index in range(qty_groups):
            groups[index].student.set(groups_students[index])
