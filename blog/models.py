from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

class Article (models.Model):
    title = models.CharField(max_length=255)
    author =models.ForeignKey(get_user_model() ,on_delete=models.CASCADE ,blank = True, null = True)
    time_created =models.DateTimeField(auto_now_add=True)
    time_updated=models.DateTimeField(auto_now=True)
    content =models.TextField()
    published = models.BooleanField(null=True)


    def __str__(self):
        return self.title

