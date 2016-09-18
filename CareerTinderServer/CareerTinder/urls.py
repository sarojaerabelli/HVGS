from django.conf.urls import url

from . import views, tinder, resume_upload, resume_retrieval, take_picture

urlpatterns = [
    url(r'^review', tinder.index, name='index'),
    url(r'^upload', resume_upload.list, name='list'),
    url(r'^retrieve', resume_retrieval.index, name='index'),
    url(r'^picture', take_picture.index, name='index'),
    url(r'^$', views.index, name='index')
]
