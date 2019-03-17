#Graham L Wood
#Last Edited: 12/2/19
import tweepy
import json
import operator

#This line imports a key and secret from a
#file elsewhere on the computer
#in order to use this program you will have
#to have your own saved under a keys.json
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['twitter']

#key and secret allow for access to account
#both are 'consumer' grade
#meaning I can only use them for certain things
key = keys['key']
secret = keys['secret']

#token and token secret are for tweepy
#tweepy needs to be authorized before it can act
accessToken = keys['accessToken']
accessTokenSecret = keys['accessTokenSecret']

#This line allows me to access my
#Twitter account
auth = tweepy.OAuthHandler(key, secret)

#This line enables tweepy to
#also access my twitter account
auth.set_access_token(accessToken, accessTokenSecret)

#This line gives over the metaphorical
#keys to tweepy
api = tweepy.API(auth)

#takes in a string and tweets it immediately
def tweetInput (string):
	api.update_status(string)

#takes in a string and tweets it after 3600
#seconds or one hour
def oneHourTweet (string):
	sleep(3600)
	tweetInput(string)

def main ():
	while:
		##Sourcing information from Wikipedia will go here
		oneHourTweet(tweet)

