import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'BNPj5RN5YFrBkoy8FCSSUADXc'
csecret = 'zeuNOocezOH1wRWujUBINT4CvKumEtpJW0ql2CQx1SqpNfwj6E'
atoken = '2902474477-UxJR8N06sjNIXuaGlGk0IPsPtb2UYoWnhq3D4YL'
asecret = 'TPti3ngvexZCcnzN27jPlx6fz7wc5f24aHJDoddJIf2KE'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,q="#titanic").items(200):         #15 seconds for 200 tweets
    if 'RT @' not in tweet.text:                                        # to avoid retweets and thereby duplicates
        print " * " + tweet.user.name + ' - ' + tweet.text
    
