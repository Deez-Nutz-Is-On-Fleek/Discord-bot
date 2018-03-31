import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import json
import time
import random
from random import randrange
from discord.voice_client import VoiceClient

Client = discord.Client() #line 10
bot = commands.Bot(description="A Communist bot made by TheSilentAngel#3156", command_prefix ="s!")
chatFilter = ["CAPITALISM","CAPITALIST","TRUMP","CAPATALISM","GASTON","CAPITALISTS","OBAMA","GAST0N"]
bypassList = ['427870453357346826','427872312000249866']
prop = ["The USSR is almighty","The Might of Stalin will overtake the world","Capitalist swines shall be executed","We live for communism","Communism is the only way of life",":b:gone capitalist swine"]
iprop =["https://i.ytimg.com/vi/rwmkDufxrqc/maxresdefault.jpg","https://i.ytimg.com/vi/yCrYvHBMGLY/maxresdefault.jpg","https://i.ytimg.com/vi/jm4pVfLXKqk/maxresdefault.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh6ZL4G9Mq4YU0GFE1oRmclgfs-qRw6affVlS_qgZ7etbbGf-U",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLwQqjWyo9tgBjcyrEx1HTi4oCPnHjv5hamDipzseFhQlzCWBCBw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZQ_TCJxN_TWzNdKq0t-ivDnEvjzNyeZqWX-Cb4tTL1b5U3AoXRg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQusz71Sw8KstuejsSvDUR-iT-mdXeaok3U6PjHU49LbrabcYr8pQ",
        "http://www.infobaires24.com.ar/wp-content/uploads/2016/03/fidel.jpg"]
startup_extensions = ["Music"]
soviet_facts=["In 1954 Soviet prisoners overthrew their guards and, for 40 days, established a gulag republic with a democratically elected provisional government, marriages between male and female prisoners, indigenous religious ceremonies and a general flowering of art and culture.",
             "The USSR renamed its rocket base Baikonur in 1961 to keep the Soviet space program a secret. Residents of the original Baikonur, hundreds of km away, took advantage of the resulting confusion by ordering many valuable supplies for themselves before the scam was discovered.",
             "There is an unreleased experimental Russian film where nobody on set was allowed to admit they were part of a movie production. Everyone had to pretend they were living in the 50’s for three whole years. The entire set was even wired to reproduce the effect of living under the Soviet regime.",
             "There is a theme park in Lithuania that recreates life as a USSR citizen. Visitors have their belongings confiscated, wear gas masks, experience interrogation, and must learn the Soviet anthem. Their reward is a shot of vodka.",
             "A Soviet soccer player was so popular that when he was sent to the Siberian gulags during Stalin’s Great Purge in the 1930s, he was treated rather well as the gulag commanders were also his fans, who gave him better quarters and food rations, and was even asked to coach the local teams.",
             "The soviet military mapped the entire world with an extreme accuracy. They created more than 1 million maps and some are still used today. It remains one of the most ambitious cartography project till today.",
             "The term “Politically Correct” was originally used within the Communist Party in Stalinist Russia to describe which opinions on government were appropriate to hold and which were not.",
             "Nikita Khrushchev made a speech denouncing Stalin that was so shocking it caused heart attacks for some in attendance and others committed suicide afterwards",
             "During the Civil Rights Movement, the Soviet Union purposely inflamed racial tensions by mailing forged threats from the KKK to black neighborhoods.",
             "In the Soviet Union in 1991, voting “None of the Above” led to new elections with new candidates, eventually leading to the end of the Soviet Union.",
             "The USSR had a televised song contest. Since few people had phones, viewers would turn their house lights ON if they liked a certain song (OFF if they didn’t). The state energy company recorded the size of each power spike and reported the results to the station to determine points for each contestant.",
             "Fifty-five years ago today, astronaut Yuri Gagarin made history, when he got into Soviet Vostok 1 spaceship capsule and launched into space. Yuri Gagarin became the first human in space. Reports praised Gagarin for his perfect flight, but in fact he didn’t pilot the Vostok capsule. Psychologists working with the Soviet Space Program were worried that exposure to weightlessness would impact the pilot’s decision-making faculties. And so, the pilot was effectively locked out of controlling his capsule.",
             "In the mid-1980’s the Soviet KGB launched “Operation INFEKTION,” aimed at making people believe that the United States invented HIV.",
             "During a visit to Boeing, Soviet scientists secretly applied adhesive to the bottom of their shoes in order to covertly collect metal samples from the floor.",
             "Cosmonaut Sergei Krikalev was in space when the Soviet Union was dissolved. He went up a Soviet citizen and returned a Russian citizen.",
             "The Tsar Bomba, the single most physically powerful device ever used, had a mushroom cloud over 7 times the height of Everest. The shockwave circled the earth 3 times and caused windowpanes to be partially broken at distances of 900 km (560 mi). The original design was twice as large.",
             "A youth subculture from the late 1940s until the early 1960s in the Soviet Union used to dress like Americans in order to express their apolitical views, neutral or negative attitudes toward Soviet morality.",
             "A joint Nazi-Soviet military parade in Brest-Litovsk was held on September 22, 1939, to display the power of the newly formed Soviet-Nazi pact to the whole world.",
             "The Soviet Union and the United States were originally in talks to go to the moon together during the Cold War. Nikita Khruschev was poised to accept the plan but then President Kennedy was assassinated. The Soviets did not trust Vice President Johnson, so Khruschev rejected the plan.",
             "Raisa Gorbachev once told a British minister there were more than 300 ways to cook potatoes in the USSR. When he had doubts, she sent him a cookbook and a note: “My apologies for being somewhat inaccurate: in fact, there are five hundred, rather than three hundred, recipes to cook potatoes.”",
             "From 1929 to 1940, the Soviet Union introduced a 5-day week in a deliberate bid to eliminate religion.",
             "The Soviet Union attempted to domesticate moose for use in a cavalry.",
             "Only one Soviet male was awarded the “Mother Heroine Medal” (reserved for women who bore at least 10 children), because he adopted 12 children.",
             "During the 1968 invasion of Czechoslovakia by Warsaw Pact soldiers, road signs in towns were removed or painted over to confuse invading troops—except for those indicating the way to Moscow.",
             "In 1954 the USSR proposed a dam to the U.S. that would close off the Bering Straight. The Soviets claimed it would block arctic cold currents that flow down over Korea and the Sea of Japan, warming it as much as 30 degrees. The U.S. declined.",
             "The Soviet Union refused to host the 1980 Paralympics, stating that none of their citizens had disabilities.",
             "25 years ago, two million people joined their hands to form a human chain spanning over 600 kilometers (370 mi) across the three Baltic states in memory of the victims of the Soviet terror.",
             "In 1976, a Soviet pilot defected to Japan in his advanced MiG-25 fighter, which Russia demanded be returned. Japan complied, but only after allowing American engineers to examine the aircraft. Japan then shipped it back piece by piece, and billed Russia $40,000 in transport and labor costs.",
             "Before Chernobyl, the Soviets had another massive nuclear disaster which contaminated over 20,000 square km. The area was turned into a preserve to cover up the accident. The CIA knew of the accident, but also covered it up in order to protect the fledgling US nuclear industry from hysteria.",
             "The Soviet Union had a water computer created in 1928 that was used until the 1980s.",
             "The Soviet Union did not admit that a reactor had exploded at Chernobyl until nearly 3 days after radiation from the disaster set off alarms at a nuclear plant in Sweden 1000 km away.",
             "The practice of focusing on disasters elsewhere when one occurs in the Soviet Union was so common that after watching reports on Soviet television about a catastrophe abroad, Russians would call Western friends to find out whether something had happened in the Soviet Union.",
             "The Soviet Union allowed theaters to play The Grapes of Wrath movie because of its depiction of the plight of the poor under capitalism, but it was later withdrawn because Russian audiences were amazed that even the poorest Americans could afford a car.",
             "The US and the USSR’s only direct military confrontation happened in October 1944, over the Serbian town of Niš. It is considered top secret by both governments, and the exact number of casualties is unknown.",
             "In 1933 Soviet Russia dumped 6200 people on an island in Siberia and left them to their fate. A month later 4000 of them were dead.",
             "Stalin’s guards were so afraid of him that no one called a doctor until 12 hours after he had a stroke. They feared he might recover and execute anyone who had acted outside of his orders.",
             "During the Cold War, the USSR was able to tell a Soviet passport was a forgery because the staples in real passports would corrode due to the poor quality of metal.",
             "The Soviet Union under Lenin and Trotsky was the world’s first country that decriminalized homosexuality and abortion. Stalin, however, recriminalised homosexuality in 1933 and abortion in 1936.",
             "During WW2 one Russian pilot was shot down by Germans and dragged himself 18 days to Soviet controlled territory. After having his legs amputated, he learned how to fly with prosthetics, returned to flying combat missions and shot down 7 more German planes. He also lived to be 84 (died literally an hour before his 85 birthday party), received Golden Star of the Hero of the Soviet Union, got a PhD in History, also served in the supreme soviet which was a legislative body for the USSR.",
             "In 1956 Soviets proposed a joint project to build a dam across Bering Strait in order to warm the Arctic Ocean but it wasn’t found practicable by the US.",
             "In Holland’s embassy in Moscow, two Siamese cats kept meowing and clawing at the walls of the building. Their owners finally investigated, thinking they would find mice. Instead, they discovered microphones hidden by Russian spies.",
             "Eighty percent of Soviet males born in 1923 died in WWII.",
             "The Soviet Tu4 was a reversed-engineered copy of the US B29 bomber. Copied to such detail that every Tu4 had a rivet hole in one wing exactly where an unknown Boeing engineer mistakenly drilled it in the B29 used as a template.",
             "In 1936, the Russians made a computer that ran on water.",
             "The Soviet Tsar Bomba was so powerful it shattered windows 900 km away.",
             "George Koval, Soviet master spy, infiltrated the Manhattan project, stole nearly all of our nuclear secrets, single-handedly provided the key technology for Russia’s nuclear arsenal, and was only discovered as a spy in 2002.",
             "Between 1975-1982, USSR had six probes land on the surface of Venus, surviving temperatures of 855 °F and successfully taking photos."]







#line 20
@bot.event
async def on_ready():
    print("Bot is online")
    loop = True
    if loop == True:
        await bot.change_presence(game=discord.Game(name='s!help'))
        time.sleep(5)
        await bot.change_presence(game=discord.Game(name='https://discord.gg/dSWtGDh for help'))
        time.sleep(5)
        await bot.change_presence(game=discord.Game(name='Work for the Motherland'))
        time.sleep(5)



    

@bot.command()
async def ping():
    """If you say Ping then the bot will reply with pong"""
    await bot.say("Pong!")
#line 30
@bot.command(pass_context=True)
async def echo(ctx,*, txt):
    """The bot will say whatever is after 'echo'"""
    if txt is None:
        await bot.say("You have not said anything")
    else:
        await bot.delete_message(ctx.message)
        await bot.say(txt)

@bot.group(pass_context=True)
async def role(ctx): #line 40
    if ctx.invoked_subcommand is None:
        await bot.say(ctx.message.channel, "Please invoke a subcommand or Papa Stalin will get mad with the spam")

@role.command(name="give")
async def role_give(name):
    await bot.send_message(ctx, "This command is currently WIP")

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def gulag(ctx, user: discord.Member, secs):#line 50
    userid = user.id
    if not userid == "427894615505371138":
        server = ctx.message.server
        role = discord.utils.get(server.roles, name="Gulag Prisoners")
        await bot.add_roles(user, role)
        await bot.send_message(discord.Object(id='428267559742341120'), "<@%s> has been sent to gulag" % (userid))
    else:
        await bot.send_message("Dont send me to gulag u capitalist")

    
@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def megagulag(ctx, user: discord.Member):
    userid = user.id
    if not user.id == "427894615505371138":
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
    await bot.say(embed=em.set_image(url=iprop[random]))

@bot.command()
async def fact_sender():
    channel = discord.Object(id='429448868426416168')
    if 1:
        await bot.send_message(channel, random.choice(soviet_facts))
        await asyncio.sleep(84600)


    
for extension in startup_extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        exe = '(): ()'.format(type(e).__name__, e)
        print('Failed to load extension C:\n()'.format(extension, exe))

           
bot.run("NDI3ODk0NjE1NTA1MzcxMTM4.DaCL5Q.rPfTQv7-osD8NateQ5wyxTAxMH8")
