from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jsonData/$', views.getJSONData, name='getJSONData'),
    url(r'^jsonLiveData/$', views.getLiveJSONData, name='getLiveJSONData'),
	url(r'^sse/$', views.sse, name='sse'),
    url(r'^graph/$', views.getGraph, name='getGraph'),
    url(r'^$', views.userview, name='userview'),
    url(r'^userview/$', views.homeview, name='homeview'),
    url(r'^getUser2/$', views.storePickedStation, name='storePickedStation'),
    url(r'^userview2/$', views.userview2, name='userview2')
]
