import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import time
import random

bot = commands.Bot(description="A supernatural bot!!", command_prefix="sb!",pm_help=True)

swear = ["Dont swear on my christian minecraft server!!", "I'll wash down that throat with soap!","You just sweared... Im gonna have to ask you to leave my sleepover",
         "You sweared.. That is unacceptable.My Mom will banish you from my house","Swear one more time and I'll snap crackle and pop your joints"]

@bot.event
async def on_ready():
    print("Supernatural bot is online")
    await bot.change_presence(game=discord.Game(name='sb!help'))
    while 1:
        channel = discord.Object(id='440124384623984641')
        await bot.send_message(channel,"!disboard bump")
        await asyncio.sleep(3600)
@bot.event
async def on_message(message):
    #we do not want the bot to repy to itself
    if message.author == bot.user:
        return    
        

@bot.event
async def on_member_join(member):
    userID = member.id
    channel = discord.Object(id='418177569347731457')
    await bot.send_message(channel, "Welcome to the best server in the world, <@%s>! Please make sure to read rules and submit your character to start roleplaying" % (userID))
@bot.event
async def on_member_remove(member):
    userID = member
    channel = discord.Object(id='418177569347731457')
    await bot.send_message(channel, "We're sorry to see you leave,**%s**!" % (userID))


@bot.command(pass_context=True)
async def echo(ctx,*, txt):
    """The bot will say whatever is after 'echo'"""
    if txt is None:
        await bot.say("You have not said anything")
    else:
        await bot.say(txt)
        await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def mute(ctx, user: discord.Member):
    userid = user.id
    server = ctx.message.server
    role = discord.utils.get(server.roles, name="Muted")
    await bot.add_roles(user, role)
    await bot.send_message(ctx.message.channel, "<@%s> has been muted" % (userid))
    await bot.send_message(ctx.message.channel, "User will have to get unmuted manually")

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def kick(ctx, user: discord.Member):
    userid = user.id
    if not user.id == "436553984501874699":
        await bot.send_message(ctx.message.channel, "<@%s> has been kicked" % (userid))
        await bot.kick(user)
 



bot.run("NDM2NTUzOTg0NTAxODc0Njk5.Dbp6sA.Br4uCdL6mEASySg9Tf1YDL4WxEA")
