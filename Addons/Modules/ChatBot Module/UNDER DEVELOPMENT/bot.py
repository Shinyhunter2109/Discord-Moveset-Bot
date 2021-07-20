import discord
from discord.ext import commands
from prsaw import RandomStuff

bot = commands.Bot(command_prefix=">")
rs = RandomStuff(async_mode = True)

Bot.event
async def on_message(message):
    if bot.user == message.author:
        return
    if message.channel.id == 0000000000:
        response = await rs.get_ai_response(message.content)
        await message.reply(response)

    await bot.process_commands(message)



TOKEN = "ENTER TOKEN HERE"
bot.run(TOKEN)