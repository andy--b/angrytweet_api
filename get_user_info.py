import tweepy
from tweepy import OAuthHandler
from secret_keys import *

def get_user_info(user_id):
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	return api.get_user(user_id)
	
def get_multi_user_info(ids):
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	return api.lookup_users(user_ids=ids)