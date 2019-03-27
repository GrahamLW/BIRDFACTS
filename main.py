#Graham L Wood
#Last Edited: 27/3/19

#Library that greatly increases speed of authorizing and making tweets
import tweepy

#Used to access keys.json, which is where we keep our
#passwords and secrets
import json

#???
import operator

#Mostly for the sleep function, which lets us
#put pauses between tweets
import time

#Importing the tweeting functions
import tweet

#Import the wikipedia access functions
import wikipedia

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

# def main ():
# 	while true:

