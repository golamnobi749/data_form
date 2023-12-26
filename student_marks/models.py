from django.db import models

# Create your models here.
class Student_info(models.Model):
    student_name = models.CharField(max_length=15)
    father_name = models.CharField(max_length=15)
    mother_name = models.CharField(max_length=15)
    bangla = models.CharField(max_length=15)
    english = models.CharField(max_length=15)
    math = models.CharField(max_length=15)
    social_science = models.CharField(max_length=15)
    general_science = models.CharField(max_length=15)
    religion = models.CharField(max_length=15)
    point = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)
    text_area = models.CharField(max_length=150)

