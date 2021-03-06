from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# class User(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # Unique ID
#     username = models.CharField(max_length=200, unique=True) # one string no bigger than 200 chars
#     password = models.CharField(max_length=200) # one string no bigger than 200 chars
#     created_at = models.DateTimeField(auto_now_add=True) # like Date.now() automatically calculated on creation

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # Unique ID
    title = models.CharField(max_length=200) # one string no bigger than 200 chars
    content = models.TextField(blank=True) # a text block as big as it permits: can be empty
    created_at = models.DateTimeField(auto_now_add=True) # like Date.now() automatically calculated on creation
    last_modified = models.DateTimeField(auto_now=True) # When it was last edited auto calculater
    url = models.URLField(default='')
    
class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

