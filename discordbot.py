import discord
import random
import datetime

random.seed(datetime.datetime.now())

TOKEN = 'XXXXX'

client = discord.Client()

def is_pop(user):
        return user.name == "Prophet" and user.discriminator == "3661"

def is_sam(user):
        return user.name == "Spar" and user.discriminator == "4145"

forceproc = False

@client.event
async def on_message(message):
        # we do not want the bot to reply to itself
        # print("message sent by user id: " + message.author.id)

        global forceproc

        messagelist = ['fk u spar!!', 'r u even drunk..', 'u shut ur mouf pat']

        if message.author == client.user:
                return
        luck = random.randint(0,99)
        print("luck: " + str(luck))
        if (forceproc or (luck == 2)):
                #if (is_sam(message.author) or is_pop(message.author)):
                msg = random.choice(messagelist).format(message)
                await client.send_message(message.channel, msg)

        forceproc = False
        if message.content.startswith('!proc'):
                forceproc = True
#       if message.content.startswith('!hello'):
#               msg = 'Hello {0.author.mention}'.format(message)
#               await client.send_message(message.channel, msg)

@client.event
async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

client.run(TOKEN, bot=True, reconnect=True)
