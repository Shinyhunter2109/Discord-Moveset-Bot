import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import datetime
from datetime import date
from datetime import datetime
import time
import asyncio
import random
import logging
import threading
import traceback



TOKEN = 'INSERT TOKEN HERE'

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='Giveaway.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = '!')
client.launch_time = datetime.utcnow()
status = cycle(['Discord Giveaways', 'Collecting Giveaways'])
ROLE = 'Your Role'

@client.event
async def on_ready():
    change_status.start()
    print('Logged in as: ' + client.user.name + '\n')
    print('This Module is made by twitch.tv/shinyhunter2109')
    print('Bot version: 1.2')


def is_it_me(ctx):
    return ctx.author.id == 'Insert IDs here'


@client.command()
@commands.check(is_it_me)
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 

    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} seconds from now!")

    my_msg = await ctx.send(embed = embed)

    await my_msg.add_reaction("🎁")

    await asyncio.sleep(mins)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"**Congratulations! {winner.mention} won {prize}!**")
    await ctx.send(f'**Please send a Dm to @Marcel#6089 or @lɐuɐʞdluoɯǝʞod#7795 to get your Prize**')



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**Invalid command used.**')


@client.event
async def on_permission_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**You dont have the right Permissions to execute this command.**')


@tasks.loop(seconds=360)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



@client.command()
async def GA_Help(ctx):
    await ctx.send(f'**It is very simple , just react to the message from the GA Bot and you are in !**')


@client.command()
async def GA_Prize(ctx):
    await ctx.send(f'**These are the following Prizes: 1 Free Sub Gift, Shoutout, 1 Month VIP Membership, Beta_Access**')



def is_it_me(ctx):
    return ctx.author.id == 'Insert ID here'


@client.command()
@commands.check(is_it_me)
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f'**{days}d, {hours}h, {minutes}m**')


@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason='No reason provided'):
    try:
        await member.send('**You have been kicked from the Shinyhunter2109 Discord! Reason:None | Join again: https://discord.gg/Hz2VvJa**')
    except:
        await ctx.send('**The Member has their dms closed.**')
    
    await member.kick(reason=reason)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason='No reason provided'):
    try:
        await member.send('**You have been banned from the Shinyhunter2109 Discord! Reason:None | RIP Better Luck next Time!**')
    except:
        await ctx.send('**The Member has their dms closed.**')
    
    await member.ban(reason=reason)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.has_permissions(manage_channels=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'**Channel Clear Successfully done!**')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def Poll(ctx,*, msg):
    channel = ctx.channel
    try:
        op1 , op2 = msg.splitt('or')
        txt = f'React with ✅ for {op1} or ❎ for {op2}'
    except:
        await channel.send('**Correct Syntax: [Choice1] or [Choice2]**')
    return


    embed = discord.Embed(title='Poll', description = txt,color = discord.Color.red())
    message_ = await channel.send(embed=embed)
    await message_.add_reaction('✅')
    await message_.add_reaction('❎')
    await ctx.message.delete()


@client.command()
async def GA_Ad(ctx):
    await ctx.message.delete()
    await ctx.send('**No Giveaway Ads allowed | Warning!**')


@client.command()
async def HCIW(ctx):
    await ctx.send(f'**React to the Message of the Giveaway Bot and wait till the Giveaway runs out !**')


@client.command()
async def Command_list(ctx):
    await ctx.send(f'**These are all usable commands at this time: [!GA-Ad],[!HCIW],[!poll],[!GA_Help],[!GA_Prize]**')



@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)
    print(f'{member} was given {role}')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')



client.run(TOKEN)