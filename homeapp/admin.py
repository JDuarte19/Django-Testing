from django.contrib import admin
from .models import userSet, Term,User

# Register your models here.

admin.site.register(User)
admin.site.register(userSet)
admin.site.register(Term)