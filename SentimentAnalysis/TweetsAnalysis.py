import tweepy
from textblob import TextBlob 

# twitter authentication process
consumer_key = "CQjEBVbqI2XCvy4Pc4K3IlcRz"
consumer_secret = "3BejfdDn61I5oBY5fUewfB1Ji5tbavNHdukO8pGbJTTWmGstWD"

access_token = "982714904-ci2WkrNQ65M36wIWl27zzykSYXnKujoSGDuYkUiR"
access_token_secret = "MYdOxaailZYOWQv3LQybu7DEv4Zn82BWPTF9npb3gWze7"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#fetching tweets from twitter for a particular topic e.g Manchester United

fetched_tweets = api.search('Manchester United')

for tweets in fetched_tweets:
	print(tweets.text)
	analysis = TextBlob(tweets.text)
	print(analysis.sentiment)
	print("-----------")
