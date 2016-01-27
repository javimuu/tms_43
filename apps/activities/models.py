from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    content = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

