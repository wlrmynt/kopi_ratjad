from django.urls import path
from . import views


urlpatterns = [
    path('', views.kopiratjad, name='kopiratjad'),
    path('login/', views.loginForm, name='loginForm'),
    path('daftar/', views.formDaftar, name='formdaftar'),
    path('index/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('furniture/', views.furniture, name='furniture'),
    path('contact/', views.contact, name='contact'),
#     path('belanja/', views.shoping, name='shoping'),
#     path('detailshoping/<int:id>', views.shopingdetails, name='shopingdetails'),
]