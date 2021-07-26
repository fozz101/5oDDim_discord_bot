import discord
import os
from discord.ext import commands
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.members = True

#client = discord.Client(intents=intents)
client = commands.Bot(intents=intents,command_prefix = '!')





@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) 
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to my master Fozz"))



@client.event
async def on_member_join(member):
  role = discord.utils.get(member.guild.roles,name="CS Member")
  await member.add_roles(role)
  tag = "<@"+str(member.id)+">"
  tagFozz= "<@378375795892158466>"
  channel = client.get_channel(868904959071113238)
  
  await channel.send(f"Yooo {tag}, mara7bee biik fi discord el CS !  😎🎉")
  await member.send(f"Ahlaa ahla {tag}, mara7bee bik fi darek 😍 \n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.facebook.com/cs.esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.instagram.com/ieee.cs.esprit/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.linkedin.com/company/cs-esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttp://computer-esprit.ieee.tn/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nTansanèch fi follow/like ken mech 3amel 👀🤣\nFINALLY, 3andek fekra mte3 event wela project? T7eb t7assenni ?\nMy Master {tagFozz} yestana fik 🤩🤩")

    

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
    await usr.send(f"Ahlaa ahla {tag}, mara7bee bik fi darek 😍 \n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.facebook.com/cs.esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.instagram.com/ieee.cs.esprit/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.linkedin.com/company/cs-esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttp://computer-esprit.ieee.tn/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nTansanèch fi follow/like ken mech 3amel 👀🤣\nFINALLY, 3andek fekra mte3 event wela project? T7eb t7assenni ?\nMy Master {tagFozz} yestana fik 🤩🤩")
  
  await client.process_commands(message)


@client.command()
async def echo(ctx,msg):
  await ctx.send(msg)

@client.command()
async def ping(ctx):
  await ctx.send('Pong!')


@client.command(pass_context=True)
#async def clear_chat(ctx,amount=10):
async def clear(ctx,amount=10):
  channel = ctx.message.channel
  messages = await ctx.history(limit=int(amount)+1).flatten()

  if "CS ExCom" in [role.name for role in ctx.message.author.roles]:
    await channel.delete_messages(messages)
    await ctx.send(f"Fassa5tlek {amount} messages")
      
  else:
    await ctx.send("Ma3endekch access lel command hedhi 🙃")

#Try discord Embed  
'''
@client.command()
async def display(ctx):
  embed = discord.Embed(
    title= "Title",
    description="Descrioption",
    colour= discord.Colour.blue()
  )    
  embed.set_footer(text="this is a footer")
  embed.set_image(url="https://cdn.discordapp.com/attachments/867880055182589975/869293459360612402/6.jpg")
  embed.set_author(name="author name")
  embed.add_field(name="field name",value="field value",inline=False)
  embed.add_field(name="field name",value="field value",inline=True)
  embed.add_field(name="field name",value="field value",inline=True)
  await ctx.send(embed=embed)
  '''





@clear.error
async def clear_error(ctx, error):
  await ctx.send(f"billehi kifeh tconvertih l int 🤨?")
























#THANK YOU https://uptimerobot.com/
keep_alive()

client.run(os.environ['TOKEN'])