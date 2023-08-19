import requests 
from bs4 import BeautifulSoup
# This program adheres to the robots.txt code of conduct that is set by the website
global header 
header =  {'User-Agent': 'Mozilla/5.0'} 

def ConnectionTest(): # This function tests the connection to the website and returns a status code
    testConnection = requests.get("https://www.pets4homes.co.uk/sale/puppies/basset-hound/", headers=header)
    if testConnection.status_code == 200:
        print("Connection successful")
    else:
        print("Connection unsuccessful")

soup = BeautifulSoup(requests.get("https://www.pets4homes.co.uk/sale/puppies/basset-hound/", headers=header).content, 'html.parser')
resultsNum = soup.find("h2", class_="Nj").string # The class value changes on the website's HTML so change if not working
advertNameList = []
priceList = []
averagePriceList = [] 
breederStatusList = []
timeTagList = []

for tagHTML in soup.find_all(("h2"), class_="aq"): # The class tag must be updated if working incorrectly
    advertNameList.append(tagHTML.text)  

for tagHTML in (soup.find_all("span", class_="bq")): # The class tag must be updated if working incorrectly
    priceList.append(tagHTML.text)

for tagHTML in (soup.find_all("span", class_="bq")): # The class tag must be updated if working incorrectly
    averagePriceList.append(tagHTML.text[1:].replace(",", ""))

for tagHTML in (soup.find_all("div", class_="Zp")): # The class tag must be updated if working incorrectly
    timeTagList.append(tagHTML.text)
    for i in range(len(timeTagList)):
        if timeTagList[i] == '':
            timeTagList[i] = "No time result"

# for tagHTML in (soup.find_all("span", class_="Gg")): # The class tag must be updated if working incorrectly
#     if "Boost" in tagHTML:
#         pass
#     else:
#         breederStatusList.append(tagHTML.text)

for i in range(int(resultsNum[0:2])-1):
    print(i, advertNameList[i], "-", priceList[i], "-", ''' breederStatusList[i],  "-" ''',  timeTagList[i])

averagePrice = 0
for i in range(len(averagePriceList)):
    averagePrice = averagePrice + int((averagePriceList[i]))
#print("Average Price of Available Dogs is: £" + str(averagePrice / int(resultsNum[0:2])))

def sortByOldestFirst():
    ans = input("Would you like to view the list sorted by oldest first?\nY/N\n")
    if ans == "Y" or ans == "y":
        advertNameList.reverse()
        timeTagList.reverse()
        priceList.reverse()
        for i in range(int(resultsNum[0:2])-1):
            print(advertNameList[i], "-", priceList[i], "-", timeTagList[i])

def sortByPrice():
    listLength = len(averagePriceList)
    for i in range(listLength): # Use bubble sort, probably needs while loop
        swapped = False
        for j in range(0, listLength-i-1):
            if averagePriceList[0] > averagePriceList[1]:
                print(listLength)
                pass

sortByPrice()
