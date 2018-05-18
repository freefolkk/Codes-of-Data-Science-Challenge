import tweepy
from textblob import TextBlob 

# twitter authentication process
# Use your own authentication  
consumer_key = "CQjEBVbqI2XCvy432YFDEJFJJHKK3IlcRzc"
consumer_secret = "3BejfdDn61I5oBAVEEEY5fUewfB1Ji5cascStbavNHdukO8pGbJTTWmGstWD"

access_token = "982714904-ci2WkrNAVAQ65M36wIWl27FQEGEzzykSYXnKujoSGDuYkUiR"
access_token_secret = "MYdOxaailZYOWVAAVQv3LQybu7DWEQGQTEGWTAEv4Zn82BWPTF9npb3gWze7"

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
