import os
import random
import discord
from dotenv import load_dotenv
import io
import aiohttp
import json
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def setnames(x,y):
    f = open("recent.txt","w")
    f.write(x+";"+y)
    f.close()
def readnames():
    f = open("recent.txt","r")
    x = f.readline().split(";")
    return x

def choosepokemon():
    wildpoke=""
    wildpokename=""
    r = random.choices(population=[1,2,3,4,5,6], 
    weights=[0.6,0.35,0.025,0.015,0.005,0.005])
    pokemon = []
    print(r)
    x = r[0]

    poke =""
    numm = 0
    toOpen = ""
    if x == 1:
        toOpen="basic.txt"
    elif x==2:
        toOpen="secondevolFINAL.txt"
    elif x==3:
        toOpen = "thirdevolfin.txt"
    elif x==4:
        toOpen = "sublegfin.txt"
    elif x==5:
        toOpen = "legfin.txt"
    elif x == 6:
        toOpen = "mythicfin.txt"
    f = open(toOpen,"r")
    for i in f:
        poke = str(i)
        poke = poke.strip()
        pokemon.append(poke)
    wildpoke = random.choice(pokemon)
    #wildpoke = "meowth-galarian"
    exceptions = []
    exceptions1 = []
    excep = ""
    num = 0
    ex = open("except.txt","r")
    for j in ex:
        excep = str(j)
        excep = excep.strip("\n")
        excep = excep.split(";")
        exceptions.append(excep[0])
        exceptions1.append(excep[1])
    if wildpoke in exceptions:
        num = exceptions.index(wildpoke)
        wildpokename = exceptions1[num]
    elif "-" in wildpoke:
        names = wildpoke.split("-")
        wildpokename = names[1]+" "+names[0]
    else:
        wildpokename = wildpoke
    setnames(wildpoke,wildpokename)


@bot.command(name='spawn', help='Spawns a wild pokemon')
async def spawn(ctx):
    choosepokemon()
    namess = readnames()
    wildpoke = namess[0]
    wildpokename = namess[1]
    print(wildpoke)
    print(wildpokename)
    url = 'https://img.pokemondb.net/artwork/'+wildpoke+'.jpg'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'x.jpg'))

    #response = random.choice(brooklyn_99_quotes)
    #await ctx.send(response)

@bot.command(name='catch',help='Catch a wild pokemon')
async def catch(ctx,*, arg):
    namess = readnames()
    wildpoke = namess[0]
    wildpokename = namess[1]
    guessname = str(arg)
    #print(guessname)
    userid = ctx.message.author.id
    pokemon = []
    #print(userid)

    with open('userdata.json') as f:
    	data = json.load(f)
    
    if guessname.lower() == wildpokename:
        
        if str(userid) in data:
            pokemon = data[str(userid)]
            if wildpokename not in pokemon:
                pokemon.append(wildpokename)
                pokemon.sort()
                data[str(userid)]=pokemon
            with open('userdata.json','w') as f:
                json.dump(data,f)
        else:
            pokemon = [wildpokename]
            data[userid]=pokemon
            with open('userdata.json','w') as f:
                json.dump(data,f)
        setnames("","")
        return await ctx.send("Gotcha!")
    else:
        return await ctx.send("Try again")

@bot.command(name='poke',help='Displays your pokemon')
async def poke(ctx):
    pokemon = []
    with open('userdata.json') as f:
    	data = json.load(f)
    print(data)
    userid = ctx.message.author.id
    person = ctx.message.author
    print(userid)
    if str(userid) not in data:
        return await ctx.send("No data right now! Catch a pokemon first.")
    else:
        pokemon = data[str(userid)]
        printer = ""
        for i in pokemon:
            printer+= (i+"\n")
        mess = "```"+str(person)+"'s pokemon\n"+printer+"```"
        return await ctx.send(mess)

"""@bot.command(name='display',help='Shows you a picture of a pokemon you own')
async def display(ctx,*, arg):
    guessname = str(arg)
    guessname = guessname.lower()
    with open('userdata.json') as f:
    	data = json.load(f)
    userid = ctx.message.author.id
    person = ctx.message.author
    if str(userid) not in data:
        return await ctx.send("No data right now! Catch a pokemon first.")
    else:
        pokemon = data[str(userid)]
        printer = ""
        if guessname in pokemon:
            url = 'https://img.pokemondb.net/artwork/'+wildpoke+'.jpg'
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status != 200:
                        return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'x.jpg'))
        else:
            return await ctx.send("Catch this pokemon first!")"""

bot.run(TOKEN)