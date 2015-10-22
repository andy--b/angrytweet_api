from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from find_extreme_tweets import extreme_tweets
from get_user_info import get_user_info, get_multi_user_info
import re
from worsttweet.models import FavoriteWorst

def home_page(request):
	return render(request, 'home.html')
	
def new_search(request):
	search_term = request.GET['search_text']
	formatted_url = re.sub(r'\W', '', search_term.replace(' ', '_'))
	return redirect('/mean/search/%s/' % (formatted_url,))
	
def search_result(request, formatted_url):
	search_term = formatted_url.replace('_', ' ')
	tweet = extreme_tweets(search_term)
	if type(tweet) == None:
		return redirect('/insufficient/')
	to_render = {'search_term': search_term,
				 'tweet': tweet}
	return render(request, 
				  'results.html', 
				  to_render,)

def insufficient(request):
	return render(request, 'insufficient.html')
	
def add_favorite(request):
	term = request.POST["search_term"].replace(' ','_')
	tw_id = request.POST["tweet_id"]
	tw_text = request.POST["tweet_text"]
	tw_user_id = request.POST["twitter_user_id"]
	try:
		existing_tweet = FavoriteWorst.objects.get(tweet_id = tw_id)
		if existing_tweet.upvote_count < 5:
			existing_tweet.upvote_count += 1
			existing_tweet.save()
	except FavoriteWorst.DoesNotExist:
		FavoriteWorst.objects.create(
			search_term=term.replace('_',' '),
			tweet_id=tw_id, 
			tweet_text=tw_text,
			twitter_user_id=tw_user_id,
			)
	return redirect('addfav/%s/%s' % (tw_id, term,),)
	
def view_favorite(request, id, term):
	tweet = FavoriteWorst.objects.get(tweet_id=id)
	user_info = get_user_info(tweet.twitter_user_id)
	to_render = {'profile_pic': user_info.profile_image_url,
				'tweet_text': tweet.tweet_text,
				'upvote_count': tweet.upvote_count,
				'twitter_handle': user_info.screen_name,
				'search_term': term}
	return render(request,
				  'view_favorite.html',
				  to_render)
				  
def view_random(request):
	random_tweet = FavoriteWorst.objects.random()
	user_info = get_user_info(random_tweet.twitter_user_id)
	return render(request,
				  'random_favorite.html',
				  {'random_tweet': random_tweet,
				   'user_info': user_info})
				   
def view_top(request):
	top_tweets=FavoriteWorst.objects.order_by('-upvote_count')[:10]
	top_user_ids = [status.twitter_user_id for status in top_tweets]
	users = get_multi_user_info(top_user_ids)
	list = zip(top_tweets, users)
	return render(request,
				  'top_tweets.html',
				  {'top_tweets': list})
				  