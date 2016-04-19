#!/usr/bin/python

#Import the necessary methods from tweepy library
import tweepy


#Variables that contains the user credentials to access Twitter API 
consumer_key = "zoZcOVp8JVOWj79E9AkY1jAlu"
consumer_secret = "3JCuAp9OGD7HMWAPYvTaIdoKsi8eJTVtoUXpWtQ0rdDFWm0Tlv"
access_token = "2515623180-awMeJvHn8yHzSc0CWSqZYp9SL3cuiGdApsgk5mM"
access_token_secret = "NR0oLruLOz9gqWCgVlIDP1RytVKAeZ9ipmNHC3yhUURcB"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = None
user = None


api = tweepy.API(auth)
user = api.me()

def tweet():
	global api
	var = raw_input("Tweet something! ")
	api.update_status(var)


def get_user_info():
	print "Username: " + user.screen_name + "\n"
	print "Followers: " + str(user.followers_count)

dwef print_tweets():
	my_tweets = api.user_timeline()
	for tweet in my_tweets:
		print tweet.text + "\n"

# class StdOutListener(tweepy.StreamListener):
#     ''' Handles data received from the stream. '''
 
#     def on_status(self, status):
#         # Prints the text of the tweet
#         print(status.text)
 
 
#     def on_error(self, status_code):
#         print('Got an error with status code: ' + str(status_code))
#         return True # To continue listening
 
#     def on_timeout(self):
#         print('Timeout...')
#         return True # To continue listening

get_user_info()
iterations = input("How many thoughts do you want to tweet? ")
while iterations > 0:
	var = raw_input("Tweet something! ") 
	api.update_status(var)
	iterations = iterations - 1

print_tweets()

# myStreamListener = StdOutListener()
# Stream = tweepy.Stream(auth, myStreamListener)
# #Stream.filter(track=['python'])
# status = api.get_status()
# myStreamListener.on_status(status)

