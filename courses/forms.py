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

class QuestionForm(forms.ModelForm):
    '''Method to create a form that utilises external css'''
    class Media:
        '''Media data that is utilised by this form'''
        css = {'all':('courses/css/order.css',)}
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',
            'courses/js/order.js'
        )

class TrueFalseQuestionForm(QuestionForm):
    '''Method to create a form from the TrueFalseQuestionForm'''
    class Meta:
        '''Meta Data for the TrueFalseQuestionFormClass'''
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt']

class MultipleChoiceQuestionForm(QuestionForm):
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
    '''Model form that deals with the Answer model'''
    class Meta:
        '''Metadata for the AnswerForm Class'''
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

AnswerInlineFormSet = forms.inlineformset_factory(
    models.Question,
    models.Answer,
    extra=2,
    fields=('order', 'text', 'correct'),
    formset=AnswerFormSet,
    min_num=1,
)
