#Graham Wood
#This file contains most of the functions for tweeting
#tweets, though it can only really be used as an extention of main

#Not sure if this is needed, considering these functions will only
#be called from main, but here it is anyway
import tweepy
import main

#takes in a string and tweets it immediately
def tweetInput (string):
	main.api.update_status(string)

#takes in a string and tweets it after 3600
#seconds or one hour
def oneHourTweet (string):
	sleep(3600)
	tweetInput(string)

