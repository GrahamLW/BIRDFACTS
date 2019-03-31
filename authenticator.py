#Graham Wood

#These two imports let us use tweepy's authentication functions
#in combination with out keys.json file
import tweepy
import json


#returns an api objhect, which is used in conjunction with other functions
def authenticate ():
	with open('keys.json', 'r') as f:
   		keys = json.loads(f.read())['twitter']
	key = keys['key']
	secret = keys['secret']
	accessToken = keys['accessToken']
	accessTokenSecret = keys['accessTokenSecret']
	auth = tweepy.OAuthHandler(key, secret)
	auth.set_access_token(accessToken, accessTokenSecret)
	api = tweepy.API(auth)
	return api
