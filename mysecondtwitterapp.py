import tweepy

#keys for Vdana101's twitter app
consumer_key = "zoZcOVp8JVOWj79E9AkY1jAlu"
consumer_secret = "3JCuAp9OGD7HMWAPYvTaIdoKsi8eJTVtoUXpWtQ0rdDFWm0Tlv"
access_token = "2515623180-awMeJvHn8yHzSc0CWSqZYp9SL3cuiGdApsgk5mM"
access_token_secret = "NR0oLruLOz9gqWCgVlIDP1RytVKAeZ9ipmNHC3yhUURcB"

api = None
auth = None

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

class StdOutListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        print(status.text)
 
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

def tweet():
	tweet = raw_input("Tweet something friend: ")
	api.update_status(tweet)

def print_tweets():
	my_tweets = api.user_timeline()
	for tweet in my_tweets:
		print tweet.text

myStreamListener = StdOutListener()
Stream = tweepy.Stream(auth, myStreamListener)
Stream.filter(track=['Tinder'])


# print user.screen_name
# print user.followers_count
# for friend in user.friends():
# 	print friend.screen_name

# iterations = input("How many tweets would you like to write " )
# while iterations > 0:
# 	tweet()
# 	iterations = iterations - 1

# print_tweets()