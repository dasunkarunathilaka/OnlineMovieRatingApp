from models import Tweet

class dbConnector(object):
	
	def saveTweet(self, username, tweetContent, publishedDate):
		tweetObject = Tweet(username = username, text = tweetContent, date = publishedDate)
		# Creates an object to be saved in the Tweet model in the database.

		tweetObject.save()

	def saveSentiment(self, tweetObj, analyzedSentiment):
		tweetObj.sentiment = analyzedSentiment
		tweetObj.save()


	def deleteAll(self):
		Tweet.objects.all().delete()
		# Deletes all the Tweets in the database. Applied before every search.

	def retrieveTweets(self):
		retrieved_Tweets = Tweet.objects.all()
		return retrieved_Tweets

	def getSentimentCount(self, sentimentType):
		sentiment_count = Tweet.objects.filter(sentiment = sentimentType).count()
		return sentiment_count
		# Get the count of the tweets according to its sentiment - pos / neg



