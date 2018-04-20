import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import time
import random

bot = commands.Bot(description="A supernatural bot!!", command_prefix="#")
months = ["January","February","March","April","May","June","July","August",
          "September","October","November","December"]
swear = ["Dont swear on my christian minecraft server!!", "I'll wash down that throat with soap!","You just sweared... Im gonna have to ask you to leave my sleepover",
         "You sweared.. That is unacceptable.My Mom will banish you from my house","Swear one more time and I'll snap crackle and pop your joints"]

@bot.event
async def on_ready():
    print("Supernatural bot is online")
    await bot.change_presence(game=discord.Game(name='#help'))
    currday = 16
    currmonth = 11
    curryear = 2033
    while 1:
        date = currday,months[currmonth],curryear
        await bot.send_message(discord.Object(id='434435475705692160'), date)
        if currmonth == 11 and currday == 30:
            currday = 1
            currmonth = 0
            curryear = curryear + 1
        elif currday == 28 and currmonth == 1:
            currday = 1
            currmonth = 2
        elif currday != 30:
           currday = currday+1
        await asyncio.sleep(14400)

@bot.event
async def on_message(message):
    #we do not want the bot to repy to itself
    if message.author == bot.user:
        return
    if 'OOF' in message.content:
        emoji = get(bot.get_all_emojis(), name='OOF')
        await bot.add_reaction(message,emoji)
    if ':OOF:' in message.content:
        emoji = get(bot.get_all_emojis(), name='OOF')
        await bot.add_reaction(message,emoji)
    if 'fuck' in message.content:
        await bot.send_message(message.channel,"owo")
        await asyncio.sleep(3)
        await bot.send_message(message.channel,random.choice(swear))
    if 'FUCK' in message.content:
        await bot.send_message(message.channel,"owo")
        await asyncio.sleep(3)
        await bot.send_message(message.channel,random.choice(swear))
    if message.content.startswith('@everyone @everyone @everyone'):
        userID = message.author.id
        await client.send_message(message.channel,"<@%s> has been muted" % (userID))
        role = discord.utils.get(server.roles, name="Muted")
        await bot.add_roles(user, role)
    await bot.process_commands(message)        
        

@bot.event
async def on_member_join(member):
    userID = member.id
    channel = discord.Object(id='418177569347731457')
    await bot.send_message(channel, "Welcome to the best server in the best server in the world, <@%s>!" % (userID))
@bot.event
async def on_member_remove(member):
    userID = member.id
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

