import discord
from dotenv import load_dotenv
import os
import requests 
import json 
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands
from random import randrange
from discord.utils import get

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Game(name="-help for help!", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('We have Logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
    embed = discord.Embed(title='yay! im now in your server!', description='hello! thank you for welcoming me into your server. to see some of my commands, type in `-help!`!', color=0xbaffc9)
    await guild.text_channels[0].send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-meme'):
        response = requests.get("https://meme-api.herokuapp.com/gimme/me_irl")
        json_data = json.loads(response.text)
        embed = discord.Embed(title=json_data['title'], description=json_data['postLink'], color=0xffb3ba) #make the layout smoother
        embed.add_field(name= 'upvotes!', value= json_data['ups'], inline = True)
        embed.add_field(name= 'nsfw?', value= json_data['nsfw'], inline = True)
        await message.channel.send(embed=embed)
        await message.channel.send(json_data['url'])

    if message.content.startswith('-help'):
        embed = discord.Embed(title='help has arrived!', description='hi! this is a pretty simple bot. some of my commands are down below: \n\n `-kermit`: generates a kermit meme for funsies :) \n\n `-meme`: generates a meme from a reddit api ! \n\n `-news`: gets news articles from a news api \n\n `-inspire`: generates an inspirational quote if you are ever feeling down! \n\n `-affirmation`: affirmations because we all need love once in a while \n\n `-poetry`: for all you poetry/sonnet lovers ;) \n\n `-invite`: for my invite link! \n\n  more features coming soon!', color=0xbaffc9)
        await message.channel.send(embed=embed)
    
    if message.content.startswith('-about'):
        embed = discord.Embed(title='about', description='hello! thank you for welcoming me into your server. I am kermit bot, your locally sourced and fresh bot! i can generate memes, find new news, and do all kinds of tricks ;D if you ever need any help from me, make sure to type in `-help!` or dm BlueLightning#5322!', color=0xbaffc9)
        await message.channel.send(embed=embed)


    if message.content.startswith('-news'):
        response = requests.get("https://newsapi.org/v2/everything?q=random&apiKey=5864ce55c4574a8eaa9be41c7ad027f0")
        json_news = json.loads(response.text)
        newsLength = len(json_news['articles']) 
        ranNum = randrange(newsLength)
        embed = discord.Embed(title=json_news['articles'][ranNum]['title'], description=json_news['articles'][ranNum]['content'], color=0xbae1ff)
        embed.add_field(name= 'news link!', value=json_news['articles'][ranNum]['url'], inline = True)
        embed.add_field(name= 'author!', value=json_news['articles'][ranNum]['author'], inline = True)
        await message.channel.send(embed=embed)

    if message.content.startswith('-inspire'):
        response = requests.get("https://zenquotes.io/api/random/[your_key]")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " - " + json_data[0]['a']
        inspire_synonyms = ["your daily inspirational quote!" , "inspiration~"  , "your quote has arrived!"]
        ranNumInspire = randrange(0,3)
        embed = discord.Embed(title=inspire_synonyms[ranNumInspire], description=quote, color=0xffffba)
        await message.channel.send(embed=embed)

    if message.content.startswith('-affirmation'):
        response = requests.get("https://www.affirmations.dev/")
        json_data = json.loads(response.text)
        affirmation = json_data['affirmation']
        affirmation_synonyms = ["you are amazing." , "don't let anything break your stride!~"  , "affirmations for the soul~"]
        ranNumAffirmation = randrange(0,3)
        embed = discord.Embed(title=affirmation_synonyms[ranNumAffirmation], description=affirmation, color=0xC3B1E1)
        await message.channel.send(embed=embed)

    if message.content.startswith('-poetry'):
        response = requests.get("https://poetrydb.org/linecount/10/lines")
        json_data = json.loads(response.text)
        poetryLength = len(json_data) 
        ranNumPoetry = randrange(poetryLength)
        str =""
        for line in json_data[ranNumPoetry]['lines']:
            str = str + line
        embed = discord.Embed(title="sonnets!", description=str, color=0xC3B1E1) #todo: put \n after each comma for clear indenting 
        await message.channel.send(embed=embed)

    if message.content.startswith('-kermit'):
        kermit_memes = ["https://i.pinimg.com/originals/94/06/ab/9406abc9ab5741af3d9381e0fd6786b3.png" ,
        "https://i.pinimg.com/originals/25/31/20/2531209fe0aea1e82a5b3349fb4b68a8.jpg" , 
        "https://i.pinimg.com/564x/de/4a/cb/de4acb6205c98da1db5c49d3060a5683.jpg" , 
        "https://img.buzzfeed.com/buzzfeed-static/static/2016-12/14/14/asset/buzzfeed-prod-fastlane02/sub-buzz-19631-1481742974-9.png?resize=990:960?output-quality=auto&output-format=auto&downsize=640:*",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ--0gQlAQ4PGypJkSq7kLzLqZPOeB2XToDw&usqp=CAU",
        "https://cdn.discordapp.com/attachments/831761725346545704/842480318178656256/frog-me-ill-do-it-at-4-time-405-me-wow-looks-like-i-gotta-wait-till-5-now-kermit-chilling-in-bed.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ--0gQlAQ4PGypJkSq7kLzLqZPOeB2XToDw&usqp=CAU",
        "https://i.pinimg.com/564x/94/06/ab/9406abc9ab5741af3d9381e0fd6786b3.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRutoL3FSXIrXr5OI6ADBx7YVngk6sNbyk4Eg&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEyjT6EpPPf07mZCGV9EhA0cYsDS7UPQH_rg&usqp=CAU",
        "https://1tb.favim.com/preview/7/781/7812/78129/7812963.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_ySd-bvIECQKU25p1a2RcyWQ1HWc4O3eRMfklzmzFxIXs1l788QW02Bsgz_OHC-8RE3A&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjhk37xrGXa6RQ0McwubHI9YOcXiYurRWanRd0N8esy5VtQatxa5BHsBTwY7s8WYHzlNY&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx5Clxd0KCDALSZ4O4XuVF6akJ6mp_84ghvPPJoIrsHmzQHYOvBcbp6KlsUsupFLr4Za0&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLpi-oFhd-O1FX1aavCNOs1qmkHnHOWa5vJ1ZOHy27-x7ZgRotTIfb3SK2v0NBIusC4x0&usqp=CAU",
        "https://images7.memedroid.com/images/UPLOADED552/5fc2d6dd8422b.jpeg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcHK_NWlq9sZqcfmtwZAXGrCLO6G_Xy5nC9HdlvhmTBFm1omPFkamwFX5_ekhbZRNARHU&usqp=CAU",
        "https://www.dailydot.com/wp-content/uploads/2018/10/Screen-Shot-2018-10-30-at-4.25.48-PM-389x512.png",
        "https://i.pinimg.com/236x/25/d6/d2/25d6d20520952076774c9a9c97edefe0.jpg",
        "https://i.pinimg.com/236x/24/f5/b3/24f5b399e707f766b2123b70239e1411.jpg"]
        ranNumKermit = randrange(0,20)
        await message.channel.send(kermit_memes[ranNumKermit])

    if message.content.startswith('-invite'):
        embed = discord.Embed(title="invite link", description="hi! if you want to invite me to any other of your servers, here's my invite link: https://discord.com/oauth2/authorize?client_id=841107411690586153&permissions=2617764951&scope=bot", color=0xbaffc9) 
        await message.channel.send(embed=embed)


keep_alive()

client.run(TOKEN)

