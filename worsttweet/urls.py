# worsttweet URLs

from django.conf.urls import include, url
from worsttweet import views
from worsttweet import api_urls 

urlpatterns = [
	url(r'^$', views.home_page, name='home'),
	# api
	url(r'^api/', include(api_urls)),
	# UI
	url(r'new/$', views.new_search, name='new_search'),
	url(r'search/$', views.home_page, name='home'),
	url(r'search/([^/]+)/$', views.search_result, name='search_result'),
	url(r'addfav/$',  views.add_favorite, name='add_favorite'),
	url(r'fav/$', views.view_random, name='view_random'),
	url(r'fav/(up|down)vote/$', views.vote_random, name='vote_random'),
	url(r'top/$', views.view_top, name='view_top'),
	url(r'view/(\d+)/$', views.view_by_id, name='view_by_id'),
]