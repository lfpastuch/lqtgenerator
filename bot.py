import os
import discord
from discord import Game
import lqtgenerator

TOKEN = os.environ['LUQUITO_BOT']

client = discord.Client()


@client.event
async def clear(channel):
    messages = []
    async for message in channel.history(limit=100):
        if message.author == client.user:
            messages.append(message)
        if message.content == '!frasetts':
            messages.append(message)

        if message.content == '!frase':
            messages.append(message)

        if message.content == '!jogo':
            messages.append(message)

        if message.content == '!clear':
            messages.append(message)

    await channel.delete_messages(messages)


@client.event
async def on_message(message):
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

    if message.content == '!clear':
        await clear(message.channel)


@client.event
async def on_ready():
    s = lqtgenerator.gera_jogo()
    await client.change_presence(activity=Game(name=s))
    print("Logged in as " + client.user.name)

client.run(TOKEN)
