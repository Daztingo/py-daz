import tweepy
from tweepy import OAuthHandler
import config
 
 
def initApi(authentificationToken) :
	api = tweepy.API(authentificationToken)
	return api

def initAuth() :
	authentificationToken = OAuthHandler(config.consumer_key, config.consumer_secret)
	authentificationToken.set_access_token(config.access_token, config.access_secret)
	return authentificationToken
