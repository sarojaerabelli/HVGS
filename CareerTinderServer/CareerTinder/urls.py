from django.conf.urls import url

from . import views, tinder, resume_upload, resume_retrieval, take_picture


urlpatterns = [
    url(r'^review/(?P<idx>[0-9]+)/', tinder.review_page, name='review_page'),
    url(r'^review', tinder.review_page, name='review_page'),
    url(r'^browse', tinder.browse, name='browse'),
    url(r'^upload', resume_upload.upload_resume, name='upload_resume'),
    url(r'^retrieve', resume_retrieval.index, name='retrieve'),
    url(r'^picture', take_picture.index, name='picture'),
    url(r'^home', views.index, name='home'),
    url(r'^$', views.index, name='index')
]
