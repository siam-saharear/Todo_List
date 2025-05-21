from django.db import models

from uuid import uuid4

# Create your models here.
class Category(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key= True, verbose_name="category uuid")
    name = models.CharField(max_length=50, verbose_name="category name")
    description = models.CharField(max_length=100, verbose_name="category description")
    creation_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=30, choices=[("exercise", "Exercise"),("chores", "Chores"),("academic", "Academic"),("code", "Code"),("habit","Habit"),("other","Other")], default="NA")
    status = models.BooleanField(default=False,)
    def __str__(self):
        return self.name
        
class Task(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, verbose_name="task uuid")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null= True)
    name = models.CharField(max_length=50, verbose_name="task name")
    descripiton = models.CharField(max_length=100, verbose_name="task description")
    creation_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=30, choices=[("exercise", "Exercise"),("chores", "Chores"),("academic", "Academic"),("code", "Code"),("habit","Habit"),("other","Other")], default="NA")
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

