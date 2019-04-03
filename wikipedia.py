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

extinctWildResponse = requests.get(baseSite + extinctWild)
criticalEndangerResponse = requests.get(baseSite + criticalEndanger)
normalEndangerResponse = requests.get(baseSite + normalEndanger)
vulnerableResponse = requests.get(baseSite + vulnerable)
nearThreatenedResponse = requests.get(baseSite + nearThreatened)

extinctWildBSOBJ = BeautifulSoup(extinctWildResponse.content, "html.parser")
extinctWildBSOBJ = extinctWildBSOBJ.find(id = "bodyContent")
criticalEndangerBSOBJ = BeautifulSoup(criticalEndangerResponse.content, "html.parser")
criticalEndangerBSOBJ = criticalEndangerBSOBJ.find(id = "bodyContent")

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

print(pageToDict(extinctWildBSOBJ))




