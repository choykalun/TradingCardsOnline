import requests
import json

response = requests.get("https://db.ygoprodeck.com/api/v5/cardinfo.php?fname=Wizard&attribute=light&race=spellcaster")

listOfCards = response.text

jsonList = json.loads(listOfCards)
# jsonObject = json.loads(jsonList[0])
for each in jsonList:
	print(each["name"])
