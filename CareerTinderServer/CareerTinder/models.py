import datetime

from django.db import models
from django.utils import timezone


class Hiree(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date of birth')
    face_picture = models.FileField('face')
    resume_picture = models.FileField('resume')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.FileField('company logo')

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    interested_hirees = models.ForeignKey(Hiree, default=[])

    def __str__(self):
        return "%s from %s" % (self.name, self.company)
