#Graham L Wood
#Last Edited: 27/3/19


#Mostly for the sleep function, which lets us
#put pauses between tweets
import time
#Importing the tweeting functions
import tweet
#Import the wikipedia access functions
import wikipedia
#Import random library
import random

def selector(dictionary):
	return random.choice(list(dictionary.items()))

def shortSeries():
	dictionary = wikipedia.updateDictionary()
	secondsString = input("Select time in seconds between tweets, I recommend 3600 ")
	seconds = int(secondsString)
	for i in 20:
		species, status = selector(dictionary)
		tweet = species + " is currently considered to be " + status
		timedTweet(tweets, seconds)

def main ():
	dictionary = wikipedia.updateDictionary()
	secondsString = input("Select time in seconds between tweets, I recommend 3600 ")
	seconds = int(secondsString)
	while True:
		species, status = selector(dictionary)
		tweet = species + " is currently considered to be " + status
		timedTweet(tweets, seconds)

