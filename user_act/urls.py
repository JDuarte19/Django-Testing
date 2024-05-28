from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('features', views.features, name='features'),
    path('profile',views.profile, name='profile'),
    #path('register', views.register, name='register'),
    path('add_account', views.add_account, name='add_account'),
    path('<int:id>',views.view_account,name='view_account'),
    path('edit/<int:id>', views.edit_info, name='edit_info'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('admin', views.admin, name='admin'),
    path('test', views.test, name='test'),
]