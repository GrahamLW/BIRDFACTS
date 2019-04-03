#Graham Wood

import requests
from bs4 import BeautifulSoup

baseSite = "http://en.wikipedia.org"
extinctWild = "/wiki/List_of_extinct_in_the_wild_animals"
criticalEndanger = "/wiki/IUCN_Red_List_critically_endangered_species_(Animalia)"
normalEndanger = "/wiki/IUCN_Red_List_endangered_species_(Animalia)"
vulnerable = "/wiki/IUCN_Red_List_vulnerable_species_(Animalia)"
nearThreatened = "/wiki/IUCN_Red_List_near_threatened_species_(Animalia)"

extinctWildResponse = requests.get(baseSite + extinctWild)
# criticalEndangerResponse = requests.get(baseSite + criticalEndanger)
# normalEndangerResponse = requests.get(baseSite + normalEndanger)
# vulnerableResponse = requests.get(baseSite + vulnerable)
# nearThreatenedResponse = requests.get(baseSite + nearThreatened)

bsObj = BeautifulSoup(extinctWildResponse.content, "html.parser")

# for tag in bsObj.body.children:
#   print(tag.name)
#   if tag.name is not None:
#     print(tag.attrs)

bsObj = bsObj.find(id = "bodyContent")


elemsKeys = [
  tag.get('title')
  for tag in bsObj.find_all('a')
]

elemsValues = [
  tag.get('href')
  for tag in bsObj.find_all('a')
]

#cleans out things we don't want from the 
#keys and values are arrays of the same length
def cleaner(keys, values):
	i = 0
	while i < len(keys)
		if "edit" not in elemsValues[i]
			i = i + 1
		keys.pop(i)
		values.pop(i)

def dictMaker(keys, values)



