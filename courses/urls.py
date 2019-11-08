from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_courses),
    url(r'(?P<pk>\d+)/$', views.view_course),
]