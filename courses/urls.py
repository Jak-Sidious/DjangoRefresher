'''Method to deal with the urls within the courses app'''
from django.conf.urls import url

from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.all_courses, name="list"),
    url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)$', views.text_detail, name="text"),
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)$', views.quiz_detail, name="quiz"),
    url(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create, name="create_quiz"),
    url(r'(?P<course_pk>\d+)/edit_quiz/(?P<quiz_pk>\d+)$', views.quiz_edit, name="edit_quiz"),
    url(r'(?P<pk>\d+)/$', views.view_course, name='detail'),
    url(r'(?P<quiz_pk>\d+)/create_question/(?P<question_type>mc|tf)/$',
        views.create_question, name="create_question"),
    url(r'(?P<question_pk>\d+)/create_answer/$', views.answer_form, name="create_answer"),
    url(r'(?P<quiz_pk>\d+)/edit_question/(?P<question_pk>\d+)$',
        views.edit_question, name="edit_question"),
]
 