f = open("pokemonfin.txt","r")
x = open("thirdevolfin.txt","r")
y = open("secondevolFINAL.txt","r")
z = open("sublegfin.txt","r")
l = open("legfin.txt","r")
c = open("mythicfin.txt","r")
t = open("basic.txt","a")
pokemon = []
poke = ""
for i in x:
    poke = str(i)
    poke = poke.strip()
    pokemon.append(poke)
for i in y:
    poke = str(i)
    poke = poke.strip()
    pokemon.append(poke)
for i in z:
    poke = str(i)
    poke = poke.strip()
    pokemon.append(poke)
for i in l:
    poke = str(i)
    poke = poke.strip()
    pokemon.append(poke)
for i in c:
    poke = str(i)
    poke = poke.strip()
    pokemon.append(poke)
for j in f:
    poke = str(j)
    poke = poke.strip()
    if poke not in pokemon:
        t.write(str(j))


f.close()
x.close()
y.close()
z.close()
l.close()
c.close()
t.close()