import os
import discord
import random
import time
from discord import Intents, Client, Message
from responses import get_response
from webhookdata import sendfeedback
from vidsscraper import scrapeyoutube
dtoken = os.environ['DISCORD_TOKEN']
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
presstr = "With with the Money🤑🤑🔥🔥"
playv = discord.ActivityType.playing
textvar = "-------------------------------------------------"
textval = "Use `.help` for info about the Money Mallard Bot. \n Use `.memes` for the list of memes you can use. \n Use `.meme` and one of the available memes for Money Mallard to send that meme. \n Use `.vids` for the latest NBA videos. \n Use `.whowwins` followed by 2 teams to see my guess on a game.  \n Use `.teams` to display all NBA Teams. (Useful for mocks.) \n Use `.badtake` for something very cool 🤫🤫 (you'll love it) \n Use `.mytake` followed by your take to see my opinion \n \n Use `.feedback` to send feedback to the creator. \n Use `.info` for more info and the source code. \n Use `.add` to add Money Mallard to your server. \n **" + textvar + "**"
#



#

async def send_message(message: Message, user_message: str, user) -> None:
  
  
  if not user_message:
    #REF.
    return

  if is_private := user_message[0] == "?":
    user_message = user_message[1:]

  try:
    response: str = get_response(user_message, user)
    if response == "help_embed":
      global embcolor
      embcolor = 0x2c6437
      if random.randint(0, 2) == 1:
        embcolor = 0xffc300
      stringofemb = "This is the necessary info about the Money Mallard Bot."
      embed=discord.Embed(title="Money Mallard", description=stringofemb, color=embcolor)
      embed.add_field(name=textvar, value=textval, inline=False)
      async def sendauth():
        await message.author.send(embed=embed)
      sendauth() if is_private else await message.channel.send(embed=embed, reference=message)
    elif response ==  "memes_embed":
      embcolor = 0x2c6437
      if random.randint(0, 2) == 1:
        embcolor = 0xffc300
      stringofemb = "This is the list of all memes."

      #
      embed=discord.Embed(title="Memes", description=stringofemb, color=embcolor)
      embed.add_field(name=textvar, value="`.meme lmao`", inline=False)
      embed.set_image(url="https://i.ibb.co/6BdYFZn/LMFAOOOOOOO.png")

      embed2=discord.Embed(color=embcolor)
      embed2.add_field(name=textvar, value="`.meme neutral`", inline=False)
      embed2.set_image(url="https://i.ibb.co/Pjv8DCr/woah-funny-joke.jpg")

      embed3=discord.Embed(color=embcolor)
      embed3.add_field(name=textvar, value="`.meme yell`", inline=False)
      embed3.set_image(url="https://i.ibb.co/8mY05mQ/hames-jarden.jpg")

      embed4=discord.Embed(color=embcolor)
      embed4.add_field(name=textvar, value="`.meme huh`", inline=False)
      embed4.set_image(url="https://i.ibb.co/q00L8rq/huh.jpg")
      
      
      #
      embedlist = [embed, embed2, embed3, embed4]
      #
      async def sendauth():
        await message.author.send(embeds=embedlist)
      sendauth() if is_private else await message.channel.send(embeds=embedlist, reference=message)
    elif response == "lmao" or response == "huh" or response == "neutral" or response == "yell":
      async def sendauth():
        await message.author.send(file=discord.File(response + ".jpg"))
      sendauth() if is_private else await message.channel.send(file=discord.File(response + ".jpg"))
      await message.delete()
    elif "feedback_ret" in response:
        embcolor = 0x2c6437
        if random.randint(0, 2) == 1:
          embcolor = 0xffc300
        embed=discord.Embed(title="Feedback Delivered", description="Thank you for your feedback!", color=embcolor)
        sendfeedback(response[13:], message.author.name, message.author.id)
        async def sendauth():
          await message.author.send(embed=embed)
        sendauth if is_private else await message.channel.send(embed=embed, reference=message)
    elif "vids_embed" in response:
        embcolor = 0x2c6437
        if random.randint(0, 2) == 1:
          embcolor = 0xffc300
        stringofemb = "**" + textvar + "**" + "\n \n **What videos would you like to see?** \n \n **" + textvar + "**"
        embed=discord.Embed(title="Videos", description=stringofemb, color=embcolor)
        embed.add_field(name="", value="`.vids espn` The ESPN Youtube Channel \n `.vids nba` The official NBA Youtube Channel \n `.vids blrp` The Bleacher Report Youtube Channel \n  `.vids chaz` The Youtube Channel for Chaz NBA \n `.vids flight` NotTheAverageFlight's Youtube Channel (curry4mvps about to flip) \n `.vids jxmy` The Youtube Channel for JxmyHigherroler \n `.vids jess` Jesser's youtube Channel \n `.vids cash` CashNasty's Youtube Channel \n \n **" + textvar + "**", inline=False)
        async def sendauth():
          await message.author.send(embed=embed)
        sendauth() if is_private else await message.channel.send(embed=embed, reference=message)
    elif "ytscr" in response:
        scrdvids = scrapeyoutube(response[6:].lower())
        resstr = response[6:]
        embcolor = 0x2c6437
        if random.randint(0, 2) == 1:
          embcolor = 0xffc300
        stringofemb = resstr.upper()
        async def sendauth():
          await message.author.send(embed=scrdvids)
        sendauth() if is_private else await message.channel.send(embed=scrdvids, reference=message)
    elif "teams_embed" in response:
        print("what")
        embcolor = 0x2c6437
        if random.randint(0, 2) == 1:
          embcolor = 0xffc300
        embed=discord.Embed(title="NBA Teams", description="", color=embcolor)
        embed.add_field(name="", value="**" + textvar + "**" + ' \n `.teams fullnames` Ex: **"Detroit Pistons"** \n', inline=False)
        embed.add_field(name="", value='`.teams teamnames` Ex: **"Spurs"** \n', inline=False)
        embed.add_field(name="", value='`.teams abrvs` Ex: **"LAC"** \n', inline=False)
        embed.add_field(name="", value='`.teams cities` Ex: **"Denver"** \n **' + textvar + "**", inline=False)
        async def sendauth():
          await message.author.send(embed=embed)
        sendauth if is_private else await message.channel.send(embed=embed, reference=message)
    elif "badtake" in response:
        channel = message.channel
        webhook = await message.channel.create_webhook(name=message.author.display_name)
        sent = await webhook.send(content=response[8:], avatar_url=message.author.avatar)
        await message.delete()
        await webhook.delete()
        time.sleep(2)
        await message.channel.send("woah that's an awful take! 😂😂 <@" + str(message.author.id)+ "> knows **0**‼‼ ball CONFIRMED😂😂")
    elif "mytake" in response:
        choi = random.choice(["🔥", "💯", "👍", "🆗", "🤷‍♂️", "🙅‍♂️", "😅", "🧢", "🤣", "💀"])
        await message.add_reaction(choi)
    elif "info_embed" in response:
        embcolor = 0x2c6437
        if random.randint(0, 2) == 1:
          embcolor = 0xffc300
        embed=discord.Embed(title="Additional Info", description="", color=embcolor)
        embed.add_field(name=textvar, value="Made by [theswagduck](https://github.com/duckswag) \n Made with Custom Python \n [Github](https://github.com/duckswag/money-mallard) \n [Replit](https://replit.com/@theswagduck/Money-Mallard) \n [Invite](https://discord.com/api/oauth2/authorize?client_id=1207085383800856596&permissions=275414903872&scope=bot)", inline=False)
        embed.add_field(name="", value='**Color Pallete:** \n Green: #ffc300 \n Yellow: #ffc300 \n', inline=True)
        embed.add_field(name="", value='**Changelog:** \n [Changelog](https://github.com/duckswag/money-mallard/blob/main/CHANGELOG.md) \n', inline=True)
        embed.add_field(name="", value='**Timespan:** \n May be active around 10AM-12PM EST with temporary breaks. \n', inline=True)
        embed.add_field(name="**" + textvar + "**", value = "[ᶜˡᶦᶜᵏ ʰᵉʳᵉ](https://discord.com/vanityurl/dotcom/steakpants/flour/flower/index11.html)", inline=False)
        embed.set_thumbnail(url="https://i.ibb.co/hHLRt5x/Mallard.png")
        async def sendauth():
          await message.author.send(embed=embed)
        sendauth() if is_private else await message.channel.send(embed=embed, reference=message)
    else:
      async def sendauth():
        await message.author.send(response)
      sendauth if is_private else await message.channel.send(response, reference=message)

  except Exception as e:
    #e

#
@client.event
async def on_ready() -> None:
  #print(f'{Client.user} is now running.')
  await client.change_presence(activity=discord.Activity(type=playv, name=presstr))
#
  
  @client.event
  
  async def on_message(message: Message) -> None:
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    #print(f'[{channel}] {username}: "{user_message}"')
    user = message.author
    await send_message(message, user_message, user)

def main() -> None:
  client.run(token=dtoken)

if __name__ == '__main__':
  main()
