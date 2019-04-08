Senior Thesis For Graham Wood, Hanover College '19

This program is pretty simple to run, but a user will need a few things on their computer before they can run the program.

Before anything else, the user must be running Python3. You can download the latest version at https://www.python.org/downloads/

Firstly, the user will need a twitter account. These can be created at https://twitter.com/ 

Once that is complete the user must make their account a developer account. After they create their account they can do that here: https://developer.twitter.com/en/apps

The user will need to take the secret, key, accessToken, and accessTokenSecret for their unique account and put it into a file in the folder called "keys.json" The structure should look like this:

{
	"twitter": {
	"key" : "Your Key",
	"secret" : "Your Secret",

	"accessToken" : "Your accessToken",
	"accessTokenSecret" : "Your Token Secret"
	}
}

In order to run the program you will need to download the tweepy library. Tweepy gives the program a variety of useful functions that allow us to make the program work. Tweepy can be downloaded at https://github.com/tweepy/tweepy

The user will need the BeautifulSoup3 Library as well. Beautiful Soup makes web scraping possible for our program. You can download that here: https://www.crummy.com/software/BeautifulSoup/

Once these have been done the user is ready to go. All they have to do is run the main function in main.py. The program will update the dictionary with our web scraped data, query the user for how long the wait should be between tweets, and then begin tweeting.
