from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.

def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/all_courses.html', {'courses': courses})

def view_course(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/view_course.html', {'course': course})