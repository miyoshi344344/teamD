from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)

    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    elective_subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name
