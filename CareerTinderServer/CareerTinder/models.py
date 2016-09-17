from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=200)
	date_of_birth = models.DateTimeField('date of birth')
	face_picture = models.FileField('face')

class Company(models.Model):
	name = models.CharField(max_length=200)
	logo = models.FileField('company logo')
