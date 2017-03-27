import tweepy
from tweepy import OAuthHandler
from . import dbConnector


class twitterConnector(object):

	ckey = 'BNPj5RN5YFrBkoy8FCSSUADXc'
	csecret = 'zeuNOocezOH1wRWujUBINT4CvKumEtpJW0ql2CQx1SqpNfwj6E'
	atoken = '2902474477-UxJR8N06sjNIXuaGlGk0IPsPtb2UYoWnhq3D4YL'
	asecret = 'TPti3ngvexZCcnzN27jPlx6fz7wc5f24aHJDoddJIf2KE'

	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	api = tweepy.API(auth)
	# These should be static variables, because they are same across all objects.


	def searchTwitter(self, name):
		
		connectorObj = dbConnector.dbConnector()
		# dbConnector class in dbConnector file.

		connectorObj.deleteAll()
		# delete previous search results from the database.

		for tweet in tweepy.Cursor(self.api.search,lang = 'en', q = name).items(200):        
		# 15-25 seconds for 200 tweets.
		# Tweet objects are returned by Tweepy module. No need to have a seperate Tweet class.
		# To access static variables inside a method, 'self.api'. Can also use 'twitterConnector.api'
			
			if 'RT @' not in tweet.text:                                        		
			# to avoid retweets and thereby duplicates        
			
				username = tweet.user.name
				tweetContent = tweet.text
				publishedDate = tweet.created_at

				connectorObj.saveTweet(username, tweetContent, publishedDate)
				