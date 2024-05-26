from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('/register', views.register, name='register'),
    path('/reg_account/', views.reg_account, name='reg_account'),
    path('/test', views.test, name='test'),
]