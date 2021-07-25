import discord
import asyncio
import logging
import async_timeout
import asyncore
import traceback
from discord.ext import commands

TOKEN = 'Set Token Here'
bot = commands.Bot(command_prefix='!')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    bot.load_extension('cogs.leveling')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**Invalid command used.**')


bot.run(TOKEN)
