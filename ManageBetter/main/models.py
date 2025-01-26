from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    todo = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="todos")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo
