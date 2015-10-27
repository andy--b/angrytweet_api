from django.db import models
from django.db.models.aggregates import Count
from random import randint, sample

# Returns a specified number of random tweets
class TweetRandomizer(models.Manager):
	def random(self, sample_size):
		count = self.aggregate(count=Count('id'))['count']
		random_index = sample(range(0, count), sample_size)
		tweet_list = []
		for i in random_index:
			tweet_list.append(self.all()[i])
		return tweet_list
			
		
class FavoriteWorst(models.Model):
	objects = TweetRandomizer()
	created = models.DateTimeField(auto_now_add=True)
	search_term = models.CharField(max_length=50, blank=True)
	tweet_id = models.CharField(max_length=50, blank=True)
	tweet_text = models.CharField(max_length=300)
	twitter_user_id = models.CharField(max_length=50, blank=True)
	twitter_screen_name = models.CharField(max_length=50, blank=True)
	upvote_count = models.IntegerField(default=1)
	user_followers_count = models.IntegerField(default=1)
	user_profile_pic_url = models.CharField(max_length=100, default="")
