from django.db import models

# Create your models here.

class User(models.Model):
    user_id  = models.CharField(max_length=15)
    user_email = models.CharField(max_length=100)
    creation_date = models.DateTimeField("date created")
    def __str__(self):
        return self.user_id
    
class userSet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    set_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField("date created")
    def __str__(self):
        return self.set_name

class Term(models.Model):
    set_name = models.ForeignKey(userSet, on_delete=models.CASCADE)
    term = models.CharField(max_length=200)
    termDef = models.CharField(max_length=300, default="temp definition//please replace")
    def __str__(self):
        return self.term
