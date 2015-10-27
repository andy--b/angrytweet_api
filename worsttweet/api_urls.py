# worsttweet URLs

from django.conf.urls import include, url
from worsttweet import views

urlpatterns = [
	url(r'random/$', views.api_random, name="api_random"),
	url(r'random/(\d+)/$', views.api_random, name="api_random"),
	url(r'top/$', views.api_top, name="api_top"),
]