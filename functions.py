#Graham Wood
#Last Edited: 10/1/19

import operator
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import json

#Pull key and secret from keys.json
#Required to access the account
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['twitter']

#Base, requirement for almost every json action
base = 'https://api.twitter.com/1.1/'

#Update, url for specifically creating updates
update = base + 'statuses/update.json'

def tweeter(status){
	
}