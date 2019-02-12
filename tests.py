#Graham L Wood
#Last Edited 12/2/19
import main

#Automated Testing File
print("###########USER CHECK###########")
user = main.api.me()
print(user.name)
assert user.name == "ConservationGo1"

