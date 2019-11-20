from django import forms
from django.core import validators

def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')
class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, 
                                widget=forms.HiddenInput, label="Leave Empty",
                                validators=[must_be_empty])

    # def clean_honeypot(self):
    #     honeypot = self.cleanrd_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError(
    #             "Honeypot should be left empty. Bad Bot1")
    #     return honeypot