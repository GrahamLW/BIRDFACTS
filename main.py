#Graham L Wood
#Last Edited: 12/2/19
import tweepy

#key and secret allow for access to account
#both are 'consumer' grade
#meaning I can only use them for certain things
key = 'YanDNcrWjSK2W2li61e3IDu2p'
secret = 'yuCkce4As21ccfJNFtbgsytc0F3X0FMnIX6QH9odFU4t76CsWY'

#token and token secret are for tweepy
#tweepy needs to be authorized before it can act
accessToken = '1094330695118438400-9MFa6XVEBpa6Iq1rymqAkJdtqrRTMK'
accessTokenSecret = 'Dd958RHPz1HadbWMTAcClB8ZJl4utkssonpfVwu905dic'

#This line allows me to access my
#Twitter account
auth = tweepy.OAuthHandler(key, secret)

#This line enables tweepy to
#also access my twitter account
auth.set_access_token(accessToken, accessTokenSecret)

#This line gives over the metaphorical
#keys to tweepy
api = tweepy.API(auth)

api.update_status("Test 1")
