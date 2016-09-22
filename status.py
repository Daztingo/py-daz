import tweepy
import re

def getStatuses(api) :
	#Fetch latest statuses for current user
	for status in tweepy.Cursor(api.home_timeline).items(10):
		# Process a single status
		print(status.text) 
		print('')

def getStatusesForId(user, api) :
	for status in api.user_timeline(user):
		# Process a single status
		if re.match(r'^RT', status.text) :
			# It's a RT, you have to select right field to avoid truncation
			print(status.retweeted_status.text) 
			print('')
		else :
			# Standard tweet
			print(status.text) 
			print('')
		
