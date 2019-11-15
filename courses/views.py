from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, Step
# Create your views here.

def all_courses(request):
    courses = Course.objects.all()
    email = 'questions@learning_site.com'
    return render(request, 'courses/all_courses.html', {'courses': courses,
                                                        'email': email})

def view_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/view_course.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})