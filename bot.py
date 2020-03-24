import os
import discord
from discord import Game
import lqtgenerator

TOKEN = os.environ['LUQUITO_BOT']

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == '!frasetts':
        msg = lqtgenerator.gera_frase()
        await message.channel.send(tts=True, content=msg)

    if message.content == '!frase':
        msg = lqtgenerator.gera_frase()
        await message.channel.send(msg)

    if message.content == '!jogo':
        s = lqtgenerator.gera_jogo()
        await client.change_presence(activity=Game(name=s))


@client.event
async def on_ready():
    s = lqtgenerator.gera_jogo()
    await client.change_presence(activity=Game(name=s))
    print("Logged in as " + client.user.name)

client.run(TOKEN)
