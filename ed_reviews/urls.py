from django.conf.urls import url

from . import views

app_name = "reviews"

urlpatterns = [
    url(r'^$', views.ListCourse.as_view(), name='course_list')
]