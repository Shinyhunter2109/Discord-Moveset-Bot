import discord
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
import random
import asyncio
import json
import numpy
import async_timeout
import asyncore
import math
import threading
import logging
import time
import typing
import traceback
from datetime import datetime
from github import Github
from discord.voice_client import VoiceClient
from discord.ext import commands, tasks
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import Spotify
import youtube_dl
from youtube_dl import YoutubeDL
import os
from os import system
from itertools import cycle

TOKEN = 'INSERT YOUR TOKEN HERE...'

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')
status = cycle(['Shiny Pokémon Linktrades', 'GTS Moveset Help'])
ROLE = 'INSERT ROLES HERE...'


@client.event
async def on_ready():
    change_status.start()
    print('Logged in as: ' + client.user.name + '\n')
    print('This Bot is Made by twitch.tv/shinyhunter2109')
    print('Bot version: 4.1.1')
    print('You are on the Latest Version')


@client.event
async def on_error(event, *args, kwargs):
    message = args[0]
    logging.warning(traceback.format_exc())
    await client.send_message(message.channel, "You caused an error!")
    print ('an error has occurred..!')


class JoinDistance:
    def __init__(self, joined, created):
        self.joined = joined
        self.created = created

    @classmethod
    async def convert(cls, ctx, argument):
        member = await commands.MemberConverter().convert(ctx, argument)
        return cls(member.joined_at, member.created_at)

    @property
    def delta(self):
        return self.joined - self.created


@client.command()
async def delta(ctx, *, member: JoinDistance):
    is_new = member.delta.days < 100
    if is_new:
        await ctx.send("Hey you're pretty new!")
    else:
        await ctx.send("Hm you're not so new.")


class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!


@client.command()
async def roles(ctx, *, member: MemberRoles):
    """Tells you a member's roles."""
    await ctx.send('I see the following roles: ' + ', '.join(member))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**Invalid command used.**')


@client.event
async def on_permission_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**You dont have the right Permissions to execute this command.**')


@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))


class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)


@client.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)


def is_it_me(ctx):
    return ctx.author.id == 'INSERT ID HERE'


@client.command()
@commands.check(is_it_me)
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f'**{days}d, {hours}h, {minutes}m**')


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='help')
    embed.add_field(name='.ping', value='Returns Pong!', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def coinhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='coinhelp')
    embed.add_field(name='.coinflip', value='Return Heads/Tails', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def joinhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='joinhelp')
    embed.add_field(name='.join', value='Tells if joining from Bot was Successful', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def pokehelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='pokehelp')
    embed.add_field(name='.pokemonname', value='Returns Info & Picture', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def bottlehelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='bottlehelp')
    embed.add_field(name='.bottles', value='Returns [Value of Beer]', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def spotifyhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='spotifyhelp')
    embed.add_field(name='.spotify', value='Returns listening Activity from the User', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def eightballhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='eightballhelp')
    embed.add_field(name='.8ball', value='Returns one of the pre Messages for your Question', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def musichelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='musichelp')
    embed.add_field(name='.play', value='Returns the music that user has requested', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def kickhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='kickhelp')
    embed.add_field(name='.kick', value='Kicks the User from the Discord-Server', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def banhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='banhelp')
    embed.add_field(name='.ban', value='Bans the User from the Discord-Server', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def blackjackhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='blackjackhelp')
    embed.add_field(name='.blackjack', value='Return either [You Won | You Lost | Tied]', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def unbanhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='unbanhelp')
    embed.add_field(name='.unban', value='unbans a specific user that got banned recently', inline=False)
    await ctx.send(author, embed=embed)


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def spotify(ctx, user: discord.Member=None):
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            await ctx.send(f'{user} is listening to {activity.title} by {activity.artist}') # Tells you to what someone is listening


@spotify.error
async def spotify_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error
        
        
@client.command() 
async def add(ctx, *nums):
    operation = " + ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@client.command() 
async def sub(ctx, *nums): 
    operation = " - ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@client.command() 
async def multiply(ctx, *nums): 
    operation = " * ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@client.command() 
async def divide(ctx, *nums): 
    operation = " / ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')


@client.command()
async def emoji(ctx, emoji: discord.PartialEmoji = None):
    if not emoji:
        await ctx.send('**You need to provide an emoji!**')
    else:
        await ctx.send(emoji.url)


@client.command()
async def backup(ctx):
    await ctx.send('**Currently In Development! | Error Code: 0830-5219-8607 |**')
    await ctx.send('**https://open.spotify.com/track/6R6on0ldJcSDfi2whJziJ1?si=NcphntXxRN67ht26nMYIjQ**')


@client.command()
async def sendembed(ctx):
    e = discord.Embed(title="Stack Overflow - Where Developers Learn, Share, & Build Careers",
                      url="https://stackoverflow.com",
                      description="Stack Overflow | The World’s Largest Online Community for Developers")
    e.set_thumbnail(url="https://i.imgur.com/ddx8Bpg.png")
    await ctx.send(embed=e)


@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
        print(f'The bot has joined {channel}')
        await ctx.send(f'Joined {channel}')
    else:
        print('Bot joined your Channel')
        voice = await channel.connect()


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'The bot has left {channel}')
        await ctx.send(f'Left {channel}')


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        
        return
    
    await ctx.send("Getting everything ready, playing audio soon")
    print("Someone wants to play music let me get that ready for them...")
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()


@client.command()
async def coinflip(ctx):
    choices = ['Heads', 'Tails']
    rancoin = random.choice(choices)
    await ctx.send(f'Coinflip has started...')
    await asyncio.sleep(5)
    await ctx.send(rancoin)


@client.command()
async def Ads(ctx, member : discord.Member, *, reason=None):
    await ctx.send('**NO ADVERTISEMENT ALLOWED | WARNING KICK INCOMING**')
    await asyncio.sleep(10)
    await member.kick(reason=reason)
    await ctx.send('**Press F to pay respect**')


@client.command()
async def guessinggame(ctx):
    number = random.randint(1,150)
    for i in range(1, 150):
        await ctx.send('**guess a number**')
        response = await client.wait_for('message')
        guess = int(response.content)
        if guess > number:
            await ctx.send('**bigger**')
        elif guess < number:
            await ctx.send('**smaller**')
        else:
            await ctx.send('**true**')


@client.command()
async def info(ctx, *, member: discord.Member):
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))


@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')


@tasks.loop(seconds=320)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def Switch(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('switch-talk')


@client.command()
async def Community(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('community-couch')


@client.command()
async def SSBU(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('smash-battles ')


@client.command()
async def spam(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('bot-spam')


@client.command()
async def trades(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('viewer-trades')


@client.command()
async def Youtube(ctx):
    guild = ctx.guild
    await guild.create_role(name="Youtuber")


@client.command()
async def YT(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Youtuber")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def FB(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Facebook")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def Facebook(ctx):
    guild = ctx.guild
    await guild.create_role(name="Facebook")


@client.command()
async def DB(ctx):
    guild = ctx.guild
    await guild.create_role(name="Discord-Bot")


@client.command()
async def DBot(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Discord-Bot")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def ST(ctx):
    guild = ctx.guild
    await guild.create_role(name="Sub-Trade")


@client.command()
async def STrade(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Sub-Trade")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def Mixer(ctx):
    guild = ctx.guild
    await guild.create_role(name="Mixer")


@client.command()
async def Stream(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Mixer")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def Admin(ctx):
    guild = ctx.guild
    await guild.create_role(name="Administrator")


@client.command()
async def Chef(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Administrator")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


@client.command()
async def Discord(ctx):
    await ctx.send('Come and checkout the Development of this Project')
    await ctx.send(f'https://discord.gg/T2deZV8')


@client.command()
async def dm(ctx):
    rand_num = (randint(1, 3))
    win_num = 1
    pm_channel = await ctx.author.create_dm()
    if win_num == rand_num:
        await pm_channel.send("You won!")
    else:
        await pm_channel.send("You lost")


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def vip_dm(ctx):
    guild = client.get_guild(id=434343434343434)
    role = discord.utils.get(guild.roles, id=34343434343434)
    member = guild.get_member(ctx.message.author.id)
    await member.add_roles(role)


@vip_dm.error
async def vip_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.has_permissions(administrator=True)
async def keyword(ctx, *, word: str):
    channel = client.get_channel(00000000000)
    messages = await ctx.channel.history(limit=200).flatten()

    for msg in messages:
        if word in msg.content:
            await ctx.send(msg.jump_url)


@keyword.error
async def kw_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.has_permissions(administrator=True)
async def setdelay(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f'**Removed the slowmode delay in this channel from {seconds} seconds!**')


@setdelay.error
async def sd_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def Prime(ctx):
    await ctx.send(f'Use Amazon Prime on Twitch: https://twitch.amazon.com/tp')


@client.command()
async def timer(ctx):
    await ctx.send(f'Starting Countdown in less than 15 seconds')
    await asyncio.sleep(15)
    await ctx.send(f'Starting Countdown now...')
    await asyncio.sleep(1)
    await ctx.send(f'3...')
    await asyncio.sleep(1)
    await ctx.send(f'2...')
    await asyncio.sleep(1)
    await ctx.send(f'1...')
    await asyncio.sleep(1)
    await ctx.send(f'GO Wondertrade')
    await asyncio.sleep(90)
    await ctx.send(f'Trades finished succesfully | Thanks for Trading')


@client.command()
@commands.cooldown(1, 90, commands.BucketType.user)
async def blackjack(ctx):
    choices = ['You Won the Blackjack', 'You Lost the Blackjack', 'Tied']
    rancoin = random.choice(choices)
    await ctx.send(f'Shuffleling Cards [20 seconds]')
    await asyncio.sleep(20)
    await ctx.send(f'Making Choice Now [10 seconds]')
    await asyncio.sleep(10)
    await ctx.send(f'I choose this One...')
    await asyncio.sleep(2)
    await ctx.send(rancoin)


@blackjack.error
async def blj_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))


@client.command()
async def close(ctx):
    await ctx.send(f'Disconnecting Bot in 15 seconds...')
    await asyncio.sleep(15)
    await client.logout()


@client.command()
async def Sub(ctx):
    await ctx.send(f'https://www.twitch.tv/products/shinyhunter2109')


def is_it_me(ctx):
    return ctx.author.id =='Insert Your Discord-ID here!'


@client.command()
@commands.check(is_it_me)
async def Update(ctx):
    await ctx.send(f'Checking for Updates...')
    await asyncio.sleep(10)
    await ctx.send(f'Latest Version detected...')
    embed = discord.Embed(
            color= discord.Colour.dark_teal()
        )
    embed.add_field(name='Latest Bot Version' ,value='[Click here to download]( https://github.com/Shinyhunter2109/Discord-Moveset-Bot/releases/download/4.1.1/Discord-Moveset-Bot.7z )', inline=False)
    await ctx.send(embed=embed)
    await asyncio.sleep(20)
    await ctx.send(f'Downloading New Version Now!')
    await asyncio.sleep(60)
    await ctx.send(f'Verify New Content')
    await asyncio.sleep(20)
    await ctx.send(f'Update Complete')
    await asyncio.sleep(10)
    await ctx.send(f'Please restart Bot now or wait 60 seconds')
    await asyncio.sleep(60)
    await ctx.send(f'No User Input recognized, restarting Bot now...')
    await client.logout()


@client.command()
async def BN(ctx):
    guild = ctx.guild
    await guild.create_role(name="Battle.net")


@client.command()
async def Battle_net(ctx):
    guild = ctx.guild
    await guild.create_role(name="Battle.net")


@client.command()
async def pokedex(ctx):
    await ctx.send(f'There are over 910 Pokemon on the Pokedex!')


@client.command()
async def abomasnow(ctx):
    await ctx.send(f'Ability: Soundproof  EVs: 92 HP / 252 SpA / 164 Spe  Nature: Mild  Moves: Blizzard  Giga Drain  Focus Blast  Ice Shard  Item: Abomasite')
    await ctx.send(f'https://www.pokewiki.de/images/f/ff/Pok%C3%A9monsprite_460_Schillernd_XY.gif')


@client.command()
async def abra(ctx):
    await ctx.send(f'Ability: Magic Guard  EVS: 236 Spa / 76 SpD / 196 Spe  Nature: Timid  Level: 5    Moves: Psychic  Dazzling Gleam  Hidden Power Fighting  Protect  Item: Focus Sash')
    await ctx.send(f'https://www.pokewiki.de/images/3/3a/Pok%C3%A9monsprite_063_Schillernd_XY.gif')


@client.command()
async def absol(ctx):
    await ctx.send(f'Ability: Justified  EVS: 252 Atk / 4 Def / 252 Spe  Nature: Adamant  Moves: Swords Dance  Knock Off  Sucker Punch  Superpower  Item: Life Orb')
    await ctx.send(f'https://www.pokewiki.de/images/c/c8/Pok%C3%A9monsprite_359_Schillernd_XY.gif')


@client.command()
async def accelgor(ctx):
    await ctx.send(f'Ability: Sticky Hold  EVS: 4 Def / 252 SpA / 252 Spe  Nature: Timid  Moves: Bug Buzz  Focus Blast  Energy Ball  Spikes  Item: Choice Specs')
    await ctx.send(f'https://www.pokewiki.de/images/9/9d/Pok%C3%A9monsprite_617_Schillernd_XY.gif')


@client.command()
async def aegislash(ctx):
    await ctx.send(f'Ability: Stance Change  EVS: 252 HP / 252 SpA / 4 SpD  Nature: Quit  Moves: Shadow Ball  Flash Cannon  Shadow Sneak  Kings Shield  Item: Leftovers')
    await ctx.send(f'https://www.pokewiki.de/images/6/67/Pok%C3%A9monsprite_681_Schillernd_XY.gif')


@client.command()
async def aerodactyl(ctx):
    await ctx.send(f'Ability: Unnerve  EVS: 252 Atk / 4 Def / 252 Spe  Nature: Jolly  Moves: Stone Edge  Earthquake  Pursuit  Roost  Item: Aerodactylite')
    await ctx.send(f'https://www.pokewiki.de/images/a/a0/Pok%C3%A9monsprite_142_Schillernd_XY.gif')


@client.command()
async def aggron(ctx):
    await ctx.send(f'Ability: Sturdy  EVS: 252 HP / 4 Def / 252 SpD  Nature: Careful  Moves: Stealth Rock  Heavy Slam  Earthquake  Toxic  Item: Aggronite')
    await ctx.send(f'https://www.pokewiki.de/images/7/79/Pok%C3%A9monsprite_306_Schillernd_XY.gif')


@client.command()
async def aipom(ctx):
    await ctx.send(f'Ability: Skill Link  EVS: 76 HP / 116 Atk / 76 Def / 236 Spe  Nature: Jolly  Level: 5    Moves: Fury Swipes  Knock Off  Brick Break  Fake Out  Item: Life Orb')
    await ctx.send(f'https://www.pokewiki.de/images/c/ce/Pok%C3%A9monsprite_190_Schillernd_XY.gif')


@client.command()
async def alakazam(ctx):
    await ctx.send(f'Ability: Magic Guard  EVS: 4 Def / 252 SpA / 252 Spe  Nature: Timid  Moves: Psychic  Focus Blast  Recover  Shadow Ball  Item: Alakazite')
    await ctx.send(f'https://www.pokewiki.de/images/f/f2/Pok%C3%A9monsprite_065_Schillernd_XY.gif')


@client.command()
async def alomomola(ctx):
    await ctx.send(f'Ability: Regenerator  EVS: 40 HP / 252 Def / 216 SpD  Nature: Bold  Moves: Wish  Protect  Toxic  Scald  Item: Leftovers')
    await ctx.send(f'https://www.pokewiki.de/images/2/21/Pok%C3%A9monsprite_594_Schillernd_XY.gif')


@client.command()
async def altaria(ctx):
    await ctx.send(f'Ability: Natural Cure  EVS: 72 HP / 252 Atk / 184 Spe  Nature: Adamant  Moves: Dragon Dance  Return  Refresh  Roost  Item: Altarianite')
    await ctx.send(f'https://www.pokewiki.de/images/a/a5/Pok%C3%A9monsprite_334_Schillernd_XY.gif')


@client.command()
async def amaura(ctx):
    await ctx.send(f'Ability: Snow Warning  EVS: 60 HP / 220 SpA / 228 Spe  Nature: Modest  Level: 5    Moves: Blizzard  Earth Power  Thunderbolt  Ancient  Item: Choice Scarf')
    await ctx.send(f'https://www.pokewiki.de/images/e/e8/Pok%C3%A9monsprite_698_Schillernd_XY.gif')


@client.command()
async def ambipom(ctx):
    await ctx.send(f'Ability: Technican  EVS: 252 Atk / 4 Def / 252 Spe  Nature: Jolly  Moves: Fake Out  Return  Low Kick  U-turn  Item: Life Orb')
    await ctx.send(f'https://www.pokewiki.de/images/1/13/Pok%C3%A9monsprite_424_Schillernd_XY.gif')


@client.command()
async def amoonguss(ctx):
    await ctx.send(f'Ability: Regenerator  EVS: 252 HP / 176 Def / 80 SpD  Nature: Bold  Moves: Spore  Giga Drain  Hidden Power Fire  Clear Smog  Item: Rocky Helmet')
    await ctx.send(f'https://www.pokewiki.de/images/6/64/Pok%C3%A9monsprite_591_Schillernd_XY.gif')


@client.command()
async def ampharos(ctx):
    await ctx.send(f'Ability: Static  EVS: 4 HP / 252 SpA / 252 Spe  Nature: Modest  Moves: Volt Switch  Dragon Pulse  Focus Blast  Thunderbolt  Item: Ampharosite')
    await ctx.send(f'https://www.pokewiki.de/images/0/0a/Pok%C3%A9monsprite_181_Schillernd_XY.gif')


@client.command()
async def anorith(ctx):
    await ctx.send(f'Ability: Battle Armor  EVS: 236 Atk / 36 Def / 236 Spe  Nature: Jolly  Level: 5  Moves: Stealth Rock  Rapid Spin  Knock Off  Rock Blast  Item: Berry Juice')
    await ctx.send(f'https://www.pokewiki.de/images/3/39/Pok%C3%A9monsprite_347_Schillernd_XY.gif')


@client.command()
async def araquanid(ctx):
    await ctx.send(f'Ability: Water Bubble  EVS: 96 HP / 220 Atk / 192 Spe  Nature: Adamant  Moves: Liquidation  Spider Web  Toxic  Rest  Item: Splash Plate')
    await ctx.send(f'https://www.pokewiki.de/images/6/66/Pok%C3%A9monsprite_752_Schillernd_SoMo.gif')


@client.command()
async def arbok(ctx):
    await ctx.send(f'Ability: Intimidate  EVS: 252 Atk / 4 SpD / 252 Spe  Nature: Adamant  Moves: Coil  Gunk Shot  Earthquake  Sucker Punch  item: Black Sludge')
    await ctx.send(f'https://www.pokewiki.de/images/7/78/Pok%C3%A9monsprite_024_Schillernd_XY.gif')


@client.command()
async def arcanine(ctx):
    await ctx.send(f'Ability: Flash Fire  EVS: 252 Atk / 4 Def / 252 Spe  Nature: Jolly  Moves: Flare Blitz  Wild Charge  Extreme Speed  Morning Sun  Item: Life Orb')
    await ctx.send(f'https://www.pokewiki.de/images/7/72/Pok%C3%A9monsprite_059_Schillernd_XY.gif')


@client.command()
async def arceus(ctx):
    await ctx.send(f'Ability: Multitype  EVS: 240 HP / 252 Atk / 16 Spe  Nature: Adamant  Moves: Swords Dance  Extreme Speed  Shadow Claw  Recover  Item: Chople Berry')
    await ctx.send(f'https://www.pokewiki.de/images/9/94/Pok%C3%A9monsprite_493_Schillernd_XY.gif')


@client.command()
async def archen(ctx):
    await ctx.send(f'Ability: Defeatist  EVS: 76 HP / 180 Atk / 196 Spe  Nature: Jolly  Level: 5  Moves: Acrobatics  Rock Slide  Heat Wave  Hidden Power Grass Item: Berry Juice')
    await ctx.send(f'https://www.pokewiki.de/images/e/e6/Pok%C3%A9monsprite_566_Schillernd_XY.gif')


@client.command()
async def archeops(ctx):
    await ctx.send(f'Ability: Defeatist  EVS: 252 Atk / 252 Spe / 0 HP / 0 Def / 0 SpD  Nature: Naive  Moves: Head Smash  Stealth Rock  Endeavor  Taunt  Item: Focus Sash')
    await ctx.send(f'https://www.pokewiki.de/images/e/e0/Pok%C3%A9monsprite_567_Schillernd_XY.gif')


@client.command()
async def ariados(ctx):
    await ctx.send(f'Ability: Swarm  EVS: 252 Atk / 4 Def / 252 Spe  Nature: Jolly  Moves: Sticky Web  Toxic Spikes  Megahorn  Toxic Thread  Item: Focus Sash')
    await ctx.send(f'https://www.pokewiki.de/images/7/75/Pok%C3%A9monsprite_168_Schillernd_XY.gif')


@client.command()
async def armaldo(ctx):
    await ctx.send(f'Ability: Battle Armor  EVS: 252 HP / 92 Atk / 164 Spe  Nature: Adamant  Moves: Rapid Spin  Stone Edge  Knock Off  Earthquake  Item: Leftovers')
    await ctx.send(f'https://www.pokewiki.de/images/7/74/Pok%C3%A9monsprite_348_Schillernd_XY.gif')


@client.command()
async def aromatisse(ctx):
    await ctx.send(f'Ability: Aroma Veil  EVS: 248 HP / 252 SpA / 8 SpD  Nature: Quit  Moves: Trick Room  Nasty Plot  Moonblast  Psychic  Item: Fairium Z')
    await ctx.send(f'https://www.pokewiki.de/images/a/a1/Pok%C3%A9monsprite_683_Schillernd_XY.gif')


@client.command()
async def aron(ctx):
    await ctx.send(f'Ability: Rock Head  EVS: 196 Atk / 116 SpD / 196 Spe  Nature: Jolly  Level: 5  Moves: Rock Polish  Head Smash  Heavy Slam  Earthquake  Item: Eviolite')
    await ctx.send(f'https://www.pokewiki.de/images/7/7a/Pok%C3%A9monsprite_304_Schillernd_XY.gif')


@client.command()
async def articuno(ctx):
    await ctx.send(f'Ability: Pressure  EVS: 252 SpA / 4 SpD / 252 Spe  Nature: Timid  Moves: Substitute  Roost  Freeze-Dry  Hurricane  Item: Leftovers')
    await ctx.send(f'https://www.pokewiki.de/images/a/a9/Pok%C3%A9monsprite_144_Schillernd_XY.gif')


@client.command()
async def audino(ctx):
    await ctx.send(f'Ability: Regenerator  EVS: 252 HP / 4 Def / 252 SpD  Nature: Calm  Moves: Wish  Protect  Heal Bell  Knock Off  Item: Audinite')
    await ctx.send(f'https://www.pokewiki.de/images/a/a4/Pok%C3%A9monsprite_531_Schillernd_XY.gif')


@client.command()
async def aurorus(ctx):
    await ctx.send(f'Ability: Snow Warning  EVS: 252 SpA / 4 SpD / 252 Spe  Nature: Modest  Moves: Blizzard  Freeze-Dry  Earth Power  Hidden Power Rock  Item: Choice Specs')
    await ctx.send(f'https://www.pokewiki.de/images/0/01/Pok%C3%A9monsprite_699_Schillernd_XY.gif')


@client.command()
async def avalugg(ctx):
    await ctx.send(f'Ability: Sturdy  EVS: 252 HP / 88 Atk / 168 Def  Nature: Impish  Moves: Avalanche  Recover  Rapid Spin  Earthquake  Item: Rocky Helmet')
    await ctx.send(f'https://www.pokewiki.de/images/a/a5/Pok%C3%A9monsprite_713_Schillernd_XY.gif')


@client.command()
async def axew(ctx):
    await ctx.send(f'Ability: Mold Breaker  EVS: 68 HP / 220 Atk / 220 Spe  Nature: Jolly  Moves: Dragon Dance  Outrage  Superpower  Iron Tail  Item: Eviolite')
    await ctx.send(f'https://www.pokewiki.de/images/a/af/Pok%C3%A9monsprite_610_Schillernd_XY.gif')


@client.command()
async def azelf(ctx):
    await ctx.send(f'Ability: Levitate  EVS: 252 Atk / 4 SpA / 252 Spe  Nature: Jolly  Moves: Stealth Rock  Explosion  Taunt  Knock Off  Item: Focus Sash')
    await ctx.send(f'https://www.pokewiki.de/images/c/c8/Pok%C3%A9monsprite_482_Schillernd_XY.gif')


@client.command()
async def azumarill(ctx):
    await ctx.send(f'Ability: Huge Power  EVS: 252 Atk / 4 HP / 252 Spe  Nature: Adamant  Moves: Belly Drum  Aqua Jet  Play Rough  Knock Off  Item: Sitrus Berry')
    await ctx.send(f'https://www.pokewiki.de/images/5/59/Pok%C3%A9monsprite_184_Schillernd_XY.gif')


@client.command()
async def azurill(ctx):
    await ctx.send(f'Ability: Huge Power  EVS: 196 HP / 196 Atk / 116 Def  Nature: Brave  Level: 5  Moves: Double-Edge  Waterfall  Return  Knock Off  Item: Life Orb')
    await ctx.send(f'https://www.pokewiki.de/images/6/63/Pok%C3%A9monsprite_298_Schillernd_XY.gif')


@client.command(aliases=['8ball', 'test'])
async def _8Ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt',
                 'Yes.',
                 'My reply is no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
@commands.has_permissions(manage_channels=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Channel Clear Successfully done!')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error


@client.event
async def on_guild_join(guild):
    channel = guild.text_channels[0]
    embed = discord.Embed(title=guild.name, description="Hello, how can I help your Server?")
    await channel.send(embed=embed)
    
   
@client.event
async def on_member_update(before, after):
    if before.status is discord.Status.offline and after.status is discord.Status.online:
        print('was offline then online')
        channel = client.get_channel(3333333333333333)  # notification channel
        await channel.send(f'{after.name} is now {after.status}')


@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)
    print(f'{member} was given {role}')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

client.run(TOKEN)
