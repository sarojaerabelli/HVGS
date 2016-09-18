import datetime

from django.db import models
from django.utils import timezone
from listfield import ListField

class Hiree(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField('date of birth')
    face_picture = models.ImageField(upload_to='media/faces/')
    resume_picture = models.FileField(upload_to='media/resumes/')

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='media/logos/')

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    hirees = ListField(default="")

    def __str__(self):
        return "%s from %s" % (self.name, self.company)
