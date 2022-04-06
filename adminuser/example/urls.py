from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('register',views.register,name='register'),
    # path('login',views.login, name='login'),
    # path('logout',views.logout,name='logout'),
    # path('home',views.home,name='home'),
    path('register',views.user_form,name='register'),
    path('<int:id>/register',views.user_form,name='register'),
    path('<int:id>/',views.user_form, name='update'),
    path('delete/<int:id>/',views.user_delete, name='delete'),
    path('list',views.user_list, name='list'),
    path('<int:id>/list',views.user_list, name='list'),
    # path('clist',views.user_chnged_list, name='clist'),
    path('',views.user_login, name='login'),
    path('logout',views.user_logout, name='logout'),
    path('change/<int:id>/',views.user_change, name='change'),
    path('change/<int:id>/pschnge',views.user_detail, name='detail'),
    path('idetail',views.user_detail, name='idetail'),
   
    
    
]