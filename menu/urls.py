from django.urls import path
from . import views


urlpatterns = [
    path('', views.kopiratjad, name='kopiratjad'),
    path('login/', views.loginForm, name='loginForm'),
    path('daftar/', views.formDaftar, name='formdaftar'),
    path('index/', views.kopiratjad, name='kopiratjad'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('menuDetails/<int:menu_id>', views.menuDetails, name='detail'),
    path('creatMenu', views.create_menu, name='creatMenu'),
    path('update/<int:menu_id>', views.update_menu, name='update'),
    path('delete/<int:menu_id>', views.delete_menu, name='delete'),
    ]
