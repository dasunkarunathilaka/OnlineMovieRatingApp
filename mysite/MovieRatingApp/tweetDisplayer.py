from . import dbConnector

def displayTweets():
	connectorObj = dbConnector.dbConnector()
	retrieved_tweets = connectorObj.retrieveTweets()
	sample_tweets = []

	# Adding two tweets as sample tweets.
	sample_tweets.append(retrieved_tweets[2])
	sample_tweets.append(retrieved_tweets[15])

	tweets = []
	for r in sample_tweets:
		tweets.append((r.text, r.username))

	return tweets
