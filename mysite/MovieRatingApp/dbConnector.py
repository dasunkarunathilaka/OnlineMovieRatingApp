from models import Tweet

class dbConnector(object):
	
	def saveTweet(self, username, tweetContent, publishedDate):
		tweetObject = Tweet(username = username, text = tweetContent, date = publishedDate)
		# Creates an object to be saved in the Tweet model in the database.

		tweetObject.save()


	def deleteAll(self):
		Tweet.objects.all().delete()
		# Deletes all the Tweets in the database. Applied before every search.
