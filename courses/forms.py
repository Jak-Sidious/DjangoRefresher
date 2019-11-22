'''Class that deals with the various Model forms to be created'''
from django import forms
from . import models

class QuizForm(forms.ModelForm):
    '''Method to create a form from the Quiz Model'''
    class Meta:
        '''Meta Data for the QuizFormClass'''
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]

class TrueFalseQuestionForm(forms.ModelForm):
    '''Method to create a form from the TrueFalseQuestionForm'''
    class Meta:
        '''Meta Data for the TrueFalseQuestionFormClass'''
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt']

class MultipleChoiceQuestionForm(forms.ModelForm):
    '''Method to create a form from the MultipleChoiceQuestionForm'''
    class Meta:
        '''Meta Data for the MultipleChoiceQuestionForm'''
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers',
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct',
        ]

AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm
)
