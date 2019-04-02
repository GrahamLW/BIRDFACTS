#Graham Wood

import requests
import bs4 #Beautiful Soup

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


