#importing discord library and os library
import discord, os, asyncio, time, random
from itertools import cycle
from discord.ext import commands, tasks
from keep_running import keep_running
from List import player, cultivation_level, cultivation_stages, armor, weapons, pills



bot = commands.Bot(command_prefix='ah ', intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command('help')

bot_status = cycle(["You", "Cultivation Techniques", "Cultivation Realms", "Enlightenment", "Her"])

@tasks.loop(seconds = 180)
async def change_status():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=next(bot_status)))

@bot.event
async def on_ready():
  print("Bot awake!")
  change_status.start()

#=========================Data===========================#
level = 0
stage = 0
manual_level = 1
#=========================MENU==========================#
@bot.command()
async def menu(ctx):
  
    page1 = discord.Embed(title='Menu List',
                         description="These are the commands that you can use. The prefix for this bot is 'ah'",
                         colour=discord.Colour.blue())
     
    page1.set_thumbnail(
      url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
    )
    page1.set_footer(
      text="Made By Coldiny#5056",
      icon_url=
  'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
    )
    page1.set_author(
      name='Aegisheart',
      icon_url=
      'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
    )
    page1.add_field(name="Game", value="`Start` `Cultivate` `Explore` `Breakthrough` `Shop` `Market`", inline=False)
    #Shop is shop by the game. Market is player based shop.
    page1.add_field(name="Status", value="`Profile` `Realm` `Qi`", inline=False)
    page1.add_field(name="Manual", value="`Info`, `Upgrade`", inline=False)
    page1.add_field(name="Inventory", value="`Bag` `Use` `Equip`", inline=False)
    page1.add_field(name="Guild", value="`Sect` `Join <Sect_Name>` `Leave <Sect_Name>`", inline=False)
  
    pages = [page1]
  
    message = await ctx.send(embed = page1)
    await message.add_reaction('<:arrow_left:973097114856984577>')
    await message.add_reaction('<:arrow_right:973097084515393586>')
  
    def check(reaction, user):
        return user == ctx.author
  
    i = 0
    reaction = None
  
    while True:
        if str(reaction) == '':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '<:arrow_left:973097114856984577>':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '<:arrow_right:973097084515393586>':
            if i < 2:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '':
            i = 2
            await message.edit(embed = pages[i])
  
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break
  
    await message.clear_reactions()
  
#======================Commands=======================#

#======================Game Info======================#
@bot.command()
async def game(ctx):
    page1 = discord.Embed(title='Game',
                         description="These are the commands within 'Game'.",
                         colour=discord.Colour.blue())
     
    page1.set_thumbnail(
      url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
    )
    page1.set_footer(
      text="Made By Coldiny#5056",
      icon_url=
  'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
    )
    page1.set_author(
      name='Aegisheart',
      icon_url=
      'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
    )
    page1.add_field(name="Start", value="To start playing the game.", inline=False)
    page1.add_field(name="Cultivate", value="Gives you Qi per second.", inline=False)
    page1.add_field(name="Explore", value="You will explore and find things.", inline=False)
    page1.add_field(name="Breakthrough", value="When you Qi reaches max Qi, you can level up your realm.", inline=False)
    page1.add_field(name="Shop", value="It has pills for sale.", inline=False)
    page1.add_field(name="Market", value="Not available.", inline=False)
  
    pages = [page1]
  
    message = await ctx.send(embed = page1)

#======================Status Info========================#
@bot.command()
async def status(ctx):
    page1 = discord.Embed(title='Status',
                         description="These are the commands within 'Status'.",
                         colour=discord.Colour.blue())
     
    page1.set_thumbnail(
      url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
    )
    page1.set_footer(
      text="Made By Coldiny#5056",
      icon_url=
  'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
    )
    page1.set_author(
      name='Aegisheart',
      icon_url=
      'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
    )
    page1.add_field(name="Profile", value="You can see your status.", inline=False)
    page1.add_field(name="Realm", value="You can see what Realm you are in.", inline=False)
    page1.add_field(name="Qi", value="You can see how much Qi you need to reach your Max Qi.", inline=False)
  
    pages = [page1]
  
    message = await ctx.send(embed = page1)

#======================Manual Info========================#
@bot.command()
async def manual(ctx):
    page1 = discord.Embed(title='Manual',
                         description="These are the commands within 'Manual'.",
                         colour=discord.Colour.blue())
     
    page1.set_thumbnail(
      url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
    )
    page1.set_footer(
      text="Made By Coldiny#5056",
      icon_url=
  'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
    )
    page1.set_author(
      name='Aegisheart',
      icon_url=
      'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
    )
    page1.add_field(name="Info", value="Gives information of your Manual.", inline=False)
    page1.add_field(name="Upgrade", value="Upgrades the Manual.", inline=False)

    pages = [page1]
  
    message = await ctx.send(embed = page1)

#======================Inventory Info========================#
@bot.command()
async def inventory(ctx):
    page1 = discord.Embed(title='Inventory',
                         description="These are the commands within 'Inventory'.",
                         colour=discord.Colour.blue())
     
    page1.set_thumbnail(
      url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
    )
    page1.set_footer(
      text="Made By Coldiny#5056",
      icon_url=
  'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
    )
    page1.set_author(
      name='Aegisheart',
      icon_url=
      'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
    )
    page1.add_field(name="Bag", value="Opens up your inventory.", inline=False)
    page1.add_field(name="Use <Item_Name>", value="Uses an item in your inventory.", inline=False)
    page1.add_field(name="Equip <Item_Name>", value="Equips an item in your inventory.", inline=False)
  
    pages = [page1]
  
    message = await ctx.send(embed = page1)

#======================Guild Info========================#
@bot.command()
async def guild(ctx):
    page1 = discord.Embed(title='Guild',
                         description="These are the commands within 'Guild'.",
                         colour=discord.Colour.blue())
     
    page1.set_thumbnail(
      url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
    )
    page1.set_footer(
      text="Made By Coldiny#5056",
      icon_url=
  'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
    )
    page1.set_author(
      name='Aegisheart',
      icon_url=
      'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
    )
    page1.add_field(name="Sect", value="Shows information of the sect your in.", inline=False)
    page1.add_field(name="Join <Sect_Name>", value="Used to join a sect.", inline=False)
    page1.add_field(name="Leave <Sect_Name>", value="Used to leave the sect.", inline=False)
  
    pages = [page1]
  
    message = await ctx.send(embed = page1)

#===================Start Command====================#
@bot.command()
async def start(ctx):
  await ctx.send("You have started your journey in the world of Cultivation!")

#==================Cultivate Command====================#
is_cultivating = False
cultivation_task = None
@bot.command()
async def cultivate(ctx):
    global is_cultivating, cultivation_task
    if is_cultivating:
        await ctx.send("Already cultivating! Can't start again.")
    else:
        is_cultivating = True
        await ctx.send("You have started cultivating!")
        cultivation_task = bot.loop.create_task(start_increasing_qi(player, ctx))

@bot.command()
async def stop(ctx):
    global is_cultivating, cultivation_task
    if is_cultivating and cultivation_task is not None:
        is_cultivating = False
        await ctx.send("You have stopped cultivating.")
        cultivation_task.cancel()
    else:
        await ctx.send("You are not currently cultivating.")

async def start_increasing_qi(player, ctx):
    while is_cultivating:
      player["Qi"] += player["Qi Gain Speed"]
      await ctx.send("You have gained " + str(player["Qi Gain Speed"]) + " Qi!")
      await asyncio.sleep(1)
#==================Explore Command====================#
@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command()
async def explore(ctx):
  things = ["an enemy", "pills", "items", "currency"]
  something = random.choice(things)
  await ctx.send(f"You have found ***{something}***!")
#something will be enemy, pills, items, currency

#==================Breakthrough Command====================#
@bot.command()
async def breakthrough(ctx):
  global level, stage
  
  if (int(player["Qi"]) >= int(player["Qi_Max"])):
    stage += 1
    await ctx.send("You are breaking through!")
    player["Qi"] = int(player["Qi"]) - int(player["Qi_Max"])
    add_qi = player["Qi_Max"] * 0.5
    player["Qi_Max"] = int(player["Qi_Max"]) + int(add_qi)
    if stage == 4:
      stage = 0
      level += 1
    await ctx.send("Level: " + str(level) + "\nStage: " + str(stage))
  else:
    await ctx.send("You don't have enough Qi!")
    
  c_level = cultivation_level[level]
  c_stage = cultivation_stages[stage]
  value = c_level + " - " + c_stage
  await ctx.send("You have reached " + value + "!")
    
#==================Shop Command====================#
@bot.command()
async def shop(ctx):
    thepills = random.choice(pills)
    thepills1 = random.choice(pills)
    thepills2 = random.choice(pills)
    thepills3 = random.choice(pills)
    thepills4 = random.choice(pills)
    thepills5 = random.choice(pills)
    page1 = discord.Embed(title='Shop',
                           description="Welcome to the Shop. What do you want to buy?",
                           colour=discord.Colour.blue())
       
    page1.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
    )
    page1.set_footer(
      text="Made By Coldiny#5056",
      icon_url=
  'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
    )
    page1.set_author(
      name='Aegisheart',
      icon_url=
      'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
    )
    page1.add_field(name=f"***{thepills}***", value="", inline=False)
    page1.add_field(name=f"***{thepills1}***", value="", inline=False)
    page1.add_field(name=f"***{thepills2}***", value="", inline=False)
    page1.add_field(name=f"***{thepills3}***", value="", inline=False)
    page1.add_field(name=f"***{thepills4}***", value="", inline=False)
    page1.add_field(name=f"***{thepills5}***", value="", inline=False)
  
    pages = [page1]
  
    message = await ctx.send(embed = page1)
  
#==================Market Command====================#
@bot.command()
async def market(ctx):
  await ctx.send("No market available! Please check back later.")
  
#==================Profile Command====================#
@bot.command()
async def profile(ctx):
  global level, stage, value
  c_level = cultivation_level[level]
  c_stage = cultivation_stages[stage]
  value = c_level + " - " + c_stage
  page1 = discord.Embed(title='Profile',
                       description="This is your profile.",
                       colour=discord.Colour.blue())
  page1.set_thumbnail(
    url='https://cdn.discordapp.com/attachments/1185455650650738810/1192837541527818331/9k.png?ex=65aa8787&is=65981287&hm=4dcce452ad4c05c5e1ac90563f7d2f7014e6eb76c7fb05f4c807b9288efe1069&'
  )
  page1.set_footer(
    text="Made By Coldiny#5056",
    icon_url=
'https://cdn.discordapp.com/avatars/437542797436911617/069650f06017ef78038e23934e79b101.png?size=4096'
  )
  page1.set_author(
    name='Aegisheart',
    icon_url=
    'https://cdn.discordapp.com/avatars/1192821473186939014/75ef6e4eb838636e5677b566fb90560b.png?size=4096'
  )
  page1.add_field(name=f"{ctx.author.name.capitalize()}", value = "", inline=False)
   
  page1.add_field(name="Realm", value=value, inline=False)

  page1.add_field(name="Equipment", value="Weapon \nArmor", inline=False) #More equipment to be added in the future
  page1.add_field(name="Qi", value=str(player["Qi"])+"/"+str(player["Qi_Max"]), inline=False)
  page1.add_field(name="Manual", value="<Rank 1>", inline=False) #The rank for manual can change
  page1.add_field(name="Inventory", value="`Inventory` `Use` `Equip`", inline=False)
  #page1.add_field(name="Sect", value=f"{Sect}", inline=False)
#Sect, define it, its sect name ok. This is basically a guild. so multiplayer option do later.
  pages = [page1]

  message = await ctx.send(embed = page1)
  await message.add_reaction('<:arrow_left:973097114856984577>')
  await message.add_reaction('<:arrow_right:973097084515393586>')

  def check(reaction, user):
      return user == ctx.author

  i = 0
  reaction = None

  while True:
      if str(reaction) == '':
          i = 0
          await message.edit(embed = pages[i])
      elif str(reaction) == '<:arrow_left:973097114856984577>':
          if i > 0:
              i -= 1
              await message.edit(embed = pages[i])
      elif str(reaction) == '<:arrow_right:973097084515393586>':
          if i < 2:
              i += 1
              await message.edit(embed = pages[i])
      elif str(reaction) == '':
          i = 2
          await message.edit(embed = pages[i])

      try:
          reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
          await message.remove_reaction(reaction, user)
      except:
          break

  await message.clear_reactions()

#==================Realm Command====================#
@bot.command()
async def realm(ctx):
  await ctx.send("Realm: " + value + ".")
#====================Qi Command=====================#
@bot.command()
async def qi(ctx):
  await ctx.send("Qi" + (str(player["Qi"]))+ "/" + (str(player["Qi_Max"])))
#==================Info Command====================#
@bot.command()
async def info(ctx):
  global manual_level
  await ctx.send("Your Manual is level: " + str(manual_level) + ".")
#==================Upgrade Command====================#
@bot.command()
async def upgrade(ctx):
  global manual_level
  #we need currency
#==================Bag Command====================#

#==================Use Command====================#

#==================Equip Command====================#

#==================Sect Command====================#

#==================Join Command====================#

#==================Leave Command====================#

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
      
    if bot.user.mentioned_in(message):
        await message.channel.send(f"Hello {message.author.mention}! My prefix is || ah || don't forget it now.")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("That is not a command. :angry_face:")
    
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.send(f'Your tired. Please rest for ***{error.retry_after:.0f}*** seconds before trying again.')

  
#Currency
spirit_stones = 0
coins = 0

keep_running()
bot.run(os.getenv("TOKEN"))