from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    photo = models.TextField(max_length=250, null=None, blank=None, default="default_picture.png")
    nickname = models.TextField(max_length=50, null=None, blank=None, unique=True)
    password = models.TextField(max_length=250, null=None, blank=None)
    firstname = models.TextField(max_length=250, null=None, blank=None)
    lastname = models.TextField(max_length=250)
    biography = models.TextField(max_length=250)
    email = models.EmailField(max_length=250, null=None, blank=None)
    commit = models.DateTimeField(null=None, blank=None, default=datetime.now)
    modified = models.DateTimeField(null=True)
    status = models.IntegerField(null=None, blank=None, default=1)
