import discord
import random
import asyncio
import json
import re
import aiofiles
import io
import zipfile
import secrets
import async_timeout
import threading
import warnings
import logging
import sys
import time
import requests
import re
import math
import keyword
import calendar
import venv
import webbrowser
import typing
import traceback
import youtube_dl
import os
import requests
import praw
import interactions
from datetime import datetime, timedelta
from googletrans import Translator
from discord.embeds import Embed
from discord.ext.commands import BadArgument
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import has_permissions, MissingPermissions
from github import Github
from aiohttp import ServerDisconnectedError
from aiohttp import ServerTimeoutError
from discord.voice_client import VoiceClient
from discord.ext import commands, tasks
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import StageChannel
from discord import Webhook
from discord import Intents
from discord import Streaming
from youtube_dl import YoutubeDL
from subprocess import run
from dataclasses import dataclass
from os import name, system
from dotenv import load_dotenv
from discord import Status
from itertools import cycle
from datetime import date
from discord_slash import SlashCommand, SlashContext
from discord_slash.context import MenuContext
from discord_slash.model import ContextMenuType
from discord_slash.model import SlashCommandOptionType
from discord_slash.model import ChoiceData
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow, create_button
from discord_slash.model import ButtonStyle



TOKEN = 'INSERT YOUR TOKEN HERE...' #   <---- Your Bot Token goes here ! #
if not TOKEN:
    raise ValueError("❌ No Bot Token found!")

load_dotenv()
CLEAR_PASSWORD = os.getenv("CLEAR_PASSWORD")
BAN_PASSWORD = os.getenv("BAN_PASSWORD")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()
intents.presences = True
intents.members = True
client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())
client.launch_time = datetime.utcnow()
guild_ids = [0000000000000] #  <-------  Your Guild ID goes here (multiple guilds possible) #
client.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}
slash = SlashCommand(client, sync_commands=True)
client.remove_command('help')
status = cycle([
    discord.Game("Community Party 🎉"),
    discord.Game("Listening to Spotify 🎧"),
    discord.Game("with !help"),
    ])

@tasks.loop(seconds=90)
async def change_status():
    await client.change_presence(activity=next(status))

ROLE = 'Member' # Standard Role can be edited if needed ! #

def setprefix():
    with open("prefix.txt") as f: #  (optional)
        return "\n".join(f.readlines())
    



@client.event
async def on_ready():
    check_giveaways.start()
    for guild in client.guilds:
        client.warnings[guild.id] = {}
        
    async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
        pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]
    prefix = setprefix()
    change_status.start()
    print('Welcome back: ' + client.user.name + '\n')
    print(f'This Program is designed for {OS11} {MCOS} & {Linux_OS}')
    print(f'Bot Version: {__version__}')
    print(f'Build Version: {Build_Ver_OS}')


__version__ = "8.1.2" # Current Version of the Program #


def check_for_update():
    api_url = "https://api.github.com/repos/Shinyhunter2109/Discord-Moveset-Bot/releases/latest"
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        
        latest_version = data["tag_name"].lstrip("v")
        release_url = data.get("html_url", "https://github.com/Shinyhunter2109/Discord-Moveset-Bot/releases")

        
        if latest_version != __version__:
            print(f"\U0001F4E2 Update available! New Version: v{latest_version} (current: v{__version__})")
            print("See below:", release_url)
        else:
            print(f"✅ You are using the latest Version (v{__version__})")

    except Exception as e:
        print(f"❌ Error during Update check: {e}")


check_for_update()



# ====================== ITEM STORAGE VARIABLES ============================== #

RemovedFromBot = RemovedFromBot = 'This Command has been Removed!'
Added2Item = Added2Item = 'This Command has been recently added!'
NewItem = NewItem = 'This Command is new!'
RemovedInPatch = RemovedInPatch = 'This gets removed in the next Patch!'
Classic = Classic = 'This is a Legacy Command and it exists since the Bot was created'
NewItemCategory = NewItemCategory = 'This Section has been newly added to the Program'

# =============================================================================== #

Build_Ver_OS = Build_Ver_OS = '8.5.2'
Downtime = Downtime = 'N/A'
DownDate = DownDate = 'N/A'
Version = Version = 8.5
LogVer = LogVer = 3.6
Extension = Extension = 'Loaded'
ExtVer = ExtVer = 4.1
CMM = CMM = 'Online'
CSS = CSS = 13000
OS10 = OS10 = 'Windows 10'
OS11 = OS11 = 'Windows 11'
MCOS = MCOS = 'Mac_OS'
Linux_OS = Linux_OS = 'Linux'
Server_Status = Server_Status = 'Online'
Server_Status2 = Server_Status2 = 'Offline'
Server_Status3 = Server_Status3 = 'Maintenance'
Server_Status4 = Server_Status4 = 'Closed'
Server_Status5 = Server_Status5 = 'Connection lost'
Support_End = Support_End = 'The Support Circle for the Program has ended'
PUR = PUR = 1.1
TWWA = TWWA = 'Offline'
TWWB = TWWB = 'Live'
NSW2 = NSW2 = 'Nintendo Switch 2'
DL = DL = 'Deadlock'
CataCB = CataCB = 'Live'
CataC = CataC = 'Live'
CataCV = CataCV = 4.0
DFV = DFV = '10.2.7'
TWWV = TWWV = '11.0.2'
BOwner = BOwner = 'twitch.tv/shinyhunter2109'
newdat = newdat = 8.5
OWN = OWN = 11.0
data = ("🎉")
item = ("🎉")
Build = Build = 8.1
NewVer = NewVer = 8.1
NDate = NDate = 'N/A'
Uploader = Uploader = 'Shinyhunter2109'
counter = data.count(item)
PR = PR = '8.5.1'
NPR = NPR = '8.5.2'
SDowntime = SDowntime = 'N/A'
PRDate = PRDate = 'N/A'
PRUploader = PRUploader = 'ShinyhunterTV'
DevBuild = DevBuild = 8.2
NDevB = NDevB = 8.5
PMP = PMP = 'TOP SECRET'
DevUpload = DevUpload = 'Shinyhunter'
DevDate = DevDate = 'N/A'
BDSP = BDSP = 1.3
PLA = PLA = 1.1
SV = SV = 3.0




Season_1 = Season_1 = '09/21/2024'
Season_2 = Season_2 = '12/31/2025'
Season_3 = Season_3 = 'N/A'
Season_4 = Season_4 = 'N/A'

Season_Reset = SeasonUpdate = 'The Old Season is Gone and the New Season has Started' 
SeasonUpdate_Revoke = SeasonError = 'Error retrieving Seasonal Information !'
SeasonError = SeasonError = 'Something went wrong'
Season_Start = Season_Start = 1
SeasonClose = SeasonClose = 0
S_enable = S_enable = 'Season has started'
S_disable = S_disable = 'Season has ended'

Season_1 = Season_1 = S_enable
Season_2 = Season_2 = SeasonClose

# ============================ Network Information =================================================================== #

IsConsoleBanned = IsConsoleBanned = f'{PMP}'
IsSwitchBanned = IsSwitchBanned = f'{PMP}'
Nintendo_Network_3ds = Nintendo_Network_3ds = 'Server Offline'
Nintendo_Switch_Network = Nintendo_Switch_Network = 'Server Online'
CFW_Server_Status = CFW_Server_Status = f'{PMP}'
Steam_Server_Status = Steam_Server_Status = 'Online'
Battle_Net_Status = Battle_Net_Status = 'Online'
EA_Status = EA_Status = 'Online'
EOS_Status = EOS_Status = 'Online'
ZOS_Status = ZOS_Status = 'Online'

# ======================================================== Server Status Switch ========================================#

BNS_1 = BNS_1 = 'ON'
BNS_2 = BNS_2 = 'OFF'
STS_1 = STS_1 = 'ON'
STS_2 = STS_2 = 'OFF'
EAS_1 = EAS_1 = 'ON'
EAS_2 = EAS_2 = 'OFF'
EOS_1 = EOS_1 = 'ON'
EOS_2 = EOS_2 = 'OFF'

# ======================== VALUES ========================================== # # Most of this will be used later #
NBV = NBV = 8.5
OBV = OBV = 8.5
ODV = ODV = 8.5
NDV = NDV = 8.5
NEV = NEV = 4.0
OEV = OEV = 3.9
OUE = OUE = 3.0
NUE = NUE = 3.2
OSV = OSV = 2.9
NSV = NSV = 3.5
OTV = OTV = 3.8
NTV = NTV = 4.0
EXT = EXT = 3.5
OEXT = OEXT = 3.0
UV = UV = NBV
RV = RV = OBV
# ============================================================================ #


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
        await ctx.send("You're pretty new!")
    else:
        await ctx.send("You're not so new.")


class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]


@client.command()
async def roles(ctx, *, member: MemberRoles):
    """Tells you a member's roles."""
    await ctx.send('I see the following roles: ' + ', '.join(member))


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


@client.command()
async def serveri(ctx):
    client.loop.create_task(server_icon())
    await ctx.send("Loop started, replacing current icon.")


@client.command()
async def sync(ctx: commands.Context, guild: discord.Guild = None) -> None:
    if guild is None:
        await client.tree.sync()
    else:
        await client.tree.sync(guild=guild)


@client.command()
async def server_icon():
    while True:
        server1 = client.get_guild(00000000)
        with open('EnterYourPathHere/jpg', 'rb') as f:
            icon = f.read()
        await server1.edit(icon=icon)
        print("Server Icon changed.")
        await asyncio.sleep(90)


@client.command()
@commands.has_permissions(manage_roles=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("**The provided member could not be found or you forgot to provide one.**")
        
    if reason is None:
        return await ctx.send("**Please provide a reason for warning this user.**")

    try:
        first_warning = False
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")


@client.command()
@commands.has_permissions(manage_roles=True)
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("**The provided member could not be found or you forgot to provide one.**")
    
    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        await ctx.send("**This user has no warnings.**")


@client.command()
@commands.cooldown(1, 190, commands.BucketType.user)
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f'**Uptime for the program:** {days}d, {hours}h, {minutes}m, {seconds}s')


@uptime.error
async def uptime_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def BugFix(ctx):
    us = us = '@Shinyhunter2109'
    await ctx.send(f'**Found a Bug?** | Contact **{us}** directly via DM ! | **Thank You**')



@client.command()
async def SeasonInfo(ctx):
    await ctx.send(f'The First Season starts on: **{Season_1}**')


#####################################      Update Progress   #######################################################

GITHUB_REPO = "Shinyhunter2109/Discord-Moveset-Bot"

@client.command()
@commands.is_owner()
async def updatebot(ctx):
    """Downloads the latest Version of the Program (only for Bot-Owners)."""
    await ctx.send("🔍 Checking for Updates...")

    releases_url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    try:
        response = requests.get(releases_url, timeout=10)
        response.raise_for_status()
        release = response.json()
        latest_version = release["tag_name"].lstrip("v")

        if latest_version == __version__:
            await ctx.send(f"✅ You are on the latest Version (v{__version__}).")
            return

        download_url = release["zipball_url"]
        await ctx.send(f"⬇️ Update available: v{latest_version} → Downloading...")

        zip_response = requests.get(download_url)
        zip_response.raise_for_status()

        with zipfile.ZipFile(io.BytesIO(zip_response.content)) as zip_file:
            extract_path = "update_temp"
            zip_file.extractall(extract_path)

            
            for root, dirs, files in os.walk(extract_path):
                for file in files:
                    if file == "Discord-Bot.py":  
                        full_path = os.path.join(root, file)
                        os.replace(full_path, "Discord-Bot.py")  
                        await ctx.send("✅ Update installed.")
                        break

        
        import shutil
        shutil.rmtree(extract_path)

        await ctx.send("🔁 Restarting...")

        
        os.execv(sys.executable, [sys.executable] + sys.argv)

    except Exception as e:
        await ctx.send(f"❌ Update failed: {e}")


# ================================================= Economy Section Start ============================================================== #


@client.command()
async def balance(ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    await ctx.send(f"**{ctx.author.name}'s coin balance**")
    await ctx.send(f'**Coin balance:** {wallet_amt} coins')
    await ctx.send(f'**Bank balance:** {bank_amt} coins')


@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def dailybonus(ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()


    earnings = random.randrange(1000)


    await ctx.send(f'**Your Daily Bonus are:** {earnings} coins!!')


    users[str(user.id)]["wallet"]+= earnings

    with open("bank.json","w") as f:
        json.dump(users,f)


@dailybonus.error
async def day_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**You already claimed your Daily Reward | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weeklybonus(ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()


    earnings = random.randrange(2500)


    await ctx.send(f'**Your Weekly Bonus are:** {earnings} coins!!')


    users[str(user.id)]["wallet"]+= earnings

    with open("bank.json","w") as f:
        json.dump(users,f)


@weeklybonus.error
async def week_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**You already claimed your Weekly Reward | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 2628000, commands.BucketType.user)
async def monthlybonus(ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()


    earnings = random.randrange(5000)


    await ctx.send(f'**Your Monthly Bonus are:** {earnings} coins!!')


    users[str(user.id)]["wallet"]+= earnings

    with open("bank.json","w") as f:
        json.dump(users,f)


@monthlybonus.error
async def monthly_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**You already claimed your Monthly Reward | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


async def open_account(user):

        users = await get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 0

        with open("bank.json","w") as f:
            json.dump(users,f)
        return True



async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users


async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal



@client.command()
@commands.cooldown(1, 31622400, commands.BucketType.user)
async def xmas_bonus(ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()


    earnings = random.randrange(50000)


    await ctx.send(f'**Your Christmas Bonus are:** {earnings} shinycoins!!')
    await asyncio.sleep(5)
    await ctx.send(f'**Bonus has been added to your Balance !**')
    await asyncio.sleep(5)
    await ctx.send(f'**This Bonus was secret and you found it before the event ended !**')


    users[str(user.id)]["wallet"]+= earnings

    with open("bank.json","w") as f:
        json.dump(users,f)


@xmas_bonus.error
async def christmasevent_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**The Christmas Event is over !| please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


# Economy Section End #


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
        colour = discord.Colour.gold()
    )

    embed.set_author(name='coinhelp')
    embed.add_field(name='.coinflip', value='Return Heads/Tails', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def joinhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_author(name='joinhelp')
    embed.add_field(name='.join', value='Tells if joining from Bot was Successful', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def pokehelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='pokehelp')
    embed.add_field(name='.pokemonname', value='Returns Info & Picture', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def bottlehelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='bottlehelp')
    embed.add_field(name='.bottles', value='Returns [Value of Beer]', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def spotifyhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_author(name='spotifyhelp')
    embed.add_field(name='.spotify', value='Returns listening Activity from the User', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def eightballhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.light_grey()
    )

    embed.set_author(name='eightballhelp')
    embed.add_field(name='.8ball', value='Returns one of the pre Messages for your Question', inline=False)
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def musichelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_magenta()
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
async def spotify(ctx, member: discord.Member = None):
    member = member or ctx.author  # Wenn kein Member angegeben ist, nutze den Command-Author

    for activity in member.activities:
        if isinstance(activity, discord.Spotify):
            embed = discord.Embed(
                title=f"{member.display_name} is listening to Spotify 🎧",
                description=f"**{activity.title}** von **{activity.artist}**",
                color=0x1DB954  # Spotify-Grün
            )
            embed.set_thumbnail(url=activity.album_cover_url)
            embed.add_field(name="Album", value=activity.album, inline=True)
            embed.add_field(name="Dauer", value=f"{activity.duration.seconds//60}:{activity.duration.seconds%60:02d}", inline=True)
            embed.add_field(name="Link", value=f"[Song öffnen](https://open.spotify.com/track/{activity.track_id})", inline=False)
            await ctx.send(embed=embed)
            return

    await ctx.send(f"**{member.display_name}** is not listening to Spotify")




@client.command()
@commands.cooldown(1, 90, commands.BucketType.user)
async def emoji(ctx, emoji: discord.PartialEmoji = None):
    if not emoji:
        await ctx.send('**You need to provide an emoji!**')
    else:
        await ctx.send(emoji.url)


@emoji.error
async def emo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def CheckVersion(ctx):
    if OBV < NBV:
        await ctx.send(f'**Your Version Client is outdated ! | Please download the Latest Release from the Github Repo**')
        embed = discord.Embed(
            color= discord.Colour.dark_teal()
        )
        embed.add_field(name='Latest Release Build' ,value='[Click here to download]( https://github.com/Shinyhunter2109/Discord-Moveset-Bot/releases/download/8.5/Discord-Moveset-Bot.zip )', inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'**You are on the Latest Version**')


@client.command()
async def ExtUpdate(ctx):
    if OEXT < EXT:
        await ctx.send(f'**You are using old Extensions | Please update to the latest Version {EXT}**')
    else:
        await ctx.send(f'**Up to Date**')


@client.command()
async def Log_Ver(ctx):
    if OEXT < EXT:
        await ctx.send(f'**Your Version Client is outdated ! | Please update to the latest Version**')
    else:
        await ctx.send(f'**Up to date**')


@client.command()
async def ToolVer(ctx):
    if OTV < NTV:
        await ctx.send(f'**Your Version Client is outdated ! | Please update to Version {NTV}**')
    else:
        await ctx.send(f'**Up to date**')


@client.command()
async def SecurityVer(ctx):
    if OSV < NSV:
        await ctx.send(f'**Your Version Client is outdated ! | Please update to Version {NSV}**')
    else:
        await ctx.send(f'**Up to date**')


@client.command()
async def OSVer(ctx):
    OSVer = OSVer = 'Win 11'
    OSNum = OSNum = '23H2'
    OSBNum = OSBNum = '22631.4037'
    await ctx.send(f'The Bot is currently running on **{OSVer}** with Build Number: **{OSNum}** and Build ID : **{OSBNum}**')


@client.command()
@commands.cooldown(1, 890, commands.BucketType.user)
async def ServerStatus(ctx):
    await ctx.send(f'The Status of the Server is currently **{Server_Status3}**')


@Server_Status.error
async def server_stat_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(name="meme")
async def meme(ctx, subred="memes"):
    msg = await ctx.send('Loading ... ')

    reddit = praw.Reddit(client_id='clientid',
                                client_secret='clientsecret',
                                username='username',
                                password='password',
                                user_agent='useragent')

    subreddit = await reddit.subreddit(subred)
    all_subs = []
    top = subreddit.top(limit=250) # bot will choose between the top 250 memes

    async for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    embed = Embed(title=f'__{name}__', colour=discord.Colour.random(), timestamp=ctx.message.created_at, url=url)

    embed.set_image(url=url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
    embed.set_footer(text='Here is your meme!')
    await ctx.send(embed=embed)
    await msg.edit(content=f'<https://reddit.com/r/{subreddit}/> :white_check_mark:') 
    return


@client.command()
@commands.cooldown(1, 18000, commands.BucketType.user)
async def report(ctx, member: discord.Member,  *, arg):
    role = ctx.guild.get_role(000000000000000) # enter role here #
    members = ctx.guild.members
    await ctx.channel.send('**Your complaint was sent to moderators!**', delete_after=10)
    for i in role.members:
        await i.send(f'{ctx.author.mention} sent a complaint on {member.mention} with reason:\n**{arg}**')


@report.error
async def rep_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def pages(ctx):
    contents = ["**This is page 1!**", "**This is page 2!**", "**This is page 3!**", "**This is page 4!**", "**This is Page 5!**", "**This is Page 6!**"]
    pages = 6
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)


            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()
            break


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


@client.command(help="Play with !Coinflip [your choice]")
@commands.cooldown(1, 65, commands.BucketType.user)
async def Coinflip(ctx):
    rpsGame = ['head', 'tails']
    await ctx.send(f"**head or tails? Choose wisely...**")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'head':
        if comp_choice == 'head':
            await ctx.send(f'**Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}**')
        elif comp_choice == 'tails':
            await ctx.send(f'**Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}**')
        elif comp_choice == 'head':
            await ctx.send(f"**Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}**")
        elif comp_choice == 'tails':
            await ctx.send(f"**Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}**")

    elif user_choice == 'tails':
        if comp_choice == 'head':
            await ctx.send(f'**The head beats the tails? More like the tails beats the head!!\nYour choice: {user_choice}\nMy choice: {comp_choice}**')
        elif comp_choice == 'tails':
            await ctx.send(f'**Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}**')
        elif comp_choice == 'head':
            await ctx.send(f"**Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}**")
        elif comp_choice == 'tails':
            await ctx.send(f"**Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}**")


@Coinflip.error
async def coinflip_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(name="filter", help="Adds word to filter")
async def Filter(ctx, word):
    filter = open("filter.txt", "a")
    filter.write(word+"\n")
    filter.close()
    await ctx.send(f'**Thank You for your Word !**')
    await asyncio.sleep(5)
    await ctx.send(f'**The Word has beend added to the List**')


@Filter.error
async def fil_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, or u did something wrong | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(name="feature", help="Adds features to the feature list")
async def Feature(ctx, word):
    filter = open("feature.txt", "a")
    filter.write(word+"\n")
    filter.close()
    await ctx.send(f'**Thank You for your Feature !**')
    await asyncio.sleep(5)
    await ctx.send(f'**Feature has beend added to the List**')


@Feature.error
async def feature_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, or u did something wrong | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(name="idea", help="Adds ideas to the idea list")
async def Idea(ctx, word):
    filter = open("idea.txt", "a")
    filter.write(word+"\n")
    filter.close()
    await ctx.send(f'**Thank You for your Idea !**')
    await asyncio.sleep(5)
    await ctx.send(f'**Idea has beend added to the List**')


@Idea.error
async def idea_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, or u did something wrong | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(name="hunt", help="Adds hunting ideas to the hunt list")
async def Hunt(ctx, word):
    filter = open("hunt.txt", "a")
    filter.write(word+"\n")
    filter.close()
    await ctx.send(f'**Thank You for your Hunt Idea !**')
    await asyncio.sleep(5)
    await ctx.send(f'**Hunt Idea has beend added to the List**')


@Hunt.error
async def hunt_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, or u did something wrong | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(name="art", help="Adds Art ideas to the Art list")
async def Art(ctx, word):
    filter = open("art.txt", "a")
    filter.write(word+"\n")
    filter.close()
    await ctx.send(f'**Thank You for your Art Idea !**')
    await asyncio.sleep(5)
    await ctx.send(f'**Art Idea has beend added to the List**')


@Art.error
async def art_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, or u did something wrong | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(name="amazon", help="Adds Products to the Amazon list")
async def Amazon(ctx, word):
    filter = open("amazon.txt", "a")
    filter.write(word+"\n")
    filter.close()
    await ctx.send(f'**Thank You for the Product!**')
    await asyncio.sleep(5)
    await ctx.send(f'**Product has beend added to the Amazon List**')


@Amazon.error
async def amazon_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, or u did something wrong | please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def Ads(ctx, member : discord.Member):
    await ctx.send('**NO ADVERTISEMENT ALLOWED | WARNING ACTION INCOMING**')
    await asyncio.sleep(20)
    await member.ban()
    await ctx.send('**Press F to pay respect**')


time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

def convert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key, value in matches:
        try:
            time += time_dict[value] * float(key)
        except:
            raise commands.BadArgument
    return round(time)


GIVEAWAY_FILE = "giveaways.json"

def load_giveaways():
    if not os.path.exists(GIVEAWAY_FILE):
        return []
    with open(GIVEAWAY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_giveaways(data):
    with open(GIVEAWAY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default=str)

# ----------------- Giveaway Command ------------------- #
@client.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, time_str: str, *, prize: str):
    time = convert(time_str)
    end_time = datetime.utcnow() + timedelta(seconds=time)

    embed = discord.Embed(
        title=prize,
        description=f"Hosted by {ctx.author.mention}\nReact with 🎉 to enter!\nEnds <t:{int(end_time.timestamp())}:R>",
        color=discord.Color.green()
    )
    msg = await ctx.send("🎉 **GIVEAWAY** 🎉", embed=embed)
    await msg.add_reaction("🎉")

    giveaways = load_giveaways()
    giveaways.append({
        "message_id": msg.id,
        "channel_id": ctx.channel.id,
        "prize": prize,
        "host_id": ctx.author.id,
        "end_time": end_time.isoformat()
    })
    save_giveaways(giveaways)

    await ctx.send(f"✅ Giveaway gestartet für **{prize}** (Dauer: {time_str})")

# ----------------- Giveaway Checker Task ------------------- #
@tasks.loop(seconds=60)
async def check_giveaways():
    giveaways = load_giveaways()
    updated = []

    for g in giveaways:
        end_time = datetime.fromisoformat(g["end_time"])
        if datetime.utcnow() >= end_time:
            try:
                channel = client.get_channel(g["channel_id"])
                message = await channel.fetch_message(g["message_id"])
                reaction = discord.utils.get(message.reactions, emoji="🎉")
                users = await reaction.users().flatten()
                users = [u for u in users if not u.bot]

                if users:
                    winner = random.choice(users)
                    await channel.send(f"🎉 **Glückwunsch {winner.mention}!** Du hast **{g['prize']}** gewonnen!")
                else:
                    await channel.send(f"⚠️ Keine Teilnehmer beim Giveaway für **{g['prize']}**.")

            except Exception as e:
                print(f"Fehler bei Giveaway {g['prize']}: {e}")
        else:
            updated.append(g)

    save_giveaways(updated)


@giveaway.error
async def ga_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**You dont have the right Permissions to execute this command.**')


password = '0000000' # insert numeric password here !

@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def offline(ctx, *, password_check=None):
    if password_check and password_check == password:
        await ctx.message.channel.purge(limit=1)
        await ctx.send('Shutting down bot...')
        await ctx.bot.logout()
    elif not password_check:
        await ctx.send('Please enter the password!')
    else:
        await ctx.send('You got the password wrong.')


@offline.error
async def offline_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**You dont have the right Permissions to execute this command.**')


@client.command()
async def gg(ctx):
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
        await ctx.send('**I could not find that member...**')


@tasks.loop(seconds=1000)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


password = '0000000' # insert numeric password here !


@client.command()
async def kick(ctx, member : discord.Member, *,password_check=None):
    if password_check and password_check == password:
        await ctx.message.channel.purge(limit=1)
        await ctx.send('Password correct!')
    elif not password_check:
        await ctx.send('Please enter the password!')
    else:
        await ctx.send('You got the password wrong.')
    await member.kick()


password = '0000000'  # insert numeric password here !


@client.command()
@commands.is_owner()
async def ban(ctx, member : discord.Member, *, password: str):
    if password != BAN_PASSWORD:
        await ctx.send("❌ Wrong Password")
        return
    if BAN_PASSWORD == password:
        await ctx.message.channel.purge(limit=1)
        await ctx.send('**Password correct!**')
        await member.ban()
    elif not BAN_PASSWORD:
        await ctx.send('**Please enter the password!**')
    else:
        await ctx.send('**You got the password wrong.**')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'**Unbanned {user.mention}**')
            return


@client.command()
async def Switch(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('switch-talk')
    await asyncio.sleep(5)
    await ctx.send(f'**Channel has been created**')


@client.command()
async def Community(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('community-couch')
    await asyncio.sleep(5)
    await ctx.send(f'**Channel has been created**')


@client.command()
async def SSBU(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('smash-battles ')
    await asyncio.sleep(5)
    await ctx.send(f'**Channel has been created**')


@client.command()
async def spam(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('bot-spam')
    await asyncio.sleep(5)
    await ctx.send(f'**Channel has been created**')


@client.command()
async def trades(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('viewer-trades')
    await asyncio.sleep(5)
    await ctx.send(f'**Channel has been created**')


@client.command()
async def Youtube(ctx):
    guild = ctx.guild
    await guild.create_role(name="Youtuber")
    await asyncio.sleep(5)
    await ctx.send(f'**Role has been created**')


@client.command()
async def GM(ctx):
    guild = ctx.guild
    await guild.create_role(name="Guild_Member")
    await asyncio.sleep(5)
    await ctx.send(f'**Role has been created**')


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
    await asyncio.sleep(5)
    await ctx.send(f'**Role has been created**')


@client.command()
async def DB(ctx):
    guild = ctx.guild
    await guild.create_role(name="Discord-Bot")
    await asyncio.sleep(5)
    await ctx.send(f'**Role has been created**')


@client.command()
async def DBot(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Discord-Bot")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def ST(ctx):
    guild = ctx.guild
    await guild.create_role(name="Sub-Trade")
    await asyncio.sleep(5)
    await ctx.send(f'**Role has been created**')


@client.command()
async def STrade(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Sub-Trade")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def Mixer(ctx):
    guild = ctx.guild
    await guild.create_role(name="Mixer")
    await asyncio.sleep(5)
    await ctx.send(f'**Role has been created**')


@client.command()
async def Stream(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Mixer")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def Admin(ctx):
    guild = ctx.guild
    await guild.create_role(name="Administrator")
    await asyncio.sleep(5)
    await ctx.send(f'**Role has been created**')


@client.command()
async def Chef(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Administrator")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


@client.command()
async def BDSPHelp(ctx):
    Game = Game = 'Brilliant Diamond & Shining Pearl'
    await ctx.send(f'Unfortunally we do not have Support yet for this PKMN Game: **{Game}** & Version: **{BDSP}** for creating Custom PKMN .')


@client.command()
async def SVHelp(ctx):
    Game = Game = 'Scarlet & Violet'
    await ctx.send(f'Unfortunally we do not have Support yet for the Latest PKMN Game: **{Game}** & Version: **{SV}** for creating Custom PKMN .')


@client.command()
async def Discord(ctx):
    embed = discord.Embed(
            color= discord.Colour.dark_teal()
        )
    embed.add_field(name='Come and checkout the Development of this Project' ,value='[Click here to join]( https://discord.gg/T2deZV8 )', inline=False)
    await ctx.send(embed=embed)


# Math Module Start ########

@client.command()
@commands.cooldown(1, 100, commands.BucketType.user)
async def Math_Help(ctx):
    await ctx.send(f'**Welcome New User, Commands for this Module are: !add, !sub, !multiply, !divide**')
    await asyncio.sleep(5)
    await ctx.send(f'**Use Number (1) and Number (2) that u have choosen and select one of the Commands above**')


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



#Removed / Unused Section #

@client.command()
async def dma(ctx):
    rand_num = (0, 0)
    win_num = 0
    if win_num == rand_num:
       await ctx.send(f"{RemovedFromBot}")
    else:
        await ctx.send(f"{RemovedFromBot}")


@client.command(
    name="base_command",
    description="This description isn't seen in UI",
    scope=1234567890,
    options=[
        interactions.Option(
            name="command_name",
            description="A descriptive description",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
                interactions.Option(
                    name="option",
                    description="A descriptive description",
                    type=interactions.OptionType.INTEGER,
                    required=False,
                ),
            ],
        ),
        interactions.Option(
            name="second_command",
            description="A descriptive description",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
                interactions.Option(
                    name="second_option",
                    description="A descriptive description",
                    type=interactions.OptionType.STRING,
                    required=True,
                ),
            ],
        ),
    ],
)
async def cmd(ctx: interactions.CommandContext, sub_command: str, second_option: str = "", option: int = None):
    if sub_command == "command_name":
        await ctx.send(f"You selected the command_name sub command and put in {option}")
    elif sub_command == "second_command":
        await ctx.send(f"You selected the second_command sub command and put in {second_option}")


@client.command(
    type=interactions.ApplicationCommandType.USER,
    name="User Command",
    scope=0000000000000000,
)
async def test(ctx):
    await ctx.send(f"You have applied a command onto user {ctx.target.user.username}!")

button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="world!",
    custom_id="hello"
)

@client.command(
    name="button_test",
    description="This is the first command!",
    scope=000000000000000,
)
async def button_test(ctx):
    await ctx.send("testing", components=button)


@client.command()
async def Application_Form(ctx):
    modal = interactions.Modal(
        title="Application Form",
        custom_id="mod_form",
        components=[interactions.TextInput(...)],
    )

    await ctx.popup(modal)


@client.command(aliases=["ctp", "capturethephoenix"]) # still buggy but fix will be implemented soon !
@commands.has_permissions(administrator=True)
async def catchthephoenix(ctx, member: discord.Member=None):
    points = {ctx.author: 0, member: 0}
    random_time = random.randrange(30)

    game = False
    if member is None:
        await ctx.send("...")
    elif member == client.user:
        await ctx.send("...")
    elif member.client:
        await ctx.send("...")
    else:
        game = True

    await ctx.send("The phoenix has been caught!")
    while True:
        try:
            await asyncio.sleep(random_time)
            await ctx.send(...)
            message = await client.wait_for(
                "message",
                check=lambda m: m.author.id == ctx.author.id,
                timeout=45.0
            )
        except asyncio.TimeoutError:
            game = False
            await ctx.send("The game has ended due to inactivity.")
        if not message.content.lower() == "catch":
            continue
        if message.author.id == member.id:
            await ctx.send(f"{member.mention} caught the phoenix!")
        elif message.author.id == ctx.author.id:
            ...


@catchthephoenix.error
async def ctp_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def lcp(ctx):
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="C:/path/to/your/audiofile.mp3"))
        await ctx.send("Connected to " + channel)
        while vc.is_playing():
            await asyncio.sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + " is not in a channel.")

# Removed Section End #


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def vip_dm(ctx):
    guild = client.get_guild(id=0000000000000) # guild ID here #
    role = discord.utils.get(guild.roles, id=00000000000000) # vip role goes here #
    member = guild.get_member(ctx.message.author.id)
    await member.add_roles(role)


@vip_dm.error
async def vipdm_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.has_permissions(administrator=True)
async def keyword(ctx, *, word: str):
    channel = client.get_channel(00000000000) # selected channel for keyword search #
    messages = await ctx.channel.history(limit=200).flatten()

    for msg in messages:
        if word in msg.content:
            await ctx.send(msg.jump_url)


@keyword.error
async def kw_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the needed permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error

# ===================================================================================================================== #
hug_gifs = ['https://c.tenor.com/nHkiUCkS04gAAAAC/anime-hug-hearts.gif']   
hug_names = ['Hugs you!']                                                  
# ===================================================================================================================== #


@client.command()
async def hug(ctx):
    embed = discord.Embed (
        colour=(discord.Colour.red()),
        description = f"{ctx.author.mention} {(random.choice(hug_names))}"
    )
    embed.set_image(url=(random.choice(hug_gifs)))

    await ctx.send(embed = embed)


@client.command()
async def rob(ctx):
    if random.randint(0, 100) <= 45:
        await ctx.send("Robbery has failed.")
    else:
        await ctx.send("Robbery was successful.")


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
@commands.cooldown(1, 160, commands.BucketType.user)
async def Prime(ctx):
    embed = discord.Embed(
            color= discord.Colour.dark_theme()
        )
    embed.add_field(name='Use Amazon Prime on Twitch:' ,value='[Click here to view]( https://twitch.amazon.com/tp )', inline=False)
    await ctx.send(embed=embed)


@Prime.error
async def prime_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 1000, commands.BucketType.user)
async def timer(ctx):
    await ctx.send(f'Starting Countdown in less than 10 seconds')
    await asyncio.sleep(10)
    await ctx.send(f'Starting Countdown now...')
    await asyncio.sleep(1)
    await ctx.send(f'3...')
    await asyncio.sleep(1)
    await ctx.send(f'2...')
    await asyncio.sleep(1)
    await ctx.send(f'1...')
    await asyncio.sleep(1)
    await ctx.send(f'GO Wondertrade')
    await asyncio.sleep(60)
    await ctx.send(f'Trades finished succesfully | Thanks for Trading')


@timer.error
async def wtimer_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 200, commands.BucketType.user)
async def blackjack(ctx):
    choices = ['You Won the Blackjack', 'You Lost the Blackjack', 'Tied']
    rancoin = random.choice(choices)
    await ctx.send(f'Shuffleling Cards [20 seconds]')
    await asyncio.sleep(20)
    await ctx.send(f'Making Choice Now [10 seconds]')
    await asyncio.sleep(10)
    await ctx.send(f'I choose this One...')
    await asyncio.sleep(5)
    await ctx.send(rancoin)


@blackjack.error
async def blackjack_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))


@bottles.error
async def bottles_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command(help="Play with .rps [your choice]")
@commands.cooldown(1, 180, commands.BucketType.user)
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"**Rock, paper, or scissors? Choose wisely...**")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")


@rps.error
async def rps_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def Sub(ctx):
    embed = discord.Embed(
            color= discord.Colour.dark_magenta()
        )
    embed.add_field(name='Subscribe here' ,value='[Click here to view]( https://www.twitch.tv/products/shinyhunter2109 )', inline=False)
    await ctx.send(embed=embed)


@Sub.error
async def Sub_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**This command is ratelimited, please try again in {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.has_permissions(administrator=True)
async def PreRelease(ctx):
    await ctx.send(f'**Checking for Pre-Release Updates...**')
    await asyncio.sleep(10)
    await ctx.send(f'**Pre Release Version found: Build: **{PR}** uploaded by **{PRUploader}**')
    await asyncio.sleep(10)
    await ctx.send(f'Next Pre Version will be released on: **{PRDate}** with Version **{NPR}** | Expected Downtime: **{Downtime}** hours')
    await asyncio.sleep(15)
    embed = discord.Embed(
            color= discord.Colour.dark_gold()
        )
    embed.add_field(name='Pre-Release Version' ,value='[Click here to download]( https://github.com/Shinyhunter2109/Discord-Moveset-Bot/releases/download/8.0.1/Discord-Moveset-Bot.zip )', inline=False)
    await ctx.send(embed=embed)


@PreRelease.error
async def pre_ver_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**These are Pre Released Updates and they only contain Bug-Fixes !.**'
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def BN(ctx):
    guild = ctx.guild
    await guild.create_role(name="Battle.net")
    await asyncio.sleep(10)
    await ctx.send(f'**Role has been created**')


@client.command()
async def Com_Help(ctx):
    guild = ctx.guild
    await guild.create_role(name="Community Helper")
    await asyncio.sleep(10)
    await ctx.send(f'**Role has been created**')


@client.command()
async def Communit_Help(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Community Helper")
    user = ctx.message.author
    await user.add_roles(role)


@client.command()
async def pokedex(ctx):
    await ctx.send(f'There are over 1000 Pokemon on the Pokedex!')


@client.command()
async def translate(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)


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


async def clear(ctx, amount: int, password: str):
    """Deletes Messages from the .env File."""
    if password != CLEAR_PASSWORD:
        await ctx.send("❌ Wrong Password")
        return

    if amount <= 0 or amount > 200:
        await ctx.send("⚠️ Please enter a number")
        return

    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 {len(deleted) - 1} Message(s) deleted.", delete_after=5)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = '**You dont have the right permissions to execute this command.**'
        await ctx.send(msg)
    else:
        raise error



# Movesets PKMN End #


# Slash Commands #

# Please note this will only work with Version 3.0.3 #

@slash.slash(name="ping", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send("Pong!")


@slash.slash(name="slash", guild_ids=guild_ids)
async def _slash(ctx):
    await ctx.send("**Slash Commands are now officially Supported!**")


@slash.slash(name="emotes", guild_ids=guild_ids)
async def _emotes(ctx):
    await ctx.send("**We now have some new cool Emotes from my Twitch Channel | Check it out !**")


@slash.slash(name="subicons", guild_ids=guild_ids)
async def _subicons(ctx):
    await ctx.send("**We now have some new cool Subicons on my Twitch Channel | Check it out if u want !**")


@slash.slash(name="pokedex", guild_ids=guild_ids)
async def _pokedex(ctx):
    await ctx.send(f'**There are over 800 Pokemon on the Pokédex !**')
    await asyncio.sleep(5)
    await ctx.send(f'**You can search for any Pokémon by typing /Pokemon [Pokémonname] | When  Bot is Online you will get the Results if not wait till its back Online**')


@slash.slash(name="tbi", guild_ids=guild_ids)
async def _tradebotinfo(ctx):
    await ctx.send('**The Link-Trade-Bot is exclusive on my Discord and Twitch Channel | If you want to use it leave a Follow on Twitch and Join on the Discord Server to get Permissions**')
    await asyncio.sleep(5)
    await ctx.send('**The Trading Bot on Twitch wont be able to handle Custom Requests**')


@slash.slash(name="version", guild_ids=guild_ids)
async def _version(ctx):
    await ctx.send(f'The Latest Version is: **{Version}**')


# Client Event Section #
#========================================================================================================== #

@client.command()
async def dispatch_custom(ctx):
    client.dispatch("custom_event has been started", ctx)


@client.event
async def on_custom_event(ctx):
    print("Custom event : ERROR | Try again later !")


@client.event
async def on_message_delete(message):
    if len(message.mentions) == 0:
        return
    else:
        print(message.author.name)
        ghostping = discord.Embed(title=f'GHOSTPING', color=0xFF0000, timestamp=message.created_at)
        ghostping.add_field(name='**Name:**', value=f'{message.author} ({message.author.id})')
        ghostping.add_field(name='**Message:**', value=f'{message.content}')
        ghostping.set_thumbnail(
            url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXtzZMvleC8FG1ExS4PyhFUm9kS4BGVlsTYw&usqp=CAU')
        try:
            await message.channel.send(embed=ghostping)
        except discord.Forbidden:
            try:
                await message.author.send(embed=ghostping)
            except discord.Forbidden:
                return


@client.event
async def on_raw_reaction_add(payload):
    channel = await client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)

    if payload.user_id == client.user.id:
        return

    if payload.message_id == 792058195714899998 and reaction.emoji == '✅':
        roles = discord.utils.get(guild.roles, name='Verify')
        await member.add_roles(roles)
        await reaction.remove(payload.member)


@client.event
async def on_member_update(before, after):
        if after.guild.id == 00000000000: # Your Guild ID here #
            if before.activity == after.activity:
                return

            role = get(after.guild.roles, id=0000000000000) # Your role goes here #
            channel = get(after.guild.channels, id=000000000000) # channel goes here #

            async for message in channel.history(limit=200):
                if before.mention in message.content and "is now streaming" in message.content:
                    if isinstance(after.activity, Streaming):
                        return

            if isinstance(after.activity, Streaming):
                await after.add_roles(role)
                stream_url = after.activity.url
                stream_url_split = stream_url.split(".")
                streaming_service = stream_url_split[1]
                streaming_service = streaming_service.capitalize()
                await channel.send(f":red_circle: **LIVE**\n{before.mention} is now streaming on {streaming_service}!\n{stream_url}")
            elif isinstance(before.activity, Streaming):
                await after.remove_roles(role)
                async for message in channel.history(limit=200):
                    if before.mention in message.content and "is now streaming" in message.content:
                        await message.delete()
            else:
                return
            

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**Invalid command used.**')


@client.event
async def on_permission_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**You dont have the right Permissions to execute this command.**')


@client.event
async def on_voice_state_update(member, before, after):
    if member.id == client.user.id and after.channel == None and before.channel != None:
        voiceChannel = before.channel
        await voiceChannel.connect()


@client.event
async def on_guild_join(guild):
    channel = guild.text_channels[0]
    embed = discord.Embed(title=guild.name, description="Hello, how can I help your Server?")
    await channel.send(embed=embed)


@client.event()
async def on_thread_create(thread):
    if thread.name != 'approved':
        await thread.delete()


@client.event
async def on_slash_command_error(ctx, error):

    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You do not have permission to execute this command', hidden=True)

    else:
       await ctx.send('An unexpected error occured. Please contact the bot developer', hidden=True)
       raise error


@client.event
async def on_error(event, *args, kwargs):
    message = args[0]
    logging.warning(traceback.format_exc())
    await client.send_message(message.channel, "You caused an error!")
    print ('an error has occurred..!')


@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)
    print(f'{member} was given {role}')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

client.run(TOKEN)
