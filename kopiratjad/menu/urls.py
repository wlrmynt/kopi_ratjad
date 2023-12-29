from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.loginView, name='login'),
    path('login/',views.loginView, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register, name='register'),


    path('index/', views.kopiratjad, name='kopiratjad'),
    path('about/', views.about, name='about'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),

    path('menu/',views.menu, name='menu'),
    path('menuDetails/<int:menu_id>', views.menuDetails, name='detail'),
    path('menuSOP/<int:menu_id>', views.menuSOP, name='sop'),

    path('creatMenu', views.create_menu, name='creatMenu'),
    path('update/<int:menu_id>', views.update_menu, name='update'),
    path('delete/<int:menu_id>', views.delete_menu, name='delete'),

    ]
