#Graham Wood

import requests
from bs4 import BeautifulSoup

#List of phrases we do not want in our final dictionary
exclusionList = ["edit", "Category", "List", "Conservation", "species", "subspecies", "variety",
					"Binomial", "Trinomial", "/wiki/Fish", "/wiki/Mollusca", "/wiki/Animalia", "/wiki/Aves",
					"/wiki/Reptilia", "/wiki/Fish", "/wiki/Mamallia", "/wiki/Amphibia", "/wiki/Arthropoda"]


baseSite = "http://en.wikipedia.org"
extinctWildPage = "/wiki/List_of_extinct_in_the_wild_animals"
criticalEndangerPage = "/wiki/IUCN_Red_List_critically_endangered_species_(Animalia)"
normalEndangerPage = "/wiki/IUCN_Red_List_endangered_species_(Animalia)"
vulnerablePage = "/wiki/IUCN_Red_List_vulnerable_species_(Animalia)"
nearThreatenedPage = "/wiki/IUCN_Red_List_near_threatened_species_(Animalia)"

#Takes a string for the text of the webpage and returns and html response
def updateResponse(linkExtension):
	return requests.get(baseSite + linkExtension)

#Takes in a html response and returns the response parsed with beatuiful soup
def updateBsObj(htmlResponse):
	bsObj = BeautifulSoup(htmlResponse.content, "html.parser")
	bsObj = bsObj.find(id = 'bodyContent')
	return bsObj


#takes in a Beautiful Soup Object and the value all dictionary keys should have
#and returns a dictionary with the correct text and the correct values
def bsObjToDict(bsObj):
	#make a lis tof our keys
	keys = [
	  tag.get('title')
	  for tag in bsObj.find_all('a')
	]
	#make a list of our values
	values = [
	  tag.get('href')
	  for tag in bsObj.find_all('a')
	]
	i = 0
	while i < len(keys):
		deleted = False
		for exclusion in exclusionList:
			if exclusion in values[i]\
			 or keys[i] == None:
				keys.pop(i)
				values.pop(i)
				deleted = True
				break
		if deleted == False:
			i = i + 1
	return dict(zip(keys, values))

#updates all the pages into a dictionary, returns that dictionary
def updateDictionary():
	extinctWildResponse = updateResponse(extinctWildPage)
	criticalEndangerResponse = updateResponse(criticalEndangerPage)
	normalEndangerResponse = updateResponse(normalEndangerPage)
	vulnerableResponse = updateResponse(vulnerablePage)
	nearThreatenedResponse = updateResponse(nearThreatenedPage)

	extinctWildBSOBJ = updateBsObj(extinctWildResponse)
	criticalEndangerBSOBJ = updateBsObj(criticalEndangerResponse)
	normalEndangerBSOBJ = updateBsObj(normalEndangerResponse)
	vulnerableBSOBJ = updateBsObj(vulnerableResponse)
	nearThreatenedBSOBJ = updateBsObj(nearThreatenedResponse)

	extinctWildDict = bsObjToDict(extinctWildBSOBJ)
	critcalEndangerDict = bsObjToDict(criticalEndangerBSOBJ)
	normalEndangerDict = bsObjToDict(normalEndangerBSOBJ)
	vulnerableDict = bsObjToDict(vulnerableBSOBJ)
	nearThreatenedDict = bsObjToDict(nearThreatenedBSOBJ)

	extinctWildDict = {x: "Extinct in Wild" for x in extinctWildDict}
	critcalEndangerDict = {x: "Critcalally Endangered" for x in critcalEndangerDict}
	normalEndangerDict = {x: "Endangered" for x in normalEndangerDict}
	vulnerableDict = {x: "Vulnerable" for x in vulnerableDict}
	nearThreatenedDict = {x: "Near Threatened"  for x in nearThreatenedDict}

	finalDictionary = extinctWildDict
	finalDictionary.update(critcalEndangerDict)
	finalDictionary.update(normalEndangerDict)
	finalDictionary.update(vulnerableDict)
	finalDictionary.update(nearThreatenedDict)

	return finalDictionary

updateDictionary()





