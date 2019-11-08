from django.conf.urls import url

from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.all_courses, name="list"),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_detail, name="step"),
    url(r'(?P<pk>\d+)/$', views.view_course, name='detail'),
]