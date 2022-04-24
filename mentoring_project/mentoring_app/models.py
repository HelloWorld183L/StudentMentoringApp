from django.db import models

class Mentor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    subject_area = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
