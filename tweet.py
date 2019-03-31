#Graham Wood
#This file contains most of the functions for tweeting
#tweets, though it can only really be used as an extention of main

#Not sure if this is needed, considering these functions will only
#be called from main, but here it is anyway
import tweepy
import authenticator

api = authenticator.authenticate()

#takes in a string and tweets it immediately
def tweetInput (string):
	api.update_status(string)

#takes in a string and a number of seconds, will wait that long and then tweet
def timedTweet (string, seconds):
	sleep(seconds)
	tweetInput(string)

