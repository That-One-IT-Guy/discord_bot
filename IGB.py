import discord
import random
import os
from datetime import datetime
import praw
import asyncio
from discord.ext import commands
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
from googletrans import Translator
import IGB
import subprocess
from geopy.distance import geodesic
from random_word import RandomWords
from PyDictionary import PyDictionary
import time
import re
import sys
import json


client = commands.Bot(command_prefix='-')
players = {}
songs = asyncio.Queue()
play_next_song = asyncio.Event()
bot = commands.Bot(command_prefix='-')
version = "2.0.0"
admincode = random.randrange(10000, 99999)
dictionary=PyDictionary()
amounts = {}
pickels = {}


@client.event
async def on_ready():
    print('We have logged in as {0.user}!'.format(client))
    reddit = praw.Reddit(client_id="CLIENT_ID",
                     client_secret="CLIENT_SECRET",
                     password="PASSWORD",
                     user_agent="AGENT",
                     username="USERNAME")
    print("Logged into reddit!")
    print(reddit.user.me())
    await client.change_presence(status=discord.Status.online, activity=discord.Game("FBI Server Bug /_-"))
    print("Status updated!")
    global amounts
    global pickels
    try:
        with open('amounts.json') as f:
            amounts = json.load(f)
            print("amounts.json loaded!")
    except FileNotFoundError:
        print("Could not load amounts.json")
        amounts = {}
    try:
        with open('pickels.json') as f:
            pickels = json.load(f)
            print("pickels.json loaded!")
    except FileNotFoundError:
        print("Could not load pickels.json")
        pickels = {}
    print("-Admin code is : " + str(admincode) +" !-")
    print("---------------------------------------------------------------------------")

async def audio_player_task():
    while True:
        play_next_song.clear()
        current = await songs.get()
        current.start()
        await play_next_song.wait()


def toggle_next():
    client.loop.call_soon_threadsafe(play_next_song.set)
    print("Music data injected")

@client.command(pass_context=True)
async def play(ctx, url):
    """Play audio from url"""
    print("oh")
    channel = author.voice.channel
    await channel.connect()
    player = await voice.create_ytdl_player(url, after=toggle_next)
    await songs.put(player)

client.loop.create_task(audio_player_task())

@client.command(pass_context=True)
async def hello(ctx):
    """Says hello back"""
    await ctx.send('`Hello!`')

@client.command(pass_context=True)
async def cpr(ctx):
    """Responds with a conversation starter"""
    constart = ['Whats your favorite city?', 'Whats behind you?', 'Whats up everyone?!?', 'Hows it going?', 'Anyone doing anything big today?', 'Whats your favorite thing to do?', 'Whats you favorite meme?', 'MAKE SOME NOISE!!!!', 'Its hot in here, I better go leave.', 'Whats your favorite sport?', 'If you could go anywhere, where would you go?', 'Whats your favorite word?', 'What do you want to be when you grow up?', 'Do you have a favorite food?', 'What is your favorite number?']
    constartchoice = random.choice(constart)
    confix = "`" + constartchoice + "`"
    await ctx.send(confix)

@client.command(pass_context=True)
async def dice(ctx):
    """Role a dice (1-6)"""
    cionstart = ["1", "2", "3", "4", "5", "6"]
    cionstartchoice = random.choice(cionstart)
    cionfix = "`" + cionstartchoice + "`"
    await ctx.send(cionfix)

@client.command(pass_context=True)
async def data(ctx):
    """Responds with some data that the bot uses"""
    import time
    await ctx.send("`Context data with this request: " + " - Message author: " + str(ctx.message.author) + " - Message channel: " + str(ctx.message.channel) + " - Message CTX: " + str(ctx.message.content)  + " - CTX STR data: " + str(ctx) + " - Guild owner: " + str(ctx.guild.owner) + " - Guild name: " + str(ctx.guild.name) + " - Guild ID: " + str(ctx.guild.id) + " Guild icon url: ` " + str(ctx.guild.icon_url))
    voicechannel = discord.utils.get(ctx.guild.channels, name='bot alerts')
    await vc.disconnect()
    time.sleep(1)
    vc = await voicechannel.connect()
    vc.play(discord.FFmpegPCMAudio("data.m4a"), after=lambda e: print('data', e))
    time.sleep(12)
    await vc.disconnect()


@client.command(pass_context=True)
async def time(ctx):
    """Get the current time"""
    now = datetime.now()
    await ctx.send("`" + str(now) + "`")

@client.command(pass_context=True)
async def meme(ctx, ama="1"):
    """Get a random meme from readdit"""
    ama = int(ama)
    import time
    while ama > 0:
        try:
            reddit = praw.Reddit(client_id="CLIENT_ID",
                            client_secret="CLIENT_SECRET",
                            password="PASSWORD",
                            user_agent="AGENT",
                            username="USERNAME")
            memes_submissions = reddit.subreddit('memes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            m = await ctx.send(submission.url)
            await m.add_reaction("\U0001F44D")
            await m.add_reaction("\U0001F44E")
            ama = ama - 1
        except:
            await ctx.send("`Sorry, Reddit isnt being nice and put me in timeout. (Try again later)`")
            ama = 0

@client.command(pass_context=True)
async def calc(ctx, one="420", type="Help!", two="69"):
    """Its a calculator"""
    try:
        testdata = int(one)
        testdata = int(two)
        if type == "+":
            out = int(one) + int(two)
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "-":
            out = int(one) - int(two)
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "/":
            out = int(one) / int(two)
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "x":
            out = int(one) * int(two)
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "*":
            out = int(one) * int(two)
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "^":
            out = int(one) ** int(two)
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "**":
            out = int(one) ** int(two)
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "root":
            out = int(one) **(1 / int(two))
            await ctx.send("`Thats " + str(out) + "!`")
        if type == "Help!":
            await ctx.send("`Just type FirstNumber symble SecondNumber!\nSymbles are: +, -, /, x, *, ^, **, root.`")
    except:
        await ctx.send("```Thats not a number...\nJust type FirstNumber symble SecondNumber!\nSymbles are: +, -, /, x, *, ^, **, root.```")

@client.command(pass_context=True)
async def translate(ctx, one="Bonjour", to="en"):
    """Translate stuff to ther languages "quote" stuff if its more then one word! Then use the language code"""
    translator = Translator()
    translations = translator.translate([one], dest=to)
    for translation in translations:
        await ctx.send("```" + str(translation.origin) + "-" + to + ">" + str(translation.text) + "```")

@client.command(pass_context=True)
async def restart(ctx, code="0"):
    """Debug and update the bot, must have a admin code that changes every time!"""
    if code == str(admincode):
        await ctx.send("```Hold on a sec, let me go update myself. This should take about 10 seconds! WARNING ADMIN CODE BYPASSED UPDATE CONSOLE!```")
        print("Quiting this service!")
        os.system('cls')
        subprocess.call("IGB.py", shell=True)
    elif ctx.author.id == 615876088085741568:
        await ctx.send("```Hold on a sec, let me go update myself. This should take about 10 seconds!```")
        print("Quiting this service!")
        os.system('cls')
        subprocess.call("IGB.py", shell=True)
    else:
        await ctx.send("```INVALID ADMIN CODE!```")

@client.command(pass_context=True)
async def antonym(ctx, word="Hi"):
    """Get some antonym of a word"""
    antv = dictionary.antonym(word)
    await ctx.send("```" + str(antv) + "```")

@client.command(pass_context=True)
async def number(ctx, min=0, max=999999999999999999999999999999999999999999999):
    """Get a random number (min) (max)"""
    min = int(min)
    max = int(max)
    num = random.randrange(min, max)
    await ctx.send("```" + str(num) + "```")

@client.command(pass_context=True)
async def alert(ctx, Title="", desc="", foot="", author=""):
    """Create a embeded alert (Title, description, footer, author)"""
    embed = discord.Embed(
        title = Title,
        description = desc,
        colour = discord.Colour.blue()
    )
    embed.set_footer(text=foot)
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/725167412999356446/d9ad48a45c86c05f46d6a1598660f7ca.webp?size=128')
    embed.set_author(name=author)
    await ctx.send(embed=embed)

@client.command(pass_content=True)
async def ping(ctx):
    """Pong! (Latencey)"""
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

@client.command(pass_content=True, hidden=True)
async def pickel(ctx):
    calck = random.randrange(1, 10)
    size = "=" * calck
    await ctx.send("```8" + str(size) + "D```")

@client.command(pass_context=True)
async def balance(ctx):
    """Find out how much stuff you have"""
    id = str(ctx.message.author.id)
    if id in amounts and pickels:
        await ctx.send("```You have " + str(amounts[id]) +" in the bank, and " + str(pickels[id]) + " pickels in your frige.```")
    else:
        await ctx.send("```You do not have an account```")

@client.command(pass_context=True)
async def mbalance(ctx):
    """Find out how much money you have"""
    id = str(ctx.message.author.id)
    if id in amounts and pickels:
        await ctx.send("```You have " + str(amounts[id]) +" in the bank.```")
    else:
        await ctx.send("```You do not have an account```")

@client.command(pass_context=True)
async def pbalance(ctx):
    """Find out how much money you have"""
    id = str(ctx.message.author.id)
    if id in amounts and pickels:
        await ctx.send("```You have " + str(pickels[id]) +" in the frige.```")
    else:
        await ctx.send("```You do not have an account```")

@client.command(pass_context=True, hidden=True)
async def bal(ctx):
    """Find out how much money you have"""
    id = str(ctx.message.author.id)
    if id in amounts and pickels:
        await ctx.send("```You have " + str(amounts[id]) +" in the bank, and " + str(pickels[id]) + " pickels in your frige.```")
    else:
        await ctx.send("```You do not have an account```")

@client.command(pass_context=True)
async def mbal(ctx):
    """Find out how much money you have"""
    id = str(ctx.message.author.id)
    if id in amounts and pickels:
        await ctx.send("```You have " + str(amounts[id]) +" in the bank.```")
    else:
        await ctx.send("```You do not have an account```")

@client.command(pass_context=True)
async def pbal(ctx):
    """Find out how much money you have"""
    id = str(ctx.message.author.id)
    if id in amounts and pickels:
        await ctx.send("```You have " + str(pickels[id]) +" in the frige.```")
    else:
        await ctx.send("```You do not have an account```")

@client.command(pass_context=True)
async def register(ctx):
    """Make an account"""
    id = str(ctx.message.author.id)
    if id not in amounts and pickels:
        amounts[id] = 100
        pickels[id] = 0
        await ctx.send("```You are now registered```")
        _save()
    else:
        await ctx.send("```You already have an account```")

@client.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    """Transfer money to account"""
    if amount >= 0:
        primary_id = str(ctx.message.author.id)
        other_id = str(other.id)
        if primary_id not in amounts:
            await ctx.send("```You do not have an account```")
        elif other_id not in amounts:
            await ctx.send("```The other party does not have an account```")
        elif amounts[primary_id] < amount:
            await ctx.send("```You cannot afford this transaction```")
        else:
            amounts[primary_id] -= amount
            amounts[other_id] += amount
            await ctx.send("```Transaction complete```")
        _save()
    else:
        await ctx.send("```Transaction incomplete, under minimum amount (1)!```")

@client.command(pass_context=True)
async def ptransfer(ctx, amount: int, other: discord.Member):
    """Transfer pickels to account"""
    if amount >= 0:
        primary_id = str(ctx.message.author.id)
        other_id = str(other.id)
        if primary_id not in pickels:
            await ctx.send("```You do not have an account```")
        elif other_id not in pickels:
            await ctx.send("```The other party does not have an account```")
        elif pickels[primary_id] < amount:
            await ctx.send("```You cannot afford this transaction```")
        else:
            pickels[primary_id] -= amount
            pickels[other_id] += amount
            await ctx.send("```Transaction complete (pickels)```")
        _save()
    else:
        await ctx.send("```Transaction incomplete, under minimum amount (1)!```")

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)
    with open('pickels.json', 'w+') as f:
        json.dump(pickels, f)

@client.command(hidden=True)
async def save():
    _save()

@client.command(pass_context=True)
@commands.cooldown(1, 3600, commands.cooldowns.BucketType.member)
async def work(ctx):
    primary_id = str(ctx.message.author.id)
    amounts[primary_id] += 18
    _save()
    await ctx.send("```You worked an hour.```")

@client.command(pass_context=True)
@commands.cooldown(1, 86400, commands.cooldowns.BucketType.member)
async def daily(ctx):
    primary_id = str(ctx.message.author.id)
    amounts[primary_id] += 50
    _save()
    await ctx.send("```You got your daily money for still being alive.```")

@client.command(pass_context=True)
async def give(ctx, item, amount: int, other: discord.Member):
    """Summon stuff like god"""
    if ctx.author.id == 615876088085741568:
        pid = str(other.id)
        if item == "money":
            amounts[pid] += amount
            _save()
            await ctx.send("```Transaction done! (Don't ask where it came from)```")
        elif item == "pickel":
            pickels[pid] += amount
            _save()
            await ctx.send("```Transaction done! (Don't ask where it came from)```")
        else:
            await ctx.send("```Item not valid```")
    else:
        await ctx.send("```You dont have accses to do that!```")

@client.command(pass_context=True)
async def gamble(ctx, nam:int):
    if int(nam) >= 1:
        primary_id = str(ctx.message.author.id)
        if primary_id not in pickels:
            await ctx.send("```You do not have an account```")
        elif amounts[primary_id] < int(nam):
            await ctx.send("```You cannot afford the gamble```")
        else:
            sm = int(nam - nam)
            bg = int(nam * 2)
            gen = random.randrange(int(sm), int(bg))
            print(str(gen))
            fina = int(gen) - int(nam)
            amounts[primary_id] += int(fina)
            _save()
            await ctx.send("```You got: " + str(fina) + "```")
    else:
        await ctx.send("```Did not gamble enough for minimun calculation```")

@client.command(pass_context=True)
async def callbal(ctx, other: discord.Member):
    usid = str(other.id)
    if usid in amounts and pickels:
        await ctx.send("```They have " + str(amounts[usid]) +" in the bank, and " + str(pickels[usid]) + " pickels in there frige.```")
    else:
        await ctx.send("```User dos not have a account or could not be found```")

@client.command(pass_context=True)
async def textme(ctx, number:int):
    await ctx.send("```Don't bully or spam when using this bot, or you will get banned from uing this!```")
    await ctx.send("```Not avalible yet sorry```")

client.run("SECRET")
