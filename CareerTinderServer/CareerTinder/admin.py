from django.contrib import admin
from .models import Hiree, Company, Recruiter, Relations

# Register your models here.
admin.site.register(Hiree)
admin.site.register(Company)
admin.site.register(Recruiter)
admin.site.register(Relations)
