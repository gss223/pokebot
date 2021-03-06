import re
from bs4 import BeautifulSoup
import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

url = 'https://pokemondb.net/pokedex/national'
page = opener.open(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
record = False

f = open("pokemon.txt", "w")

for link in soup.find_all("a"):
    dex = "/pokedex/"
    nameLink = link["href"]
    if dex in nameLink:
        startIndex = nameLink.find(dex)
        textIndex = startIndex + len(dex)
        rawtext = nameLink[textIndex:]
        if rawtext == "bulbasaur":
            record = True
        if record:
            f.write(rawtext+"\n")
f.close()

