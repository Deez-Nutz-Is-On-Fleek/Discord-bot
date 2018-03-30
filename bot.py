import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from random import randrange
from discord.voice_client import VoiceClient

Client = discord.Client()
bot = commands.Bot(description="A Communist bot made by TheSilentAngel#3156", command_prefix ="s!")
chatFilter = ["CAPITALISM","CAPITALIST","TRUMP","CAPATALISM","GASTON","CAPITALISTS","OBAMA","GAST0N"]
bypassList = ['427870453357346826','427872312000249866']
startup_extensions = ["Music"]
prop = ["The USSR is almighty","The Might of Stalin will overtake the world","Capitalist swines shall be executed","We live for communism","Communism is the only way of life",":b:gone capitalist swine"]
iprop =["https://i.ytimg.com/vi/rwmkDufxrqc/maxresdefault.jpg","https://i.ytimg.com/vi/yCrYvHBMGLY/maxresdefault.jpg","https://i.ytimg.com/vi/jm4pVfLXKqk/maxresdefault.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh6ZL4G9Mq4YU0GFE1oRmclgfs-qRw6affVlS_qgZ7etbbGf-U","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLwQqjWyo9tgBjcyrEx1HTi4oCPnHjv5hamDipzseFhQlzCWBCBw",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZQ_TCJxN_TWzNdKq0t-ivDnEvjzNyeZqWX-Cb4tTL1b5U3AoXRg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQusz71Sw8KstuejsSvDUR-iT-mdXeaok3U6PjHU49LbrabcYr8pQ","http://www.infobaires24.com.ar/wp-content/uploads/2016/03/fidel.jpg"]

@bot.event
async def on_ready():
    print("Bot is online")
    await bot.change_presence(game=discord.Game(name='s!help||https://discord.gg/dSWtGDh'))

@bot.command()
async def ping():
    """If you say Ping then the bot will reply with pong"""
    await bot.say("Pong!")

@bot.command(pass_context=True)
async def echo(ctx,*, txt):
    """The bot will say whatever is after 'echo'"""
    if txt is None:
        await bot.say("You have not said anything")
    else:
        await bot.delete_message(ctx.message)
        await bot.say(txt)

@bot.group(pass_context=True)
async def role(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say(ctx.message.channel, "Please invoke a subcommand or Papa Stalin will get mad with the spam")

@role.command(name="give")
async def role_give(name):
    await bot.send_message(ctx, "This command is currently WIP")

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def megagulag(ctx, user: discord.Member):
    if not user == "Soviet Bot":
        userid = user.id
        await bot.send_message(discord.Object(id='428267559742341120'), "<@%s> has been mega gulagged" % (userid))
        await bot.kick(user)
    else:
        await bot.send_message(ctx.message.channel, "Dont ya try to mega gulag me!!")

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def ultragulag(ctx, user: discord.Member):
    userid = user.id
    await bot.send_message(discord.Object(id='428267559742341120'), "<@%s> has been ultra gulagged" % (userid))
    await bot.ban(user, delete_message_days=7)
    
@bot.command()
async def stalin():
    """The saviour of the motherland is shown"""
    em = discord.Embed(title="Papa Stalin",description="Stalin ze best",colour=discord.Colour.red())
    await bot.say(embed=em.set_image(url="https://vignette.wikia.nocookie.net/hitlerrantsparodies/images/3/30/Stalin_08.jpg/revision/latest?cb=20140905235500"))

@bot.command()
async def castro():
    """Fidel Castro, the saviour of Cuba"""
    em = discord.Embed(title="Fidel Castro",description="Castro is number 2",colour=discord.Colour.dark_blue())
    await bot.say(embed = em.set_image(url="https://amedia.britannica.com/700x450/75/44175-004-1AA92245.jpg"))

@bot.command()
async def che():
    """Fidel Castro's right hand man"""
    em = discord.Embed(title="Che Guevara",description="Che is a true leader",colour=discord.Colour.dark_green())
    await bot.say(embed = em.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/CheHigh.jpg/225px-CheHigh.jpg"))

@bot.command()
async def chavez():
    """Former President of commie Venezuela"""
    em = discord.Embed(title="Hugo Chavez",description="President of Venezuela. RIP",colour=discord.Colour.dark_gold())
    await bot.say(embed = em.set_image(url="https://i.ytimg.com/vi/pJd0apzjFus/maxresdefault.jpg"))
  
@bot.command()
async def propaganda():
    """Sends a random propaganda message"""
    random = randrange(0,len(prop))                           
    await bot.say(prop[random])
 
@bot.command()
async def ipropaganda():
    """Sends a random propaganda image"""
    random = randrange(0,len(iprop))
    em = discord.Embed(title="Communist propaganda",description="Best type of propaganda there is",colour=discord.Colour.red())
    await bot.say(embed=em.set_image(url=(prop[random]))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exe = '(): ()'.format(type(e).__name__, e)
            print('Failed to load extension C:\n()'.format(extension, exe))
            
         
bot.run("NDI3ODk0NjE1NTA1MzcxMTM4.DZ7lvQ.bj_Gg_4TaWWuddZ2gGb-yHf3jYU")
