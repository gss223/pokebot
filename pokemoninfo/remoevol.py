f = open("evol.txt","r")
duoevol = open("evol2fin.txt","r")
ofile = open("evolute.txt","w")
pokemon = []
x = []
for line in f:
    pokemon.append(str(line))
for poke in duoevol:
    if str(poke) not in pokemon:
        #print(str(poke))
        x.append(str(poke))
        #print(poke)
        #ofile.write(str(poke))
for i in x:
    i = i.strip()
    print(i)
    ofile.write(i+"\n")
ofile.close()

