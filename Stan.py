import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if "Squawk!" not in message.content:
        if message.content.startswith('!count'):# Counts the number of messages in the channel (???)
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        elif message.content.startswith('!sleep'):#Puts the bot to sleep for 5 seconds
            await asyncio.sleep(5)
            await client.send_message(message.channel, 'Done sleeping')

        #Zane's shitty code:
        elif message.content.startswith("!help"):
            helpmessage = "Hi! I'm Stan the parrot, these are all the things I can do:\n" \
                          "----------------------------------------------------------------\n" \
                          "!help   -  I tell you all the neat things that I can do\n" \
                          "!count  -  I count the number of messages in this channel\n" \
                          "!sleep  -  I take a nap for 5 seconds\n\n" \
                          "And watch your mouth! I don't like swears!\n\nSquawk!"
            await client.send_message(message.channel, helpmessage)

        try:
            await client.send_message(message.channel, await swear_check(message))
        except Exception: #if the swear check returns a None then the message send will crash
            print("no swear found")

async def swear_check(message): #Checks the message it was passed to see if it has any swears, returns a scolding message
    swears = ["fuck", "fucker", "shit", "bitch", "cunt"] #This could be expanded

    swearfound = False
    for swear in swears:
        if swear in message.content:
            swearfound = True

    if swearfound:
        return "Hey! Don't fucking swear! Squawk!"
    else:
        return None


#This client token is specific to Stan, do not change it

#******************THIS MUST BE REMOVED BEFORE PUSHING TO GITHUB*******************************
client.run('MjcxMTM4NTM2NjE3NDEwNTcw.C2CFBg.dUW3sB2dJZm2vaOp4CaTAfpKJew')
