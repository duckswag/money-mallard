import scrapetube
import discord
import random
from inforeturn import gettitle
espn = "UCiWLfSweyRNmLpgEHekhoAg"
nba = "UCWJ2lWNubArHWmf3FIHbfcQ"
blrp = "UC9-OpMMVoNP5o10_Iyq7Ndw"
chaz = "UChgDp_uE5PVqnpdV05xKOOA"
flight = "UCoGIPQ7M4NWai7LRgRhaSOg"
jxmy = "UC3L9XPe0_FGfRG-CMGtBvFg"
jess = "UCQIUhhcmXsu6cN6n3y9-Pww"
cash = "UCvyTdLw8SkVmUcHYXSDEGwA"
dash = "-------------------------------------------------"
tab = []

def scrapeyoutube(channel):
  count = 0
  if channel == "espn":
    channel = espn
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    global embed
    embed=discord.Embed(title="ESPN", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  elif channel == "nba":
    channel = nba
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    embed=discord.Embed(title="NBA", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  elif channel == "blrp":
    channel = blrp
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    embed=discord.Embed(title="Bleacher Report", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  elif channel == "chaz":
    channel = chaz
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    embed=discord.Embed(title="Chaz NBA", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  elif channel == "flight":
    channel = flight
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    embed=discord.Embed(title="NotYourAverageFlight", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  elif channel == "jxmy":
    channel = jxmy
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    embed=discord.Embed(title="JxmyHighroller", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  elif channel == "jess":
    channel = jess
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    embed=discord.Embed(title="Jesser", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  elif channel == "cash":
    channel = cash
    videos = scrapetube.get_channel(channel, limit=5)
    embcolor = 0xff8331
    if random.randint(0, 2) == 1:
      embcolor = 0x0078ea
    embed=discord.Embed(title="CashNasty", description="**" + dash + "**", color=embcolor)
    for video in videos:
      count += 1
      embed.add_field(name="", value="[" + gettitle(video['videoId']) + "](https://www.youtube.com/watch?v=" + video['videoId'] + ")", inline=False)
      tab.append("" + "" + video['videoId'])
    else:
      embed.add_field(name=dash, value="", inline=False)
      return embed
  else:
    return "Sorry, " + '"' + channel + '"' + " isn't a valid option."
