x = open("galarian.txt","r")
poke = ""
pokemon = []
for line in x:
    poke = str(line)
    print(poke)
    poke = poke.strip()
    poke = poke+"-galarian\n"
    pokemon.append(poke)
x.close()
y = open("galarian.txt","w")
for i in pokemon:
    print (i)
    y.write(i)
y.close()