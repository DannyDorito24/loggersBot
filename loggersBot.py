import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")
password = os.getenv("PASSWORD")
passwordhint = os.getenv("PASSWORDHINT")
ip = os.getenv("IP")

intents = discord.Intents.default()
intents.messages = True

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='.', intents=intents)

whiskasfilenames = os.listdir("./whiskasimages/")
musicfilenames = os.listdir("./music/")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @client.event
# async def on_message(message):
#     print(message.content)
#         #1% chance of replying with :eyes:
#     if random.randint(1, 100) == 1:
#         await message.channel.send(':eyes:', reference=message) 

#     if message.author == client.user:
#         return

#     if message.content.startswith('.whiskas') and message.author.id == 720213566421991464:
#         await message.channel.send('Finish mowodmail x loggers first >:3')
        
#     if message.content.startswith('.whiskas') and message.author.id != 720213566421991464:
#         selectedfile = random.choice(whiskasfilenames)
#         path = os.path.join("./whiskasimages/", selectedfile)
#         await message.channel.send(file=discord.File(path))

#     if message.content.startswith('.dmatteridapictureofwhiskassoshedoesntexplodeinstantaneously'):
#         atterid = await client.fetch_user(720213566421991464)
#         selectedfile = random.choice(whiskasfilenames)
#         path = os.path.join("./whiskasimages/", selectedfile)
#         await atterid.send(path)

#     if message.content.startswith('.ping'):
#         await message.channel.send(f'Pong! {round(client.latency * 1000)}ms') 

#     if message.content.startswith('.tomathy') or message.content.startswith('.tom'):
#         await message.channel.send('Tom gae')

#     if message.content.startswith('.music'):
#         selectedfile = random.choice(musicfilenames)
#         path = os.path.join("./music/", selectedfile)
#         await message.channel.send("Here's some 'music' for you <:admiraaaaaaaAAAAAAAAAAAAAAAaaa:832752359624409159>", file=discord.File(path))

#     if message.content.startswith('e') and message.channel.id == 833723641359237121:
#         await message.channel.send('e')
    
#     if message.content.startswith('.cum'):
#         await message.channel.send('<a:cum:1290425739010773082>')

#     if message.content.startswith('.morbin'):
#         await message.channel.send('https://cdn.discordapp.com/attachments/833723641359237121/1290752006280970251/full-1.webm?ex=66fd99fb&is=66fc487b&hm=4695c9d8916d6956729e181b08f0e559440e68f756aba32efb179d868911ed88&')
   



#Read a current counter value from ./whiskascounter.txt and subtract the user's input number from it, then post the new value in the channel.
@bot.command()
async def eatwhiskas(ctx, arg):
    if arg.startswith("-"):
        await ctx.send("How the fuck do you think that's supposed to work. How would you eat negative whiskas. Stop it.")
        return
    WhiskasFile = open(r"./whiskascounter.txt","r")
    counter = WhiskasFile.read()
    counter = int(counter) - int(arg)
    newcounter = str(counter)
    if int(arg) > 100000:
        await ctx.send("You can't even fit that many in your mouth. Stop it now before you EXPLODE")
        return
    if counter == 0:
        await ctx.send("You eated " + arg + " whiskas. There are no whiskas left. What have you done.")
        WhiskasFile.close()
        WhiskasFile = open(r"./whiskascounter.txt","w")
        WhiskasFile.write(newcounter)
        WhiskasFile.close()
        return
    if counter < 0:
        await ctx.send("TOO MANY WHISKAS EATED. YOU CANNOT EAT MORE WHISKAS THAN THERE ARE. STOP.")
        return
    await ctx.send("You eated " + arg + " whiskas! There are now " + newcounter + " whiskas left :3")
    WhiskasFile.close()
    WhiskasFile = open(r"./whiskascounter.txt","w")
    WhiskasFile.write(newcounter)
    WhiskasFile.close()

@bot.command()
async def refillwhiskas(ctx, arg):
    if ctx.author.id != 381608421906186240:
        await ctx.send("You are not authorized to perform this action.")
        return
    if arg.startswith("-"):
        await ctx.send("How the fuck do you think that's supposed to work. How would you add negative whiskas. Stop it.")
        return
    WhiskasFile = open(r"./whiskascounter.txt","r")
    counter = WhiskasFile.read()
    counter = int(counter) + int(arg)
    newcounter = str(counter)
    await ctx.send("Whiskas refilled. There are now " + newcounter + " whiskas left :3")
    WhiskasFile.close()
    WhiskasFile = open(r"./whiskascounter.txt","w")
    WhiskasFile.write(newcounter)
    WhiskasFile.close()

@bot.command()
async def checkwhiskas(ctx):
    WhiskasFile = open(r"./whiskascounter.txt","r")
    counter = WhiskasFile.read()
    await ctx.send("There are " + counter + " whiskas left. Eat wisely.")
    WhiskasFile.close()

@bot.command()
async def unlock(ctx, arg):
    if arg == (password):
        await ctx.send("You have unlocked the vault of infinite whiskas. You may now refill the whiskas as you please. Congratulations. :3")
        return
    if arg.startswith(passwordhint):
        await ctx.send("You are not worthy to enter the vault. However. You are getting closer. You will get there soon.")
        return
    else:
        await ctx.send("You are not worthy to enter the vault.")
        return


bot.run(token)
