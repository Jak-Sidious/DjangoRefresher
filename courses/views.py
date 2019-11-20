from itertools import chain
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
# Create your views here.

def all_courses(request):
    courses = models.Course.objects.all()
    email = 'questions@learning_site.com'
    return render(request, 'courses/all_courses.html', {'courses': courses,
                                                        'email': email})

def view_course(request, pk): 
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                    key=lambda step: step.order)
    return render(request, 'courses/view_course.html', {
            'course': course,
            'steps': steps
        })

def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})