'''Module to deal with the views inside learning site. '''
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from . import forms


def hello_world(request):
    '''First view seen on the site'''
    return render(request, 'home.html')

def suggestion_view(request):
    '''
    View that corresponds to the suggestions to be raised
    '''
    form = forms.SuggestionForm()
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['tickle@tickle.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World!")
