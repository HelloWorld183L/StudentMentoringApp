from django.db import models

class Mentor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    course = models.CharField(max_length=50)
    current_year = models.IntegerField(max_length=1)

    class Meta:
        ordering = ["-name"]

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    subject_area = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    email = models.EmailField()
    current_year = models.IntegerField(max_length=1)

    class Meta:
        ordering = ["name"]
