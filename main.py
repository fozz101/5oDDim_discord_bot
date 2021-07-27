import discord
import os
import asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from PIL import Image, ImageDraw,ImageFont
from io import BytesIO
import numpy as np
from keep_alive import keep_alive
import requests
import json
import random
from replit import db


intents = discord.Intents.default()
intents.members = True


client = commands.Bot(intents=intents,command_prefix = '!')
client.remove_command("help")

players = {}



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) 
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to my master Fozz"))





@client.event
async def on_member_join(member):
  welcome = Image.open("welcome.png")
  
  asset = member.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  #avatar= Image.open(data)
  # Open the input image as numpy array, convert to RGB
  img=Image.open(data).convert("RGB")
  npImage=np.array(img)
  h,w=img.size

  # Create same size alpha layer with circle
  alpha = Image.new('L', img.size,0)
  draw = ImageDraw.Draw(alpha)
  draw.pieslice([0,0,h,w],0,360,fill=255)

  # Convert alpha Image to numpy array
  npAlpha=np.array(alpha)

  # Add alpha layer to RGB
  npImage=np.dstack((npImage,npAlpha))

  # Save with alpha
  #Image.fromarray(npImage).save('result.png')
  avatarr = Image.fromarray(npImage)
  avatarr = avatarr.resize((74,74))
  welcome.paste(avatarr,(102,62))

  draw = ImageDraw.Draw(welcome)
  font = ImageFont.truetype("ARIAL.TTF",30)

  username = str(member.name)
  W,H = 600,285
  w,h=draw.textsize(username)
  draw.text(((W-w)/2-180,(H-h)/2-120), username,(255,153,51), font=font) 
  #avatar = avatar.resize((74,74))
  #welcome.paste(avatar,(102,62))
  welcome.save("final.png")

  role = discord.utils.get(member.guild.roles,name="CS Member")
  await member.add_roles(role)
  tag = "<@"+str(member.id)+">"
  tagFozz= "<@378375795892158466>"
  channel = client.get_channel(868904959071113238)
  
  await channel.send(f"Yooo {tag}, mara7bee biik fi discord el CS !  😎🎉",file=discord.File("final.png"))
  await member.send(f"Ahlaa ahla {tag}, mara7bee bik fi darek 😍\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.facebook.com/cs.esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.instagram.com/ieee.cs.esprit/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.linkedin.com/company/cs-esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttp://computer-esprit.ieee.tn/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nTansanèch fi follow/like ken mech 3amel 👀🤣\nFINALLY, 3andek fekra mte3 event wela project? T7eb t7assenni ?\nMy Master {tagFozz} yestana fik 🤩🤩")
 

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

@client.command(pass_context=True)
async def help(ctx):
  embed = discord.Embed(
    colour = discord.Colour.orange()
  )
  embed.set_author(name="Help")
  embed.add_field(name="!ping",value="return pong",inline=False)
  await ctx.send(embed=embed)
  

@client.command(pass_context=True)
async def join(ctx):
  if not ctx.message.author.voice:
    await ctx.send('you are not connected to a voice channel')
    return

  else:
    voice_channel = ctx.author.voice.channel
  await voice_channel.connect()

    

@client.command(pass_context=True)
async def leave(ctx):
  voice_channel = ctx.author.guild.voice_client
  await voice_channel.disconnect()

@client.command(brief="Plays a single video, from a youtube URL")
async def play(ctx,url):
  #stream song
  server_id = ctx.message.guild.id
  YDL_OPTIONS = {'format': 'worstaudio/worst', 'noplaylist':'True',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '64',
        }]}

  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  if not ctx.message.author.voice:
    await ctx.send('Od5el l voice channel w taw nji nsarbik !')
    return
  else:
    voice_channel = ctx.author.voice.channel

  voice = await voice_channel.connect()
  if not voice.is_playing():
      with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)

      URL = info['formats'][0]['url']
      voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
      voice.is_playing()
  else:
      await ctx.send("Fema ghoneya temchi :v")
      return
  players[server_id] = voice
  
  while voice.is_playing() or voice.is_paused() :
    await asyncio.sleep(1)
  else:
    await voice.disconnect()

#download song
'''
  voice_channel = ctx.author.voice.channel
  voice = await voice_channel.connect() 
  YDL_OPTIONS = {
      'format': 'bestaudio',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
      'outtmpl': 'song.%(ext)s',
  }

  with YoutubeDL(YDL_OPTIONS) as ydl:
      ydl.download("URL", download=True)

  if not voice.is_playing():
      voice.play(FFmpegPCMAudio("song.mp3"))
      voice.is_playing()
      await ctx.send(f"Now playing {url}")
  else:
      await ctx.send("Already playing song")
      return 
'''

@client.command()
async def pause(ctx):
  id = ctx.message.guild.id
  players[id].pause()

@client.command()
async def resume(ctx):
  id = ctx.message.guild.id
  players[id].resume()

@client.command()
async def stop(ctx):
  id = ctx.message.guild.id
  players[id].stop()


'''@client.command()
async def welcome(ctx,user = None):
  if user == None:
    user=ctx.author
  welcome = Image.open("welcome.png")
  
  asset = ctx.author.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  #avatar= Image.open(data)
  # Open the input image as numpy array, convert to RGB
  img=Image.open(data).convert("RGB")
  npImage=np.array(img)
  h,w=img.size

  # Create same size alpha layer with circle
  alpha = Image.new('L', img.size,0)
  draw = ImageDraw.Draw(alpha)
  draw.pieslice([0,0,h,w],0,360,fill=255)

  # Convert alpha Image to numpy array
  npAlpha=np.array(alpha)

  # Add alpha layer to RGB
  npImage=np.dstack((npImage,npAlpha))

  # Save with alpha
  #Image.fromarray(npImage).save('result.png')
  avatarr = Image.fromarray(npImage)
  avatarr = avatarr.resize((74,74))
  welcome.paste(avatarr,(102,62))

  draw = ImageDraw.Draw(welcome)
  font = ImageFont.truetype("ARIAL.TTF",30)

  username = str(ctx.message.author)
  output = username.split("#",1)[0]
  W,H = 600,285
  w,h=draw.textsize(output)
  draw.text(((W-w)/2-180,(H-h)/2-120), output,(255,153,51), font=font) 
  #avatar = avatar.resize((74,74))
  #welcome.paste(avatar,(102,62))
  welcome.save("final.png")
  await ctx.send(file=discord.File("final.png"))
  #await ctx.send(file=discord.File("result.png"))
'''
@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    command = ctx.message.content
    message = command.split("!clear ",1)[1]
    await ctx.send(f"billehi kifeh tconverti -{message}- l int 🤨?")


@play.error
async def play_error(ctx, error):
  await ctx.send("Stana dawrek xD")





#THANK YOU https://uptimerobot.com/
keep_alive()

client.run(os.environ['TOKEN'])