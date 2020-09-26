import re
from bs4 import BeautifulSoup
import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

url = 'https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon_by_three-stage_evolution'
page = opener.open(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
record = False

f = open("evol.txt", "w")

for link in soup.find_all("a"):
    dex = 'title="'
    nameLink = str(link)
    #print (nameLink)
    if dex in nameLink:
        startIndex = nameLink.find(dex)
        textIndex = startIndex + len(dex)
        rawtext = nameLink[textIndex:]
        endIndex = rawtext.find('"')+textIndex
        rawtext = nameLink[textIndex:endIndex]
        #rawtext.strip(" \r\n\t")
        rawtext = rawtext.lower()
        #print(rawtext)
        if rawtext == "bulbasaur":
            record = True
        if record:
            if "nidoran" in rawtext:
                f.write("nidoran\n")
            else:
                #print(rawtext)
                f.write(rawtext+"\n")
        if rawtext == "dragapult":
            record = False
            break
f.close()