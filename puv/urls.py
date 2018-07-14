from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^jsonData/$', views.getJSONData, name='getJSONData'),
    url(r'^jsonLiveData/$', views.getLiveJSONData, name='getLiveJSONData'),
	url(r'^sse/$', views.sse, name='sse'),
    url(r'^graph/$', views.getGraph, name='getGraph')
]
