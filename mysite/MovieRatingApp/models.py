from __future__ import unicode_literals
from django.db import models


class Tweet(models.Model):         									
# name of the table.

    username = models.CharField(max_length = 100)                   
    text = models.TextField()
    date = models.DateTimeField()
    # names of the columns.

    def __unicode__(self):											
    	return self.username
		# To display the username as the identifier. Else it will show 'TweetObject' in database.
