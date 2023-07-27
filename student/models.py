from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=126)
    rollnumber = models.CharField(max_length=126)
    mail_id = models.EmailField(max_length=256)
    password = models.CharField(max_length=126)
    dob = models.DateField()

