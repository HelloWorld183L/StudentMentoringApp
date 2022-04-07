from django.db import models

# Create your models here.

class Mentor(models.Model):
    name = models.CharField(max_length=50)
    subject_area = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
