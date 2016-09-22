import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import auth

class MyListener(StreamListener):	 
	def on_data(self, data):
		try:
			with open('python.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print('Error on_data: %s' % str(e))
		return True
 
	def on_error(self, status):
		print(status)
		return True

def getStream(api, auth) :
	keyword = raw_input('Indicate keyword you want to look at : ')
	if '#' in keyword :
		hashtag = keyword
	else :
		hashtag = '#' + keyword
	twitter_stream = Stream(auth, MyListener())
	twitter_stream.filter(track=[hashtag])

def getStatuses(api) :
	for status in tweepy.Cursor(api.home_timeline).items(10):
		# Process a single status
		print(status.text) 
		print('')
    
