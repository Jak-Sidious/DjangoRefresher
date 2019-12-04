from django.conf.urls import url

from . import views

app_name = "reviews"

urlpatterns = [
    url(r'^$', views.ListCreateCourse.as_view(), name='course_list'),
    url(r'(?P<pk>\d+)/$', 
        views.RetrieveUpdateDestroyCourse.as_view(),name='course_detail'),
]