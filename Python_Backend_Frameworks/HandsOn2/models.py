from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)