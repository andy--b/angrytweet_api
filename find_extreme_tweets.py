import re
import tweepy
from random import shuffle
from tweepy import OAuthHandler
from secret_keys import *
							
def run_query(search_term, extreme_words_string, api):
	query = search_term + ' -RT AND ' + extreme_words_string
	results = [
		status for status in tweepy.Cursor(api.search, q=query).items(50)]
	return results 
				
def find_most_extreme(data, extreme_words):
	extreme_tweets = [0] * 10
	query = bytes("|".join(extreme_words), 'utf-8')
	min_addr_val = [0, 0]
	for i, t in enumerate(data):
		extreme_count = len(re.findall(query, t.text.encode('utf-8')))
		if extreme_count > min_addr_val[1]:
			extreme_tweets[min_addr_val[0]] = extreme_count
			extreme_tweets[min_addr_val[0] + 5] = t.id
			min_addr_val[0] = extreme_tweets.index(min(extreme_tweets[0:5]))
			min_addr_val[1] = min(extreme_tweets[0:5])
	return extreme_tweets[5:]

def extreme_tweets(search_term):	
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)

	key_extreme_word = 'fuck'
	extreme_words = ['shit', 'piss', 'crap', 'damn', 'idiot', 'stupid', 'fag',
					'pussy', 'dick', 'jerk', 'cunt', 'cock', 'dirtbag', 'worthless',
					'waste', 'dumb', 'retarded', 'fuk', 'fuc', 'sht', 'dam']
					
	extreme_words_string = ""
	for i in extreme_words[:-1]:
		extreme_words_string += i + ' OR '
	extreme_words_string += extreme_words[-1]
					
	# First, we try a query that REQUIRES the key_extreme_word
	# and at least one other extreme_words. If we get less than 5
	# results from that query, we redo the search treating the 
	# key word as a regular extreme_words	
	data = run_query(search_term, 
					key_extreme_word + ' AND ' + extreme_words_string, api)

	# Redo search if less than 5 results
	if len(data) < 5:
		data = run_query(search_term, 
						key_extreme_word + ' OR ' + extreme_words_string, api)

	extreme_ids = find_most_extreme(data, 
									extreme_words + [key_extreme_word])
	selected_tweets = []
	for tweet in data:
		if tweet.id in extreme_ids:
			selected_tweets.append({
				'user_screen_name': tweet.user.screen_name,
				'user_profile_image_url': tweet.user.profile_image_url,
				'text': tweet.text,
				'user_followers_count': tweet.user.followers_count,
				'id': tweet.id,
				'user_id': tweet.user.id,
				'user_name': tweet.user.name})
	shuffle(selected_tweets)
	return selected_tweets
