# worsttweet URLs

from django.conf.urls import include, url
from worsttweet import views

urlpatterns = [
	url(r'^new$', views.new_search, name='new_list'),
	url(r'search/(\w+)/$', views.search_result, name='search_result'),
]