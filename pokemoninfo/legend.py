import re
from bs4 import BeautifulSoup
import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

url = 'https://www.serebii.net/pokemon/legendary.shtml'
page = opener.open(url)
html = page.read()#.decode('utf-8')
soup = BeautifulSoup(html, "html.parser")
record = False

f = open("mythic.txt", "w")

for link in soup.find_all("a"):
    dex = "/pokemon/"
    #print(link)
    nameLink = str(link)
    #print(nameLink)
    if dex in nameLink:
        #print ("x")
        startIndex = nameLink.find(dex)
        textIndex = startIndex + len(dex)
        rawtext = nameLink[textIndex:]
        endIndex = rawtext.find('/">')+textIndex
        rawtext = nameLink[textIndex:endIndex]
        rawtext.strip(" \r\n\t")
        #print(rawtext)
        if rawtext == "mew":
            record = True
        if record:
            f.write(rawtext+"\n")
        if rawtext == "melmetal":
            record = False
            break
f.close()
