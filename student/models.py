from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.name