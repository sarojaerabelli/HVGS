import datetime

from django.db import models
from django.utils import timezone
from listfield import ListField


DEGREE_CHOICES = (
    ('BA', "B.A./B.S."),
    ('MA', "M.A./M.S."),
    ('DO', "Ph.D. or Higher")
)


def faces_directory_path(instance, filename):
    import pdb; pdb.set_trace();
    return 'media/faces/{0}'.format(instance.face_picture.id)



class Hiree(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=10, choices=DEGREE_CHOICES)
    year = models.IntegerField()
    major = models.CharField(max_length=100)
    face_picture = models.ImageField(upload_to=faces_directory_path)
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

class Relations(models.Model):
    hiree = models.ForeignKey(Hiree, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    encounter_date = models.DateTimeField(default=datetime.datetime.now())
    # 0 = not considered yet or deferred
    # 1 = rejected
    # 2 = accepted
    status = models.CharField(choices=( ('0', "Undecided"), ('1', "Rejected"), ('2', "Accepted") ), max_length=20)
