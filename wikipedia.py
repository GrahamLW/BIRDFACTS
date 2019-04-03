#Graham Wood

import requests
from bs4 import BeautifulSoup

#List of phrases we do not want in our final dictionary
exclusionList = ["edit", "Category", "List", "Conservation", "species", "subspecies", "variety",
					"Binomial", "Trinomial", "/wiki/Fish", "/wiki/Mollusca", "/wiki/Animalia", "/wiki/Aves",
					"/wiki/Reptilia", "/wiki/Fish", "/wiki/Mamallia", "/wiki/Amphibia", "/wiki/Arthropoda"]


baseSite = "http://en.wikipedia.org"
extinctWild = "/wiki/List_of_extinct_in_the_wild_animals"
criticalEndanger = "/wiki/IUCN_Red_List_critically_endangered_species_(Animalia)"
normalEndanger = "/wiki/IUCN_Red_List_endangered_species_(Animalia)"
vulnerable = "/wiki/IUCN_Red_List_vulnerable_species_(Animalia)"
nearThreatened = "/wiki/IUCN_Red_List_near_threatened_species_(Animalia)"

def updateResponse(linkExtension):
	return requests.get(baseSite + linkExtension)

def updateBsObj(htmlResponse):
	bsObj = BeautifulSoup(htmlResponse.content, "html.parser")
	bsObj = bsObj.find(id = 'bodyContent')
	return bsObj

extinctWildResponse = updateResponse(extinctWild)
criticalEndangerResponse = updateResponse(criticalEndanger)
normalEndangerResponse = updateResponse(normalEndanger)
vulnerableResponse = updateResponse(vulnerable)
nearThreatenedResponse = updateResponse(nearThreatened)

extinctWildBSOBJ = updateBsObj(extinctWildResponse)
criticalEndangerBSOBJ = updateBsObj(criticalEndangerResponse)
normalEndangerBSOBJ = updateBsObj(normalEndangerResponse)
vulnerableBSOBJ = updateBsObj(vulnerableResponse)
nearThreatenedBSOBJ = updateBsObj(nearThreatenedResponse)

#takes in a Beautiful Soup Object and returns a dictionary
def pageToDict(bsObj):
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
				print(i)
				keys.pop(i)
				values.pop(i)
				deleted = True
				break
		if deleted == False:
			i = i + 1
	return dict(zip(keys, values))




