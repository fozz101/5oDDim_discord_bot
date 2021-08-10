import discord
import os
import asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from PIL import Image, ImageDraw,ImageFont
from io import BytesIO
import numpy as np
from youtubesearchpython import VideosSearch
import asyncpraw
import random
from keep_alive import keep_alive
from DriveAPI import fetchData
import requests
import json

from replit import db


intents = discord.Intents.default()
intents.members = True


client = commands.Bot(intents=intents,command_prefix = '!')
client.remove_command("help")

reddit = asyncpraw.Reddit(client_id = os.environ['client_id'],
client_secret = os.environ['client_secret'],
username= os.environ['username'],
password=os.environ['password'],
user_agent="bot")


authorised_channel_id_memes=[868903933031104572,870324693494804571,835817984593100840,867890807759831060,870338494923440148,870404449699528714,873297121548337152]

authorised_channel_id_music= [867880055182589975,868903933031104572,835817984593100840,870338494923440148,870404449699528714,873297121548337152]
welcome_channel = 868902567705456661

players = {}

async def placement_error(ctx):
  await ctx.send("Sè7bi barra ekteb el command hedhi fi 5oddim-cmd🤬")
  messages = await ctx.history(limit=2).flatten()
  await asyncio.sleep(3)
  await ctx.message.channel.delete_messages(messages)

async def placement_error_meme(ctx):
  await ctx.send("Sè7bi barra ekteb el command hedhi fi memes | 5oddim-cmd🤬")
  messages = await ctx.history(limit=2).flatten()
  await asyncio.sleep(3)
  await ctx.message.channel.delete_messages(messages)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) 
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to my master Fozz"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send("Mnin jebt'ha el command hedhi😅? Type !help to have all the available commands 📑")
      return
    raise error



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
  #Select welcome channel !
  channel = client.get_channel(welcome_channel)
  
  await channel.send(f"Yooo {tag}, mara7bee biik fi discord el CS !  😎🎉. Ekteb !help bech ta3ref chnewa enajem nsarbik 7aliyan.",file=discord.File("final.png"))
  await member.send(f"Ahlaa ahla {tag}, mara7bee bik fi darek 😍\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.facebook.com/cs.esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.instagram.com/cs.esprit/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.linkedin.com/company/cs-esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttp://computer-esprit.ieee.tn/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nTansanèch fi follow/like ken mech 3amel 👀🤣\nFINALLY, 3andek fekra mte3 event wela project? T7eb t7assenni ?\nMy Master Fozz yestana fik 🤩🤩")
 

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
  '''if message.content.startswith('test'):
    await message.channel.send(f"mara7beee {tag}  ")
    
    #await channel.send("ahlaaa")
    await usr.send(f"Ahlaa ahla {tag}, mara7bee bik fi darek 😍 \n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.facebook.com/cs.esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.instagram.com/cs.esprit/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttps://www.linkedin.com/company/cs-esprit\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nhttp://computer-esprit.ieee.tn/\n●▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬●\nTansanèch fi follow/like ken mech 3amel 👀🤣\nFINALLY, 3andek fekra mte3 event wela project? T7eb t7assenni ?\nMy Master {tagFozz} yestana fik 🤩🤩")
'''
  #log channel
  log = client.get_channel(869462857492856883)
  if not message.guild:
    await log.send(f"{tag}: {message.content}")

  await client.process_commands(message)


'''
@client.command()
async def ping(ctx):
  await ctx.send('Pong!')
'''
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
    title= "Bot commands",
    description="Hedhoum el available commands 7aliyan^^",
    colour = discord.Colour.orange()
  )
  embed.set_image(url = "https://cdn.discordapp.com/attachments/867880055182589975/870346399525535754/img.png")
  #embed.set_author(name="Hedhoum el available commands 7aliyan^^")
  embed.add_field(name="!meme",value="nsarbik meme men subreddit, tnajem ta5tar esm el subreddit, default subreddit heya ProgrammerHumor\n Usage: !meme || !meme esmSubreddit",inline=False)
  embed.add_field(name="!play",value="n5adem ghna, het esm el gho,aya | link youtube w taw nsarbik\n Usage: !play esmGhonaya || !play linkGhonayaFromYoutube ",inline=False)
  embed.add_field(name="!pause",value="npausi laghneya",inline=False)
  embed.add_field(name="!resume",value="nraja3lek laghneya",inline=False)
  embed.add_field(name="!stop",value="n7abes laghneya w n5alik wa7dek",inline=False)
  embed.add_field(name="!leave",value="n5alik wa7dek",inline=False)
  embed.add_field(name="!clear",value="nfassa5 el chat, mech ay wa7ed enajem yesta3mel el command hedhi :v",inline=False)
  await ctx.send(embed=embed)
  
'''
@client.command(pass_context=True)
async def join(ctx):
  if not ctx.message.author.voice:
    await ctx.send('you are not connected to a voice channel')
    return

  else:
    voice_channel = ctx.author.voice.channel
  await voice_channel.connect()

 '''   

@client.command(pass_context=True)
async def leave(ctx):
  if ctx.channel.id in authorised_channel_id_music:
    voice_channel = ctx.author.guild.voice_client
    await voice_channel.disconnect()
  else : 
    await placement_error(ctx)

@client.command(brief="Plays a single video, from a youtube URL")
async def play(ctx,*url):
  if ctx.channel.id in authorised_channel_id_music:
    output=""
    for word in url:
      output+=word+" "

    videoReq = output.split("&",1)[0]
    videoSearch = VideosSearch(videoReq, limit = 1,language = 'en', region = 'TN' ) 
    finalLink = videoSearch.result()['result'][0]['link']

    title = videoSearch.result()['result'][0]['title']
    thumbnail_url = videoSearch.result()['result'][0]['thumbnails'][0]['url']

    embed = discord.Embed (title=title)
    embed.set_image(url=thumbnail_url)
  
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
        await ctx.send(embed=embed)
        with YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(finalLink, download=False)

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
  else:
    await placement_error(ctx)


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
  if ctx.channel.id in authorised_channel_id_music:
    id = ctx.message.guild.id
    players[id].pause()
  else:
    await placement_error(ctx)

@client.command()
async def resume(ctx):
  if ctx.channel.id in authorised_channel_id_music:
    id = ctx.message.guild.id
    players[id].resume()
  else:
    await placement_error(ctx)

@client.command()
async def stop(ctx):
  if ctx.channel.id in authorised_channel_id_music:
    id = ctx.message.guild.id
    players[id].stop()
  else:
    await placement_error(ctx)


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


@client.command()
async def meme(ctx,subredditName="ProgrammerHumor"):
  if ctx.channel.id in authorised_channel_id_memes:
    #Select meme channel !
    channel = client.get_channel(870323326587912273)
    subreddit = await reddit.subreddit(subredditName,fetch=True)
    all_submissions=[]
    async for submission in subreddit.top("all"):
      if "https://i.redd" in submission.url : 
        all_submissions.append(submission)
      else:
        pass
    
    random_submission = random.choice(all_submissions)
    name = random_submission.title
    url = random_submission.url

    embed = discord.Embed (title=name)
    embed.set_image (url = url)
    await ctx.send(embed = embed)
  else : 
    await placement_error_meme(ctx)


@client.command()
async def jaweb(ctx,id,*args):

  member = await client.fetch_user(id)

  output=""
  for word in args:
    output+=word + " "
  await member.send(output)

@client.command()
async def fetchDrive(ctx):
  tagRoleDev = "<@&"+str(871744335849340959)+">"
  FOLDER_ID = '1K865vIqaeVnbKmcNnnGEmFcf0ufUN09b'
  filesList = await fetchData(FOLDER_ID)
  embed = discord.Embed(
    title= "Meetings Recordings",
    description="These are the recordings in the drive folder !",
    colour= discord.Colour.blue()
  )
  for file in filesList:
    embed.add_field(name=file['name'],value = "https://drive.google.com/file/d/"+file['id'],inline=False)

  await ctx.send(tagRoleDev,embed=embed)





@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    command = ctx.message.content
    message = command.split("!clear ",1)[1]
    await ctx.send(f"billehi kifeh tconverti -{message}- l int 🤨?")
  
@meme.error
async def meme_error(ctx, error):
  if isinstance(error, commands.errors.CommandInvokeError):
    await ctx.send("Mnin jebt'ha el subreddit hedhi? xD")

@play.error
async def play_error(ctx, error):
  await ctx.send("Stana dawrek xD")
  





#THANK YOU https://uptimerobot.com/
keep_alive()

client.run(os.environ['TOKEN'])