from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import formLogin

def loginForm(request): 
    context = {}
    context['form'] = formLogin()
    return render(request, "formlogin.html", context)

def kopiratjad(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())