#Graham L Wood
#Last Edited 12/2/19
import main
import time

#Automated Testing File
#Rudimentary Check to see if it actually is connected to the internet
print("###########USER CHECK###########")
user = main.api.me()
print(user.name)
assert user.name == "ConservationGo1"
print("######USER CHECK COMPLETE#######")

#A small scale test, should probably be done at the end of the file
#or commented out when not wanted

print("######TEST TWEET 24 HOURS#######")
def testTweetsForDay():
	base = "Automated Test Tweet "
	i = 1
	while i != 25:
		main.tweetInput(base + str(i))
		i = i + 1
		sleep (3600)

twestTweetsForDay()		
print("######TEST TWEET COMPLETE#######")


