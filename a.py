#Made By draco#5013 On Discord

import os
import collections
import discord
from discord.ext import commands
import requests
from datetime import datetime
import subprocess
import time
import json
import datetime
import random
import string
import pymongo
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role

bot = commands.Bot(command_prefix=".") // You can change this prefix if you wish too
bot.remove_command('help')
bot.remove_command('methods')

@bot.command()
@commands.is_owner()
async def nuke(ctx):
	await ctx.channel.purge(limit=100000)
	nuke = discord.Embed(title="This Channel Has Been Nuked", color=0x000000)
	nuke.set_image(url="https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif")
	nuke.set_footer(text="Made By draco#8888")
	await ctx.send(embed=nuke)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.gg/Xuzcia | .help MADE BY draco#3024'))
    print('The Bot Is Now Online')

@bot.command()
async def help(ctx):
    help = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪", color=0x000000, description="These Are The List Of All Of The Commands")
    help.add_field(name="Attack Help", value="Shows How To Send An Attack ", inline=False)
    help.add_field(name="Methods", value="Shows The List Of Methods", inline=False)
    help.add_field(name="Plans", value="Shows The Prices For Our Plans", inline=False)
    help.add_field(name="Rules", value="Shows The List Of Rules", inline=False)
    help.add_field(name="Tools", value="Shows The List Of Tools", inline=False)
    help.set_image(url="https://media.giphy.com/media/dUIMslugbMsdqMxDTf/giphy.gif")
    help.set_footer(text="Discord Bot Made By draco#8888")
    await ctx.send(embed=help)

@bot.command()
async def plans(ctx):
    plan = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙋𝙡𝙖𝙣𝙨",
        color=0x000000)
    plan.add_field(name="Bronze", value="$10 Montly | $15 Lifetime | Max Time 700 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Silver", value="$20 Montly | $25 Lifetime | Max Time 1000 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Gold", value="$30 Montly | $35 Lifetime | Max Time 1300 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Bronze Elite | Reseller", value="$60 Montly | $85 Lifetime | Max Time 700 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Silver Elite | Reseller", value="$105 Montly | $115 Lifetime | Max Time 1000 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Gold Elite | Reseller", value="$130 Montly | $160 Lifetime | Max Time 1300 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Wombo Combo", value="The Wombo Combo Includes The Stresser And The OVH | $30 Monthly $60 Lifetime", inline=False)
    plan.add_field(name="15 Second Cooldown", value="$10 Montly | Private Server Access", inline=False)
    plan.add_field(name="0 Second Cooldown", value="$15 Monthly | Private Server Access", inline=False)
    plan.set_image(url="https://78.media.tumblr.com/97985a52a131fb9c6e5d9e69f0761ae9/tumblr_oakqnqGPDy1toufq9o1_500.gif")
    plan.set_footer(text="DM One Of The Owners If You Want To Get Reseller And Get A Ip Blacklist Ip Blacklist is $1 For Each Ip")
    await ctx.send(embed=plan)

@bot.command()
@has_role("Xuzcia Customers")
async def attackhelp(ctx):
    welp = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 | 𝘼𝙩𝙩𝙖𝙘𝙠 𝙃𝙚𝙡𝙥",
        color=0x000000)
    welp.add_field(name="How To Send An Attack", value=".attack [Ip] [Port] [Time] [Method]", inline=False)
    welp.add_field(name="Attack Not Sending?", value="If Your Attack Does Not Send Check Api Status Or If The Bot Is Down Or If Your Plan Has Expired", inline=False)
    welp.set_image(url="https://media.giphy.com/media/l3yoX7tmuAIAc7xK1V/giphy.gif")
    await ctx.send(embed=welp)

@bot.command()
async def rules(ctx):
    rules = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙍𝙪𝙡𝙚𝙨",
        color=0x000000)
    rules.add_field(name="Hitting Government Website Or Anything That Has To Do With The Government", value="If We See A Government Website Or IP You Will Be Banned With No Refund", inline=False)
    rules.add_field(name="Spamming Attacks", value="This Is For If You Have 0 Cooldown Only It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.add_field(name="Going Over Max Time", value="If We See It Then It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.add_field(name="Hitting School Websites", value="If We See It Then It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.add_field(name="Hitting Dstats For More Than 1min", value="If We See It Then It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.set_image(url="https://25.media.tumblr.com/tumblr_mehprdpINP1rmbrwmo1_500.gif")
    await ctx.send(embed=rules)

@bot.command()
async def tools(ctx):
    tools = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙏𝙤𝙤𝙡𝙨",
        color=0x000000)
    tools.add_field(name="Portscan", value="Portscan An IP Address", inline=False)
    tools.add_field(name="IP Lookup", value="Shows The Details Of The IP", inline=False)
    tools.add_field(name="DNS Lookup", value="Shows A Domains DNS Records", inline=False)
    tools.add_field(name="Reverse DNS Lookup", value="Shows The DNS Of An IP", inline=False)
    tools.set_image(url="https://78.media.tumblr.com/9fa91a655bda33e0924be6aadcead788/tumblr_p45fduk1lp1vl8qxbo1_500.gif")
    await ctx.send(embed=tools)

@bot.command()
@has_role("Xuzcia Customers")
async def attack(ctx, host, port, time, method):
        requests.get('API HERE')
        sent = discord.Embed(title=f"𝘼𝙩𝙩𝙖𝙘𝙠 𝙎𝙚𝙣𝙩!:tm:", color=0x000000)
        sent.add_field(name="𝙃𝙤𝙨𝙩:", value=f"{host}", inline=False)
        sent.add_field(name="𝙋𝙤𝙧𝙩:", value=f"{port}", inline=False)
        sent.add_field(name="𝙏𝙞𝙢𝙚:", value=f"{time}", inline=False)
        sent.add_field(name="𝙈𝙚𝙩𝙝𝙤𝙙:", value=f"{method}", inline=False)
        sent.set_image(url="https://66.media.tumblr.com/2a8258d3cbb16be0e7e8b4febc59db8e/tumblr_p23kniu8Te1tdd07go1_500.gif")
        await ctx.send(embed=sent)
        cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
        await ctx.send(embed=cool)

@bot.command()
async def portscan(self,host):
    ports = requests.get('https://api.hackertarget.com/nmap/?q='+host)
    embed = discord.Embed(title='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',color=0x000000)
    embed.add_field(name='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=ports.text.replace(',','\n'))
    await self.send(embed=embed)

@bot.command()
async def lookup(self,host):
    geoip = requests.get('http://extreme-ip-lookup.com/json/'+host)
    embed=discord.Embed(title='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣',value=geoip.text.replace('<br>','\n'),inline=False)
    await self.send(embed=embed)

@bot.command()
async def dnslookup(self,host):
    dns = requests.get('https://api.hackertarget.com/dnslookup/?q='+host)
    embed=discord.Embed(title='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=dns.text.replace('<br>','\n'),inline=False)
    await self.send(embed=embed)

@bot.command()
async def reversedns(self,host):
    rev = requests.get('https://api.hackertarget.com/reversedns/?q='+host)
    embed=discord.Embed(title='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=rev.text.replace('<br>','\n'),inline=False)
    await self.send(embed=embed)

@bot.command()
@commands.is_owner()
async def logout(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='The Bot Is Now Down Until Further Notice', color=0x000000)
    embed.set_image(url="https://media1.tenor.com/images/a584b3270a8a6efb5cd2b022dc35f220/tenor.gif?itemid=17549764")
    await ctx.send(embed=embed)
    await bot.logout()

@bot.command()
async def logout_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You Do Not Have Permissions To Run This Command")
    else:
        raise error

@bot.command()
@commands.is_owner()
async def on(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="The Bot Is Now Online", color=0x000000)
    embed.set_image(url="https://media0.giphy.com/media/ignzsztxyI2hfogHIL/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
async def on_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You Do Not Have Permissions To Run This Command")
    else:
        raise error

@bot.command()
#@has_role("Xuzcia Customers")
async def methods(ctx):
	meth = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙈𝙚𝙩𝙝𝙤𝙙𝙨", description="***-Home Methods-***\nSTD\nUDP\nHEX\nHOLD|7200MAX\nFUZE\nBLEND\nEMBER-HOME\nUDPRAPE\nLDAP\nNTP\nUDPMIX\n***-AMP Methods-***\nDB2\nMEMCACHE\nCHARGEN\nWIZARD\nDOMINATE\n***-TCP Methods-***\nTCP\nTCPx\nVSE\nSYN-KILL\nACK-KILL\nFRAG\nZAP\n***-OVH Methods-***\nOVH\nOVHx\nOVH-KILL\n100UP-KILLER\n***-NFO Methods-***\nNFO\nNFOx\nNFO-KILL\n***-Hydra Methods-***\nHYDRA-KILLER\n***-Dedipath Methods-***\nDEDI-RAPE\n***-VPN Methods-***\nVPN-NULL\n***-Game Methods-***\nFN-LAG\nFN-DROP\nR6-KILL\n2K-CRASH\nRUST-RAPE\nARK-255\n***-Website Methods-***\nWEB-CRUSH\nCF-SOCKETS\nCF-ENGINE\nHTTP-STUN\n***-Other Methods-***\nCNC\nKILLALL", color=0x000000)
	meth.set_image(url="https://media1.giphy.com/media/Y3YH3vl7AxoadWHQ9c/giphy.gif")
	await ctx.send(embed=meth)

@bot.command()
@has_role("Xuzcia Customers")
async def resellerrules(ctx):
	resell = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙍𝙚𝙨𝙚𝙡𝙡𝙚𝙧 𝙍𝙪𝙡𝙚𝙨", color=0x000000)
	resell.add_field(name="**ALWAYS ADD THE BUYER**", value="**IF YOU FORGET TO ADD THE USER SHOW ME PROOF OF THE PAYMENT**", inline=False)
	await ctx.send(embed=resell)

@bot.command()
async def paymentmethods(ctx):
    pay = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙋𝙖𝙮𝙢𝙚𝙣𝙩 𝙈𝙚𝙩𝙝𝙤𝙙𝙨", description="Cashapp\nPaypal\nZelle\nVenmo\nBitcoin\nAmazon Giftcards\nPlaystation Giftcards\nXbox Giftcards\nApple Giftcards\nGoogle Pay Giftcards\nApple Music Giftcards", color=0x000000)
    await ctx.send(embed=pay)

@bot.command()
async def vpnprices(ctx):
    ovh = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙑𝙋𝙉 𝙋𝙧𝙞𝙘𝙚𝙨", color=0x000000)
    ovh.add_field(name="𝙓𝙪𝙯𝙘𝙞𝙖 𝘾𝙖𝙣𝙖𝙙𝙖 𝙊𝙑𝙃", value="$5 Monthly $15 Lifetime | Attack Notifications Included | 100% Uptime | No Log Policy", inline=False)
    ovh.add_field(name="𝙓𝙪𝙯𝙘𝙞𝙖 𝙇𝙖𝙨 𝙑𝙚𝙜𝙖𝙨 𝙁𝙧𝙖𝙣𝙩𝙚𝙘𝙝", value="$5 Monthly $15 Lifetime | Attack Notifications Included | 100% Uptime | No Log Policy", inline=False)
    await ctx.send(embed=ovh)

#@bot.command()
#async def add(ctx, user, plan):
 #   f = open("users.txt")
  #  f.write("User: "+user+" Plan: "+plan)
  #  add = discord.Embed(title=user+"Has Sucessfully Been Added To Xuzcia", color=0x000000)
   # await ctx.send(embed=add)

# READ This
#YOU HAVE HAVE ATTACK.TXT AND BLACKLISTED.TXT DM ON DISCORD draco#5013 IF YOU NEED ANY HELP IMPORTING THOSE INTO THE BOT

bot.run('ODE4ODIxMzkwMDk4MTA0MzMx.YEdo2A.nfjN4Op1SiWn2VysElnkzZ3w58k')




#Made By draco#5013 On Discord

import os
import collections
import discord
from discord.ext import commands
import requests
from datetime import datetime
import subprocess
import time
import json
import datetime
import random
import string
import pymongo
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role

bot = commands.Bot(command_prefix=".") // You can change this prefix if you wish too
bot.remove_command('help')
bot.remove_command('methods')

@bot.command()
@commands.is_owner()
async def nuke(ctx):
	await ctx.channel.purge(limit=100000)
	nuke = discord.Embed(title="This Channel Has Been Nuked", color=0x000000)
	nuke.set_image(url="https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif")
	nuke.set_footer(text="Made By draco#8888")
	await ctx.send(embed=nuke)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.gg/Xuzcia | .help MADE BY draco#3024'))
    print('The Bot Is Now Online')

@bot.command()
async def help(ctx):
    help = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪", color=0x000000, description="These Are The List Of All Of The Commands")
    help.add_field(name="Attack Help", value="Shows How To Send An Attack ", inline=False)
    help.add_field(name="Methods", value="Shows The List Of Methods", inline=False)
    help.add_field(name="Plans", value="Shows The Prices For Our Plans", inline=False)
    help.add_field(name="Rules", value="Shows The List Of Rules", inline=False)
    help.add_field(name="Tools", value="Shows The List Of Tools", inline=False)
    help.set_image(url="https://media.giphy.com/media/dUIMslugbMsdqMxDTf/giphy.gif")
    help.set_footer(text="Discord Bot Made By draco#8888")
    await ctx.send(embed=help)

@bot.command()
async def plans(ctx):
    plan = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙋𝙡𝙖𝙣𝙨",
        color=0x000000)
    plan.add_field(name="Bronze", value="$10 Montly | $15 Lifetime | Max Time 700 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Silver", value="$20 Montly | $25 Lifetime | Max Time 1000 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Gold", value="$30 Montly | $35 Lifetime | Max Time 1300 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Bronze Elite | Reseller", value="$60 Montly | $85 Lifetime | Max Time 700 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Silver Elite | Reseller", value="$105 Montly | $115 Lifetime | Max Time 1000 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Gold Elite | Reseller", value="$130 Montly | $160 Lifetime | Max Time 1300 Seconds | Cooldown 2 Minutes/85 Seconds", inline=False)
    plan.add_field(name="Wombo Combo", value="The Wombo Combo Includes The Stresser And The OVH | $30 Monthly $60 Lifetime", inline=False)
    plan.add_field(name="15 Second Cooldown", value="$10 Montly | Private Server Access", inline=False)
    plan.add_field(name="0 Second Cooldown", value="$15 Monthly | Private Server Access", inline=False)
    plan.set_image(url="https://78.media.tumblr.com/97985a52a131fb9c6e5d9e69f0761ae9/tumblr_oakqnqGPDy1toufq9o1_500.gif")
    plan.set_footer(text="DM One Of The Owners If You Want To Get Reseller And Get A Ip Blacklist Ip Blacklist is $1 For Each Ip")
    await ctx.send(embed=plan)

@bot.command()
@has_role("Xuzcia Customers")
async def attackhelp(ctx):
    welp = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 | 𝘼𝙩𝙩𝙖𝙘𝙠 𝙃𝙚𝙡𝙥",
        color=0x000000)
    welp.add_field(name="How To Send An Attack", value=".attack [Ip] [Port] [Time] [Method]", inline=False)
    welp.add_field(name="Attack Not Sending?", value="If Your Attack Does Not Send Check Api Status Or If The Bot Is Down Or If Your Plan Has Expired", inline=False)
    welp.set_image(url="https://media.giphy.com/media/l3yoX7tmuAIAc7xK1V/giphy.gif")
    await ctx.send(embed=welp)

@bot.command()
async def rules(ctx):
    rules = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙍𝙪𝙡𝙚𝙨",
        color=0x000000)
    rules.add_field(name="Hitting Government Website Or Anything That Has To Do With The Government", value="If We See A Government Website Or IP You Will Be Banned With No Refund", inline=False)
    rules.add_field(name="Spamming Attacks", value="This Is For If You Have 0 Cooldown Only It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.add_field(name="Going Over Max Time", value="If We See It Then It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.add_field(name="Hitting School Websites", value="If We See It Then It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.add_field(name="Hitting Dstats For More Than 1min", value="If We See It Then It Will Result In A Ban Or Removal From The Bot", inline=False)
    rules.set_image(url="https://25.media.tumblr.com/tumblr_mehprdpINP1rmbrwmo1_500.gif")
    await ctx.send(embed=rules)

@bot.command()
async def tools(ctx):
    tools = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙏𝙤𝙤𝙡𝙨",
        color=0x000000)
    tools.add_field(name="Portscan", value="Portscan An IP Address", inline=False)
    tools.add_field(name="IP Lookup", value="Shows The Details Of The IP", inline=False)
    tools.add_field(name="DNS Lookup", value="Shows A Domains DNS Records", inline=False)
    tools.add_field(name="Reverse DNS Lookup", value="Shows The DNS Of An IP", inline=False)
    tools.set_image(url="https://78.media.tumblr.com/9fa91a655bda33e0924be6aadcead788/tumblr_p45fduk1lp1vl8qxbo1_500.gif")
    await ctx.send(embed=tools)

@bot.command()
@has_role("Xuzcia Customers")
async def attack(ctx, host, port, time, method):
        requests.get('API HERE')
        sent = discord.Embed(title=f"𝘼𝙩𝙩𝙖𝙘𝙠 𝙎𝙚𝙣𝙩!:tm:", color=0x000000)
        sent.add_field(name="𝙃𝙤𝙨𝙩:", value=f"{host}", inline=False)
        sent.add_field(name="𝙋𝙤𝙧𝙩:", value=f"{port}", inline=False)
        sent.add_field(name="𝙏𝙞𝙢𝙚:", value=f"{time}", inline=False)
        sent.add_field(name="𝙈𝙚𝙩𝙝𝙤𝙙:", value=f"{method}", inline=False)
        sent.set_image(url="https://66.media.tumblr.com/2a8258d3cbb16be0e7e8b4febc59db8e/tumblr_p23kniu8Te1tdd07go1_500.gif")
        await ctx.send(embed=sent)
        cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
        await ctx.send(embed=cool)

@bot.command()
async def portscan(self,host):
    ports = requests.get('https://api.hackertarget.com/nmap/?q='+host)
    embed = discord.Embed(title='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',color=0x000000)
    embed.add_field(name='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=ports.text.replace(',','\n'))
    await self.send(embed=embed)

@bot.command()
async def lookup(self,host):
    geoip = requests.get('http://extreme-ip-lookup.com/json/'+host)
    embed=discord.Embed(title='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣',value=geoip.text.replace('<br>','\n'),inline=False)
    await self.send(embed=embed)

@bot.command()
async def dnslookup(self,host):
    dns = requests.get('https://api.hackertarget.com/dnslookup/?q='+host)
    embed=discord.Embed(title='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=dns.text.replace('<br>','\n'),inline=False)
    await self.send(embed=embed)

@bot.command()
async def reversedns(self,host):
    rev = requests.get('https://api.hackertarget.com/reversedns/?q='+host)
    embed=discord.Embed(title='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=rev.text.replace('<br>','\n'),inline=False)
    await self.send(embed=embed)

@bot.command()
@commands.is_owner()
async def logout(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='The Bot Is Now Down Until Further Notice', color=0x000000)
    embed.set_image(url="https://media1.tenor.com/images/a584b3270a8a6efb5cd2b022dc35f220/tenor.gif?itemid=17549764")
    await ctx.send(embed=embed)
    await bot.logout()

@bot.command()
async def logout_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You Do Not Have Permissions To Run This Command")
    else:
        raise error

@bot.command()
@commands.is_owner()
async def on(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="The Bot Is Now Online", color=0x000000)
    embed.set_image(url="https://media0.giphy.com/media/ignzsztxyI2hfogHIL/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
async def on_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You Do Not Have Permissions To Run This Command")
    else:
        raise error

@bot.command()
#@has_role("Xuzcia Customers")
async def methods(ctx):
	meth = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙈𝙚𝙩𝙝𝙤𝙙𝙨", description="***-Home Methods-***\nSTD\nUDP\nHEX\nHOLD|7200MAX\nFUZE\nBLEND\nEMBER-HOME\nUDPRAPE\nLDAP\nNTP\nUDPMIX\n***-AMP Methods-***\nDB2\nMEMCACHE\nCHARGEN\nWIZARD\nDOMINATE\n***-TCP Methods-***\nTCP\nTCPx\nVSE\nSYN-KILL\nACK-KILL\nFRAG\nZAP\n***-OVH Methods-***\nOVH\nOVHx\nOVH-KILL\n100UP-KILLER\n***-NFO Methods-***\nNFO\nNFOx\nNFO-KILL\n***-Hydra Methods-***\nHYDRA-KILLER\n***-Dedipath Methods-***\nDEDI-RAPE\n***-VPN Methods-***\nVPN-NULL\n***-Game Methods-***\nFN-LAG\nFN-DROP\nR6-KILL\n2K-CRASH\nRUST-RAPE\nARK-255\n***-Website Methods-***\nWEB-CRUSH\nCF-SOCKETS\nCF-ENGINE\nHTTP-STUN\n***-Other Methods-***\nCNC\nKILLALL", color=0x000000)
	meth.set_image(url="https://media1.giphy.com/media/Y3YH3vl7AxoadWHQ9c/giphy.gif")
	await ctx.send(embed=meth)

@bot.command()
@has_role("Xuzcia Customers")
async def resellerrules(ctx):
	resell = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙍𝙚𝙨𝙚𝙡𝙡𝙚𝙧 𝙍𝙪𝙡𝙚𝙨", color=0x000000)
	resell.add_field(name="**ALWAYS ADD THE BUYER**", value="**IF YOU FORGET TO ADD THE USER SHOW ME PROOF OF THE PAYMENT**", inline=False)
	await ctx.send(embed=resell)

@bot.command()
async def paymentmethods(ctx):
    pay = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙋𝙖𝙮𝙢𝙚𝙣𝙩 𝙈𝙚𝙩𝙝𝙤𝙙𝙨", description="Cashapp\nPaypal\nZelle\nVenmo\nBitcoin\nAmazon Giftcards\nPlaystation Giftcards\nXbox Giftcards\nApple Giftcards\nGoogle Pay Giftcards\nApple Music Giftcards", color=0x000000)
    await ctx.send(embed=pay)

@bot.command()
async def vpnprices(ctx):
    ovh = discord.Embed(title="𝙓𝙪𝙯𝙘𝙞𝙖 𝙎𝙩𝙧𝙚𝙨𝙨𝙚𝙧 | 𝙑𝙋𝙉 𝙋𝙧𝙞𝙘𝙚𝙨", color=0x000000)
    ovh.add_field(name="𝙓𝙪𝙯𝙘𝙞𝙖 𝘾𝙖𝙣𝙖𝙙𝙖 𝙊𝙑𝙃", value="$5 Monthly $15 Lifetime | Attack Notifications Included | 100% Uptime | No Log Policy", inline=False)
    ovh.add_field(name="𝙓𝙪𝙯𝙘𝙞𝙖 𝙇𝙖𝙨 𝙑𝙚𝙜𝙖𝙨 𝙁𝙧𝙖𝙣𝙩𝙚𝙘𝙝", value="$5 Monthly $15 Lifetime | Attack Notifications Included | 100% Uptime | No Log Policy", inline=False)
    await ctx.send(embed=ovh)

#@bot.command()
#async def add(ctx, user, plan):
 #   f = open("users.txt")
  #  f.write("User: "+user+" Plan: "+plan)
  #  add = discord.Embed(title=user+"Has Sucessfully Been Added To Xuzcia", color=0x000000)
   # await ctx.send(embed=add)

# READ This
#YOU HAVE HAVE ATTACK.TXT AND BLACKLISTED.TXT DM ON DISCORD draco#5013 IF YOU NEED ANY HELP IMPORTING THOSE INTO THE BOT

bot.run('TOKEN')


main.py
