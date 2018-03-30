import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from random import randrange
from discord.voice_client import VoiceClient

Client = discord.Client()
client = commands.Bot(command_prefix ="!")
chatFilter = ["CAPITALISM","CAPITALIST","TRUMP","CAPATALISM","GASTON","CAPITALISTS","OBAMA","GAST0N"]
bypassList = ['427870453357346826','427872312000249866']
startup_extensions = ["Music"]


@client.event
async def on_ready():
    client.remove_command('help')
    print("Bot is ready!")
    blo = '1'
    if blo == '1':
        await client.change_presence(game=discord.Game(name='!help'))
        time.sleep(5)
        await client.change_presence(game=discord.Game(name='!help at discord.gg/dSWtGDh'))
        
class Main_Commands():
    def __init__(self,client):
        self.client = client


@client.event
async def on_message(message):
    prop = ["Communism shall prevail!!!",":b:GONE CAPITALIST SWINE","Capitalism shall fall","The USSR shall overtake the world","Communism the greatest","The Capitalist scum will be shot down by the might of the Soviet Union"]
    await client.process_commands(message)
    if message.content.startswith('Capitalist'):
        await client.send_message(message.channel, "All capitalist swine will be exterminated")
    if message.content.upper().startswith('!PROPAGANDA'):
        userID = message.author.id
        await client.send_message(message.channel,random.choice(prop))
    if message.content.upper().startswith('CAPITAL1SM IS THE WORST'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> I agree  " % (userID))
    if message.content.upper().startswith('!FGULAG'):
        if "427870453357346826" in [role.id for role in message.author.roles]:
            mentionID = message.mentions[0].id
            await client.delete_message(message)
            await client.send_message(message.channel, "**<@%s> Get sent to gulag!!!**" % (mentionID))
            time.sleep(2)
            await client.send_message(message.channel, "lol jk :joy::ok_hand:")
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Don't try to use that command or you'll get sent to gulag too!!" % (userID))


    if message.content.upper().startswith('!GULAG'):
        if "427870453357346826" in [role.id for role in message.author.roles]:
            example = discord.utils.get(message.server.roles,name='People in gulag')
            mentionID = message.mentions[0].id
            await client.delete_message(message)
            if not mentionID == '<@428932240416964619>':
                await client.send_message(message.channel, "**<@%s> Get sent to gulag!!!**" % (mentionID))
                await client.add_roles(message.mentions[0], example)
                await client.send_message(discord.Object(id='428267559742341120'), '<@%s> has been sent to gulag' % (mentionID))
                await client.send_message(message.channel, "https://ih0.redbubble.net/image.5327275.6170/sticker,375x360-bg,ffffff.png")
            else:
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Why you wanna send a faithful communist to gulag?" % (userID))


    if message.content.startswith('Added National Anthem of USSR to the queue.'):
        await client.send_message(message.channel, "@everyone **JOIN THE NATION ANTHEM :USSR:**") 
    if message.content.startswith('!mod'):
        await client.send_message(message.channel, "user isnt at least 7 days old")
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chatFilter:
            if not "427870453357346826"  in [role.id for role in message.author.roles]:
                userID = message.author.id
                await client.delete_message(message)
                msgSent = await client.send_message(message.channel,"**<@%s> DO NOT MENTION ALL THAT CAPITAL1ST SWINE ON THIS COMMUNIST SERVER**" % (userID))
                time.sleep(5)
                await client.delete_message(msgSent)



if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exe = '(): ()'.format(type(e).__name__, e)
            print('Failed to load extension C:\n()'.format(extension, exe))
            
client.run("NDI3ODk0NjE1NTA1MzcxMTM4.DZ7lvQ.bj_Gg_4TaWWuddZ2gGb-yHf3jYU")
