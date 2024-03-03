from django.urls import include, path
from rest_framework import routers

from .views import CourseViewSet, LessonViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()

router_v1.register('courses', CourseViewSet, basename='course')
router_v1.register(
    r'courses/(?P<course_id>\d+)/lessons',
    LessonViewSet,
    basename='lesson')

urlpatterns = [
    path('', include(router_v1.urls)),
]