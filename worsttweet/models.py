from django.db import models

class FavoriteWorst(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	twitter_id = models.CharField(max_length=50, blank=True)
	upvote_count = models.IntegerField()
	downvote_count = models.IntegerField()
