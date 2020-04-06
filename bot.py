import os
import discord
from discord import Game
import discord.ext
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import lqtgenerator

TOKEN = os.environ['LUQUITO_BOT']

bot = commands.Bot(command_prefix='!')


def check_message(m):
    if m.author == bot.user:
        return True

    if m.content == '!frasetts':
        return True

    if m.content == '!frase':
        return True

    if m.content == '!jogo':
        return True

    if m.content == '!clear':
        return True

    return False


@bot.command(name='clear')
@has_permissions(manage_channels=True)
async def clear(ctx):
    await ctx.channel.purge(limit=100, check=check_message)


@clear.error
async def clear_error(ctx, error):
    text = 'Sem permissão, irmão'
    await ctx.send(text)


@bot.command(name='frase')
async def frase(ctx):
    msg = lqtgenerator.gera_frase()
    await ctx.send(msg)


@bot.command(name='frasetts')
async def frasetts(ctx):
    msg = lqtgenerator.gera_frase()
    await ctx.send(content=msg, tts=True)

bot.run(TOKEN)
