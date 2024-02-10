from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(null = True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Topic(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updates = models.DateTimeField(auto_now = True) # takes a snapshot of the database whenever the save method is called
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        # -updated means in descending order
        ordering  = ['-updates', '-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField()
    updates = models.DateTimeField(auto_now = True) # takes a snapshot of the database whenever the save method is called
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        # -updated means in descending order
        ordering  = ['-updates', '-created']

    def __str__(self):
        return self.body[0:50] # preview only first 50 characters
