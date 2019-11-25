''' Models that handle all data in the courses Module.'''
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    '''The course model for all courses.'''
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(default='', max_length=100)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Step(models.Model):
    ''' Step Module that deals with all the steps involved in a a particular
    course.
    '''
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.name = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        '''Metadata for the Step Class'''
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title

class Text(Step):
    '''Text model that inherits from the Abstract Step Model'''
    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        '''Get an absolute url method'''
        return reverse('courses:text', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id
        })

class Quiz(Step):
    '''Model that deals witht he quizzes offered in our learning site'''
    total_questions = models.IntegerField(default=4)
    times_taken = models.IntegerField(default=0, editable=False)

    class Meta:
        '''Metadata for the Quiz class pertaining to how it appears in the admin
        view
        '''
        verbose_name_plural = "Quizzes"

    def get_absolute_url(self):
        '''Get an absolute url method'''
        return reverse('courses:quiz', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id
        })

class Question(models.Model):
    '''Model that deals with the questions in a Quiz'''
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        '''Metadata for the Question model'''
        ordering = ['order',]

    def get_absolute_url(self):
        '''Get an absolute url method'''
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt

class MultipleChoiceQuestion(Question):
    '''Multiple Choice Question model'''
    shuffle_answers = models.BooleanField(default=False)

class TrueFalseQuestion(Question):
    '''Stub for TrueFalseQuestion model'''
    pass


class Answer(models.Model):
    '''Model that handles answers to raised Questions'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        '''MetaData for answer that centres around Ordering'''
        ordering = ['order',]

    def __str__(self):
        return self.text
