'''Module that describes the views for the courses app.'''
from itertools import chain
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect

from . import forms
from . import models
# Create your views here.

def all_courses(request):
    '''View method to display all courses'''
    courses = models.Course.objects.filter(published=True)
    email = 'questions@learning_site.com'
    return render(request, 'courses/all_courses.html', {'courses': courses,
                                                        'email': email})

def view_course(request, pk):
    '''View method to display a single course'''
    course = get_object_or_404(models.Course, pk=pk, published=True)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                   key=lambda step: step.order)
    return render(request, 'courses/view_course.html', {
        'course': course,
        'steps': steps
        })

def text_detail(request, course_pk, step_pk):
    '''Method to display the steps in a course'''
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk,
                            course__published=True)
    return render(request, 'courses/step_detail.html', {'step': step})

def quiz_detail(request, course_pk, step_pk):
    '''Method to display the details of a quiz'''
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk,
                            course__published=True)
    return render(request, 'courses/quiz_detail.html', {'step': step})

@login_required
def quiz_create(request, course_pk):
    '''Method to create a quiz inside a course'''
    course = get_object_or_404(models.Course, pk=course_pk, 
                                course__published=True)
    form = forms.QuizForm()
    if request.method == 'POST':
        form = forms.QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Quiz Added!")
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/quiz_form.html', {
        'form': form,
        'course': course
        })

##TODO combine this method and the one above into one method
@login_required
def quiz_edit(request, course_pk, quiz_pk):
    '''Method to edit the details of an existing quiz'''
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk, course_id=course_pk,
                            course__published=True)
    form = forms.QuizForm(instance=quiz)
    if request.method == "POST":
        form = forms.QuizForm(instance=quiz, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated {}".format(form.cleaned_data['title']))
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/quiz_form.html', {'form': form, 'course': quiz.course})

@login_required
def create_question(request, quiz_pk, question_type):
    '''Method to create a question inside a quiz'''
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk)
    if question_type == 'tf':
        form_class = forms.TrueFalseQuestionForm
    else:
        form_class = forms.MultipleChoiceQuestionForm
    form = form_class()
    answer_forms = forms.AnswerInlineFormSet(
        queryset=models.Answer.objects.none()
    )

    if request.method == 'POST':
        form = form_class(request.POST)
        answer_forms = forms.AnswerInlineFormSet(
            request.POST,
            queryset=models.Answer.objects.none()
        )
        if form.is_valid() and answer_forms.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            answers = answer_forms.save(commit=False)
            for answer in answers:
                answer.question = question
                answer.save()
            messages.success(request, "Added question")
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/question_form.html', {
        'quiz': quiz,
        'form': form,
        'formset' : answer_forms
    })

@login_required
def edit_question(request, quiz_pk, question_pk):
    '''Method to edit a previous existing question'''
    question = get_object_or_404(models.Question,
                                 pk=question_pk, quiz_id=quiz_pk)
    if hasattr(question, 'truefalsequestion'):
        form_class = forms.TrueFalseQuestionForm
        question = question.truefalsequestion
    else:
        form_class = forms.MultipleChoiceQuestionForm
        question = question.multiplechoicequestion
    form = form_class(instance=question)
    answer_forms = forms.AnswerInlineFormSet(
        queryset=form.instance.answer_set.all()
    )

    if request.method == 'POST':
        form = form_class(request.POST, instance=question)
        answer_forms = forms.AnswerInlineFormSet(
            request.POST,
            queryset=form.instance.answer_set.all()
        )

        if form.is_valid() and answer_forms.is_valid():
            form.save()
            answers = answer_forms.save(commit=False)
            for answer in answers:
                answer.question = question
                answer.save()
            for answer in answer_forms.deleted_objects:
                answer.delete()
            messages.success(request, "Updated question")
            return HttpResponseRedirect(question.quiz.get_absolute_url())
    return render(request, 'courses/question_form.html', {
        'form': form,
        'quiz': question.quiz,
        'formset': answer_forms
    })

@login_required
def answer_form(request, question_pk):
    '''Method to display an answer form'''
    question = get_object_or_404(models.Question, pk=question_pk)

    formset = forms.AnswerFormSet(queryset=question.answer_set.all())

    if request.method == 'POST':
        formset = forms.AnswerFormSet(request.POST,
                                      queryset=question.answer_set.all())

        if formset.is_valid():
            answers = formset.save(commit=False)

            for answer in answers:
                answer.question = question
                answer.save()
            messages.success(request, "Added answers")
            return HttpResponseRedirect(question.quiz.get_absolute_url())
    return render(request, "courses/answer_form.html", {
        'question': question,
        'formset': formset
    })

def courses_by_teacher(request, teacher):
    courses = models.Course.objects.filter(teacher__username="teacher",
                                           published=True)
    return render(request, 'courses/all_courses.html', {'courses': courses})

def search(request):
    term = request.GET.get('q')
    courses = models.Course.objects.filter(
        Q(title__icontains=term)| Q(description__icontains=term),
        published=True
    )
    return render(request, 'courses/all_courses.html', {'courses': courses})