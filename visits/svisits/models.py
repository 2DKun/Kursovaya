from django.db import models


# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class Visits(models.Model):
    visits_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

