from django.conf.urls import url

from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.all_courses, name="list"),
    url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)$', views.text_detail, name="text"),
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)$', views.quiz_detail, name="quiz"),
    url(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create, name="create_quiz"),
    url(r'(?P<pk>\d+)/$', views.view_course, name='detail'),
]