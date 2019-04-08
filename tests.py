#Graham L Wood
#Last Edited 12/2/19
import main
import tweet
import time
import authenticator
import wikipedia


#Automated Testing File
#Rudimentary Check to see if it actually is connected to the internet
print("######Authenitcation Check######")
api = authenticator.authenticate()
print("##Authenitcation Check Complete#")

print("###########USER CHECK###########")
user = api.me()
print(user.name)
assert user.name == "Conservation Golem"
print("######USER CHECK COMPLETE#######")

print("#########Dataset Check##########")
dictionary = wikipedia.updateDictionary()
x= 0
while x < 100:
	species, status = main.selector(dictionary)
	assert species, status in dictionary
	x = x + 1
print("#####Dataset Check Complete#####")



#A small scale test, should probably be done at the end of the file
#or commented out when not wanted
# print("######TEST TWEET 24 HOURS#######")
# def testTweetsForDay():
# 	base = "Automated Test Tweet "
# 	i = 2
# 	while i != 26:
# 		tweet.tweetInput(base + str(i))
# 		i = i + 1
# 		time.sleep (3600)

# testTweetsForDay()		
# print("######TEST TWEET COMPLETE#######")


