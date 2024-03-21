from django.urls import path
from . import views

app_name = "homeapp"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/set/<int:pk>/",views.SetView.as_view(), name="setpage"),
    path("home/library", views.LibraryView.as_view(), name="library"),
]