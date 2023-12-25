from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import formLogin
from .models import Menu
from .forms import MenuForm


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
   menus = Menu.objects.all()
   context = {
       'menus': menus
   }
   return render(request, 'menu.html', context)
    
def menuDetails(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
        context = {
            'menu': menu
        }
    except Menu.DoesNotExist:
        raise Http404('Menu tidak ditemukan')
    return render(request, 'menudetail.html', context)

def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            new_menu = MenuForm(request.POST)
            new_menu.save()
            messages.success(request, 'Sukses Menambah Menu')
            return redirect('menu')
    else:
        form = MenuForm()
    return render(request, 'formMenu.html', {'form': form})

def update_menu(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)

    except Menu.DoesNotExist:
        raise Http404("Menu does not exist")
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu has been updated')
            return redirect('menu')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'formMenu.html', {'form': form})

def delete_menu(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
        menu.delete()
        messages.success(request, 'Menu deleted successfully')
        return redirect('menu')
    except Menu.DoesNotExist:
        raise Http404('Menu not exists')



def about(request):
    
    template = loader.get_template('about.html')
    
    return HttpResponse(template.render())

    
def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

