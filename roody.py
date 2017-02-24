# Roody Discord Bot | Rude Discord Bot
# Ported to Python by @gabedev

import bs4
import discord
import urllib.request
import asyncio

client = discord.Client()

def get_insult():
    sock = urllib.request.urlopen('http://www.pangloss.com/seidel/Shaker/')
    html = sock.read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for insult_str in soup.find_all('font'):
        insult = insult_str.get_text()
        insult = insult.replace('\n', '').replace('\r', '')
        return (insult)

@client.event
async def on_ready():
    print ('Logged on as: {0}'.format(client.user))
    await client.change_presence(game=discord.Game(name='Say "shakespeare-inv" for invite link'))

@client.event
async def on_message(message):
    if client.user.mention in message.content:
        await client.send_message(message.channel, '{0}, {1}'.format(message.author.mention, get_insult()))

    if "shakespeare-inv" in message.content:
        await client.send_message(message.author, 'Here is [thou] linkith to thy acceptance thy bastard: https://discordapp.com/oauth2/authorize?client_id=238261917796401152&scope=bot')


client.run('token')
