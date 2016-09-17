from django.conf.urls import url

from . import views, tinder

urlpatterns = [
	url(r'^review', tinder.index, name='index'),
    url(r'^$', views.index, name='index')
]
