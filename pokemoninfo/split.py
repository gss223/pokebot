f = open("evolute.txt","r")
x = open("secondevolute.txt","w")

incr = 1
secon = []

for line in f:
    poke = ""
    if incr==2:
        poke = str(line)
        secon.append(poke)
        print(poke)
        incr = 0
    incr+=1  
    
for i in secon:
    i = i.strip()
    print(i)
    x.write(i+"\n")
x.close()





