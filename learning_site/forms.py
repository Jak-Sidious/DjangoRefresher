'''Forms to be displayed within the main app Learningsite.py'''
from django import forms
from django.core import validators


def must_be_empty(value):
    '''Method to ensure the honeypot is empty and if not raise a validation
    error
    '''
    if value:
        raise forms.ValidationError('is not empty')
class SuggestionForm(forms.Form):
    ''' Method to create the Suggestions form '''
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput, label="Leave Empty",
                               validators=[must_be_empty])

    def clean(self):
        '''clean method to scrub the data and return and error incase email and
        verify email don't have the same data
        '''
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']

        if  email != verify:
            raise forms.ValidationError(
                "The two email fields don't match")


    # def clean_honeypot(self):
    #     honeypot = self.cleanrd_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError(
    #             "Honeypot should be left empty. Bad Bot1")
    #     return honeypot
