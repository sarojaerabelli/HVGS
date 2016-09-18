from django.conf.urls import url, include
from material.frontend import urls as frontend_urls

from . import views, tinder, resume_upload, resume_retrieval, take_picture


urlpatterns = [
    url(r'^review/(?P<idx>[0-9]+)/', tinder.review_page, name='review_page'),
    url(r'^review', tinder.review_page, name='review_page'),
    url(r'^thumbnails/(?P<hiree_id>[0-9]+)/', tinder.hiree_thumbnail_page, name='thumbnails'),
    url(r'^browse', tinder.browse, name='browse'),
    url(r'^upload', resume_upload.upload_resume, name='upload_resume'),
    url(r'^retrieve', resume_retrieval.index, name='retrieve'),
    url(r'^picture', take_picture.index, name='picture'),
    url(r'^home', views.index, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^$', views.index, name='index')
]