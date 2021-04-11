import discord
import requests
import random
import finance 
from finance import getTicker, tickerNews
import joel
from joel import joel_msg, yt, gifs, fakePerson
from discord.ext import commands
import os

client = commands.Bot(command_prefix="J!")
token = os.getenv("DISCORD_BOT_TOKEN")
POLYGON = os.getenv("POLYGON_API_KEY")
client.remove_command('help')



@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name="J!help"))
    print("I am online")


# help command
@client.command()
async def help(ctx):
    embed = discord.Embed(title="USAGE : J!<command>",color=discord.Color.blue())
    embed.add_field(name="GENERAL CMDS:", value="help, ping, whoami, youtube, twitch, speak")
    embed.add_field(name="IMAGE CMDS: ", value=" meme, pokemon <NAME>, pfp <gender>, gif")
    embed.add_field(name="FINANCE CMDS:", value="stock news <SYMBOL> , stock data <SYMBOL>")
    embed.add_field(name="OTHER CMDS:", value="fact, fakeperson, geekjoke, nudes, joke, trump")
    embed.set_footer(text="Joel Bot made by Discord Spy")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx) :
    embed = discord.Embed(title="Ping Result:",color=discord.Color.blue())
    embed.add_field(name="🏓", value=str(round(client.latency, 2))+"ms")
    await ctx.send(embed=embed)

@client.command(name="whoami")
async def whoami(ctx) :
    embed = discord.Embed(title="You are: "+str(ctx.message.author.name),color=discord.Color.blue())
    await ctx.send(embed=embed)

# show gifs
@client.command()
async def gif(ctx, amount=1) :
    i = random.randint(0,len(gifs))
    await ctx.send(gifs[i])

@client.command(name="pfp")
async def pfp(ctx, gender) :
    if gender.lower() == "male" or gender.lower() == "female":
        r = requests.get(f"https://randomuser.me/api/?gender={gender.lower()}")
        large = r.json()['results'][0]['picture']['large']
        await ctx.send(large)
    else :
        embed = discord.Embed(title="You need to specify a gender (male or female)",color=discord.Color.blue())
        await ctx.send(embed=embed)

# show youtube
@client.command()
async def youtube(ctx, amount=1) :
    i = random.randint(0,len(yt))
    await ctx.send(yt[i])


# joke command (official joke api)
@client.command(name="joke")
async def joke(ctx, amount=1) :
    joke = requests.get('https://official-joke-api.appspot.com/random_joke')
    if joke.status_code == 200:
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Setup:", value=str(joke.json()['setup']))
        embed.add_field(name="Punchline:", value=str(joke.json()['punchline']))
        embed.set_footer(text="Provided by the Official Joke API")
        await ctx.send(embed = embed)

# gimme a meme
@client.command(name="meme")
async def meme(ctx) :
    meme = requests.get('https://meme-api.herokuapp.com/gimme')
    if meme.status_code == 200:
        embed = discord.Embed(title=str(meme.json()['title']), color=discord.Color.blue())
        embed.add_field(name="Author:", value=str(meme.json()['author']))
        embed.add_field(name="Subreddit:", value=str(meme.json()['subreddit']))
        await ctx.send(embed=embed)
        await ctx.send(meme.json()['url'])
# joel quotes
@client.command(name="speak")
async def speak(ctx) :
    i = random.randint(0,len(joel_msg))
    embed = discord.Embed(title=joel_msg[i], color=discord.Color.blue())
    await ctx.send(embed=embed)
# person
@client.command(name="fakeperson")
async def fakeperson(ctx) :
    await ctx.send(embed=fakePerson())
# useless facts
@client.command(name="fact")
async def fact(ctx) :
    fact = requests.get('https://useless-facts.sameerkumar.website/api')
    if fact.status_code == 200:
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Did you know that...", value=fact.json()['data'])
        await ctx.send(embed=embed)
# pokemon generator
@client.command(name="pokemon")
async def pokemon(ctx, args) :
    pokemonAPI = requests.get(f"https://pokeapi.co/api/v2/pokemon/{args.lower()}")
    if pokemonAPI.status_code == 200:
        pokemonImg = pokemonAPI.json()['sprites']['other']['official-artwork']['front_default']
        await ctx.send(pokemonImg)
    else:
        await ctx.send("Invalid Pokemon name")

    
# trump quotes
@client.command(name="trump")
async def trump(ctx) :
    trump = requests.get("https://api.tronalddump.io/random/quote")
    if trump.status_code == 200:
        quote = trump.json()['value']
        appeared = trump.json()['appeared_at']
        embed = discord.Embed(title="Donald Trump",color=discord.Color.orange())
        embed.add_field(name="Quote:", value=str(quote))
        embed.add_field(name="Appeared:", value=str(appeared))
        embed.set_footer(text="Provided by api.tronalddump")
        await ctx.send(embed=embed)

# yo momma jokes
@client.command(name="yomomma")
async def yomomma(ctx) :
    momma = requests.get("https://api.yomomma.info/")
    if momma.status_code == 200:
        embed = discord.Embed(title=str(momma.json()['joke']), color=discord.Color.red())
        embed.set_footer(text="Provided by api.yomomma.info")
        await ctx.send(embed=embed)
# geek joke
@client.command(name="geekjoke")
async def geekjoke(ctx) :
    gjoke = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    if gjoke.status_code == 200:
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Setup:", value=str(gjoke.json()[0]['setup']))
        embed.add_field(name="Punchline:", value=str(gjoke.json()[0]['punchline']))
        embed.set_footer(text="Provided by the Official Joke API")
        await ctx.send(embed = embed)

@client.command(name="twitch")
async def twitch(ctx) :
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name="Username", value="joelgodly")
    embed.set_footer(text="https://www.twitch.tv/joelgodly")
    await ctx.send(embed=embed)

@client.command(name="nudes")
async def nudes(ctx) :
    response = requests.get("https://therealdiscordspy.github.io/imgdata/imgs.json")
    rNum = random.randint(0, len(response.json()['img']))
    tempUrl = "https://therealdiscordspy.github.io/imgdata/pics/"+response.json()['img'][rNum]
    url = ""
    for ch in tempUrl:
        if ch == " ":
            url+="%20"
        else:
            url+=ch    
    await ctx.send(url)
    
# stock  cmd 
@client.command(name="stock")
async def stock(ctx, args, arg2) :
    if args == "data": 
        await ctx.send(getTicker(arg2,POLYGON))
    elif args == "news":
        await ctx.send(embed=tickerNews(arg2, POLYGON))


client.run(token)