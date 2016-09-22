import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import auth
import string
import helper

class MyListener(StreamListener):	 
	#Customer listener for stream data
	def __init__(self, data_dir, query):
		#Based on https://gist.github.com/bonzanini/af0463b927433c73784d
		query_fname = helper.format_filename(query)
		#Handle case where  user doesn't want to filter
		if query_fname == '' :
			query_fname = 'all'
		self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)
		print 'Stream available at : ' + self.outfile
		
	def on_data(self, data):
		try:
			with open(self.outfile, 'a') as f:
				f.write(data)
				print(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
			time.sleep(5)
		return True	

	def on_error(self, status):
		print(status)
		return True

def getStream(api, auth) :
	#Fetch stream of statuses based on an hashtag given later by the user
	keyword = raw_input('Indicate keyword you want to look at : ')
	#We get keyword here, due to potential evolutions where we would be allowed to indicate multiple keywords	
	if '#' in keyword :
		hashtag = keyword
	else :
		hashtag = '#' + keyword
	twitter_stream = Stream(auth, MyListener('Streams', keyword))
	twitter_stream.filter(track=hashtag)


		
		

    
