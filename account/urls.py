from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('get-started/', views.getstarted, name='get-started'),
    path('create-post/', views.createpost, name='create-post'),
    path('commisioner-join/', views.signupCommisioner, name='commisioner-join'),
    path('principal-join/', views.principalsignup, name='principal-join'),
    path('student-join/', views.studentsignup, name='student-join'),
    path('district-join/', views.signupDistricthead, name='district-join'),
    path('state-district/', views.signupStatedistrict, name='state-district'),
    path('fedral-district/', views.signupFeddistrict, name='fedral-district'),
    path('manage-comissioners/', views.managecommissioner, name='manage-comissioners'),
    path('school/', views.school, name='school'),
    path('create-school/', views.createschool, name='create-school'),
    path('school-profile/<str:pk>', views.schoolprofile, name='schoolprofile'),
]