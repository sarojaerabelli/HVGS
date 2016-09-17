from django.db import models


class Hiree(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date of birth')
    face_picture = models.FileField('face')
    resume_picture = models.FileField('resume')


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.FileField('company logo')


class Recruiter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
