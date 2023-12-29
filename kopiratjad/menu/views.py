from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from .forms import formLogin
from .models import Menu
from .forms import MenuForm
from .forms import RegisterForm


def loginView(request):
    form = formLogin()
    
    if request.method == 'POST':
        form = forms.formLogin(request.POST)
        
        if form.is_valid():
           user = authenticate( 
               username = form.cleaned_data['username'],
               password = form.cleaned_data['password'],
               )
           if user is not None:
                login(request, user)
                return redirect('/index')
        else:
            form.add_error(None, "Invalid email or password")
        
    
    return render(request, 'formlogin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

# def register(request):
#     if request.method == 'GET':
#         return render(request, 'register.html', {'form': RegisterForm})
#     elif request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user= form.save(commit=False)
#             user.is_valid = False
#             user.save()
#         else:
#             messages.info(request, 'invalid registration')
#             return render(request, 'register.html', {'form': RegisterForm})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  
        if form.is_valid():
             form.save()
             messages.success(request, "Register successfully")
             return redirect('login')
        messages.error(request, "unsuccessful registration")
    form = RegisterForm()
    return render(request, 'register.html', {"form": form})

def kopiratjad(request):
    return render(request, 'index.html')
           

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

def menuSOP(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
        context = {
            'menu': menu
        }
    except Menu.DoesNotExist:
        raise Http404('Menu tidak ditemukan')
    return render(request, 'SOP.html', context)


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

