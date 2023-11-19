from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def menu(request):
    template = loader.get_template('indext.html')
    return HttpResponse(template.render())