from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import formLogin
from django.contrib.auth import authenticate, login


def kopiratjad(request):
    return render(request, 'index.html')
           

def loginForm(request): 
    if request.method == 'POST':
        form = formLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            form.add_error(None, "Invalid email or password")
        
    else:
        
        form = formLogin()
    return render(request, 'formlogin.html', {'form': form})
    

def formDaftar(request):
    template = loader.get_template('formdaftar.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    
    template = loader.get_template('about.html')
    
    return HttpResponse(template.render())
def furniture(request):
    template = loader.get_template('furniture.html')
    
    return HttpResponse(template.render())
def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

