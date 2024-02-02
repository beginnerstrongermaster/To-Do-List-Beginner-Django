from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField()
    completed = models.BooleanField(default=False)
    createTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
