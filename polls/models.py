from django.db import models

class Student(models.Model):
    ra = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Department(models.Model):
    name = models.CharField(max_length=255)

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    departmentId = models.ForeignKey('Department', on_delete=models.CASCADE)
