import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)





@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) 
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to my master Fozz - Beta version"))





@client.event
async def on_member_join(member):
  tag = "<@"+str(member.id)+">"
  tagFozz= "<@378375795892158466>"
  channel = client.get_channel(868904959071113238)
  
  await channel.send(f"Yooo {tag}, mara7bee biik fi discord el CS !  😎🎉")
  await member.send(f"Ahlaa ahla {tag}, mara7bee bik fi darek 😍 \n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.facebook.com/cs.esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.instagram.com/ieee.cs.esprit/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.linkedin.com/company/cs-esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttp://computer-esprit.ieee.tn/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nTansanèch fi follow/like ken mech 3amel 👀🤣\nFINALLY, 3andek fekra mte3 event wela project? T7eb t7assen el bot eli ya7ki m3ek tawa ?\nMy Master {tagFozz} yestana fik 🤩🤩")

    

@client.event
async def on_message(message):
  my_id= message.author.id
  tag = "<@"+str(my_id)+">"
  tagFozz= "<@378375795892158466>"
  #select channel
  channel = client.get_channel(867880055182589975)
  usr =  await client.fetch_user(378375795892158466)
  
  if message.author == client.user:
    return
  if message.content.startswith('test'):
    await message.channel.send(f"mara7beee {tag}  ")
    
    #await channel.send("ahlaaa")
    await usr.send(f"Ahlaa ahla {tag}, mara7bee bik fi darek 😍 \n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.facebook.com/cs.esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.instagram.com/ieee.cs.esprit/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.linkedin.com/company/cs-esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttp://computer-esprit.ieee.tn/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nTansanèch fi follow/like ken mech 3amel 👀🤣\nFINALLY, 3andek fekra mte3 event wela project? T7eb t7assen el bot eli ya7ki m3ek tawa ?\nMy Master {tagFozz} yestana fik 🤩🤩")


#THANK YOU https://uptimerobot.com/
keep_alive()

client.run(os.environ['TOKEN'])