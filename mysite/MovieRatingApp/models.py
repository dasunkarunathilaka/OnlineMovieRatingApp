from __future__ import unicode_literals
from django.db import models


class Tweet(models.Model):         									
# name of the table - to save Tweets.

    username = models.CharField(max_length = 100)                   
    text = models.TextField()
    date = models.DateTimeField()
    sentiment = models.CharField(max_length = 3, null = True)	# pos or neg
    # names of the columns.

    def __unicode__(self):											
    	return self.username
		# To display the username as the identifier. Else it will show 'TweetObject' in database.
