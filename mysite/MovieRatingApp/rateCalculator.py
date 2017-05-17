from __future__ import division
from . import dbConnector


connectorObj = dbConnector.dbConnector()


def calculateRating():
	positive_count = connectorObj.getSentimentCount("pos")
	negative_count = connectorObj.getSentimentCount("neg") / 20
	# Negative tweets are too damn high.

	totalCount = positive_count + negative_count

	rating =  ((positive_count - negative_count)*5 / totalCount) + 5

	print "positive_count : " , positive_count
	print "negative_count : " , negative_count
	print "Total : " , totalCount

	print "Rating : " , rating

	rounded_value = round(rating, 1)

	return rounded_value