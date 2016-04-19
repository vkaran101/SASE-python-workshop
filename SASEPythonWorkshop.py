#!/usr/bin/python

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import sys


class twitter_app:
	def __init__(self):
		consumer_key = raw_input("enter consumer key: ")
		consumer_secret = raw_input("enter consumer secret: ")
		access_token = raw_input("enter access token: ")
		access_token_secret = raw_input("enter secret access token: ")
		self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		self.auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(self.auth)
		self.user = self.api.get_user('twitter')

	def tweet(self):
		var = raw_input("Tweet something! ")
		self.api.update_status(var)


	def get_user_info(self):
		print self.user.screen_name
		print self.user.followers_count

	def get_my_tweets():
		my_tweets = api.user_timeline()
		for tweet in my_tweets:
			print tweet.text


def main():
	twitter_user = twitter_app()
	while 1:
		twitter_user.tweet()


if __name__ == "__main__":
	main() 