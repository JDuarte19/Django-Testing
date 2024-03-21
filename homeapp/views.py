from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import userSet, Term, User

# Create your views here.
# index view basically
class LibraryView(generic.ListView):
    template_name = "homeapp/library.html"
    context_object_name = "library_list"

    def get_queryset(self):
        return userSet.objects.all()
# view all sets
class SetView(generic.TemplateView):
    model = userSet
    template_name = "homeapp/setpage.html"

def home(request):
    return render(request,'homeapp/home.html')
