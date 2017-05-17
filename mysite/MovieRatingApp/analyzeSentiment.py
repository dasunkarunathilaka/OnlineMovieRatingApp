import pickledDataSet as s
import time
from . import dbConnector


def analyze():
	start_time = time.time()

	connectorObj = dbConnector.dbConnector()
	retrieved_tweets = connectorObj.retrieveTweets()

	for r in retrieved_tweets:

		analyzed_sentiment_confidence = s.sentiment(r.text)

		analyzed_sentiment = analyzed_sentiment_confidence[0]
		confidence = analyzed_sentiment_confidence[1]

		if (confidence >= 0.8):
			connectorObj.saveSentiment(r, analyzed_sentiment)

	print("--- %s seconds ---" % (time.time() - start_time))
