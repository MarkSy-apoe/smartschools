from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('get-started/', views.getstarted, name='get-started'),
    path('commisioner-join/', views.signupCommisioner, name='commisioner-join'),
    path('district-join/', views.signupDistricthead, name='district-join'),
    path('state-district/', views.signupStatedistrict, name='state-district'),
    path('fedral-district/', views.signupFeddistrict, name='fedral-district'),
]