# worsttweet URLs

from django.conf.urls import include, url
from worsttweet import views

urlpatterns = [
	url(r'^$', views.home_page, name='home'),
	url(r'new/$', views.new_search, name='new_search'),
	url(r'search/$', views.home_page, name='home'),
	url(r'search/([^/]+)/$', views.search_result, name='search_result'),
	url(r'addfav$',  views.add_favorite, name='add_favorite'),
	url(r'viewfav$', views.view_random, name='view_random'),
	url(r'viewfav/(up|down)vote$', views.vote_random, name='vote_random'),
	url(r'top$', views.view_top, name='view_top'),
]