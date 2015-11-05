# Python standard packages
import re

# Django and models
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from worsttweet.models import FavoriteWorst

# User modules
from nice_terms import nice_term
from find_extreme_tweets import extreme_tweets
from search_examples import search_examples

def insufficient(request):
# Return this page if search term doesn't generate any results
	return render(request, 'insufficient.html')

def home_page(request):
# Landing
	s1, s2 = search_examples(2)
	to_render = {'s1': s1,
				 's2': s2}
	return render(request, 'home.html', to_render)

def new_search(request):
# When user submits search, they are sent to this view.
# All relevant data is stored as session data	
	search_term = request.GET['search_text']
	formatted_url = re.sub(r'\W', '', search_term.replace(' ', '_'))	
	request.session['_tweets'] = extreme_tweets(formatted_url.replace('_', ' '))
	request.session['_tweet_index'] = 0
	request.session['_search_term'] = formatted_url.replace('_', ' ')
	request.session['_favorite_indices'] = []
	request.session['_newly_favorited'] = False
	return redirect('/mean/search/%s/' % (formatted_url,))

	
def search_result(request, formatted_url):
# Check if the user has already searched for this term (aka if they are
# refreshing page or using "prev/next" buttons.
# If they search term doesn't match the URL, a new search is performed
# Based on the URL.
	search_term = formatted_url.replace('_', ' ')
	try:
		if search_term != request.session['_search_term']:
			request.session['_tweets'] = extreme_tweets(search_term)
			request.session['_tweet_index'] = 0
			request.session['_search_term'] = search_term
			request.session['_is_favorite'] = False
			request.session['_favorite_indices'] = []
			request.session['_newly_favorited'] = False
			
	except:
		request.session['_tweets'] = extreme_tweets(search_term)
		request.session['_tweet_index'] = 0
		request.session['_search_term'] = search_term
		request.session['_is_favorite'] = False
		request.session['_favorite_indices'] = []
		request.session['_newly_favorited'] = False
	tweets = request.session['_tweets']	
	if len(tweets) == 0:
		return redirect('/insufficient/')
	try:
	# Change page index based on whether user hit "next/prev" button
		if request.GET["next_prev"] == 'next' and \
		request.session['_tweet_index'] + 1 < len(tweets):
			request.session['_tweet_index'] += 1
		elif request.GET["next_prev"] == 'prev' and \
		request.session['_tweet_index'] > 0:
			request.session['_tweet_index'] -= 1
	except:
		pass
	tweet_index = request.session['_tweet_index']	
	try:
		favorite_count = FavoriteWorst.objects.get(
			tweet_id=tweets[tweet_index]["id"]).upvote_count
	except:
		favorite_count = 0
	if tweet_index in request.session['_favorite_indices']:
		favorite_button = False
	else:
		favorite_button = True	
	# Rules for displaying "next/prev" buttons
	if request.session['_tweet_index'] + 1 < len(tweets):
		next_button = True
	else:
		next_button = False
	if request.session['_tweet_index'] > 0:
		prev_button = True
	else:
		prev_button = False
	to_render = {'search_term': search_term,
				 'tweet': tweets[tweet_index],
				 'next_button_visible': next_button,
				 'prev_button_visible': prev_button,
				 'nice_term': nice_term()[0],
				 'favorite_button_visible': favorite_button,
				 'upvote_count': favorite_count,
				 'newly_favorited': request.session['_newly_favorited']}
	request.session['_newly_favorited'] = False
	return render(request, 
				  'search_results.html', 
				  to_render,)

def add_favorite(request):
# Occurs when user selects "Add to favorites" button
	term = request.POST["search_term"].replace(' ','_')
	tw_id = request.POST["tweet_id"]
	tw_text = request.POST["tweet_text"]
	tw_user_id = request.POST["twitter_user_id"]
	tw_screen_name = request.POST["twitter_screen_name"]
	tw_profile_pic_url = request.POST['user_profile_pic_url']
	tw_user_followers = request.POST['user_followers_count']
	tw_user_name = request.POST['twitter_user_name']
	request.session['_newly_favorited'] = True
	try:
	# If someone else has already favorited this, don't add to DB,
	# just increment score. Limit on this is 5 to prevent "gaming" the system
		existing_tweet = FavoriteWorst.objects.get(tweet_id = tw_id)
		if existing_tweet.upvote_count < 5:
			existing_tweet.upvote_count += 1
			existing_tweet.save()
	except FavoriteWorst.DoesNotExist:
	# Add to db if new
		FavoriteWorst.objects.create(
			search_term=term.replace('_',' '),
			tweet_id=tw_id, 
			tweet_text=tw_text,
			twitter_user_id=tw_user_id,
			twitter_screen_name = tw_screen_name,
			user_followers_count = tw_user_followers,
			user_profile_pic_url = tw_profile_pic_url,
			twitter_user_name = tw_user_name,
			)
	request.session['_favorite_indices'] += [request.session['_tweet_index']]
	return redirect('/mean/search/%s/' % term)
				  
def view_random(request):
# Displays a random tweet from DB. Gets user's current profile pic and
# post's current upvote count.
	try:
		new_upvote_count = request.session['_upvote_count']
		del request.session['_upvote_count']
		visible = True
	except KeyError:
		new_upvote_count = ''
		visible = False
	random_tweet = FavoriteWorst.objects.random(1)[0]
	return render(request,
				  'random_favorite.html',
				  {'random_tweet': random_tweet,
				   'new_upvote_count': new_upvote_count,
				   'visible': visible,
				   'nice_term': nice_term()[0]})
				   
def vote_random(request, vote):
# If user votes, adds to upvote count and displays new tweet.
# On view_random view, user will see the vote total of the previous
# Tweet they voted on.
	tw_id = request.POST["tweet_id"]
	existing_tweet = FavoriteWorst.objects.get(tweet_id = tw_id)
	if vote == "up":
		existing_tweet.upvote_count += 1
	elif vote == "down":
		existing_tweet.upvote_count -= 1
	request.session['_upvote_count'] = existing_tweet.upvote_count
	if existing_tweet.upvote_count <= -2:
		existing_tweet.delete()
	else:
		existing_tweet.save()
	return HttpResponseRedirect("/mean/fav/")
				   
def view_top(request):
# Displays top 10 tweets from DB
	top_tweets=FavoriteWorst.objects.order_by('-upvote_count')[:10]
	nt = nice_term(10)
	to_render = zip(top_tweets, nt)
	return render(request,
				  'top_tweets.html',
				  {'top_tweets': to_render})
				  
def view_by_id(request, tw_id):
# Displays tweet by id number, serves as a permalink to tweets
	tweet = FavoriteWorst.objects.get(tweet_id = tw_id)
	return render(request,
				  'view_by_id.html',
				  {'tweet': tweet,
				  'nice_term': nice_term()[0]})
		  
def api_random(request, sample_size=1):
# API call to get random tweets (up to 10)
	# Limit sample size to 10
	adj_sample_size = min([10, int(sample_size)])
	random_tweets = serializers.serialize("json",
		FavoriteWorst.objects.random(adj_sample_size))
	return HttpResponse(random_tweets)
	
def api_top(request):
# API call to get top 10 tweets all-time
	top_tweets = serializers.serialize("json",
		FavoriteWorst.objects.order_by('-upvote_count')[:10])
	return HttpResponse(top_tweets)
				  