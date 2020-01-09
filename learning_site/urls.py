"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from rest_framework import routers
from ed_reviews import views as view2
from teams import views as view3
from . import views


router = routers.SimpleRouter()
router.register(r'courses', view2.CourseViewSet)
router.register(r'reviews', view2.ReviewViewSet)


urlpatterns = [
    path('courses/', include('courses.urls', namespace='courses')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', 
                                namespace='rest_framework')),
    path('api/v1/courses/', include('ed_reviews.urls', namespace='reviews')),
    path('api/v2/', include((router.urls, "reviews"), namespace="apiv2")),
    path('', views.HomeView.as_view(), name='goHome'),
    path('hello/', views.HelloWorldView.as_view(), name='hello'),
    path('suggest/', views.suggestion_view, name='suggestion'),
    path('teams/', include('teams.urls', namespace='teams')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += staticfiles_urlpatterns()
