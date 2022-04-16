# bot.py
import os
import constant
import random
import requests
import json
import re
import discord
import sys

from dotenv import load_dotenv
from discord.ext import commands


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
blacklist_user = 'Cesar#3519'
"""
Bot implementation
"""
bot = commands.Bot(command_prefix="!")

@bot.command(name="ping", help="test function")
async def ping_pong(ctx):
    await ctx.send("pong")

@bot.command(name="addcard", help="Adds specific card to user preference")
async def add_card_pref(ctx, card_name=None):
    if ctx.author == blacklist_user:
        ctx.send("stfu lmao")
    if card_name:
        await ctx.send(f"Added card {card_name} to your preferences")
    await ctx.send(f"{ctx.author.mention}, you didn't specify a card")

@bot.command(name="helpme", help="Lists all commands and their intended use.")
async def help_command(ctx, command=None):
    if ctx.author == blacklist_user:
        ctx.send("stfu lmao")
    if not command:
        await ctx.send(constant.addcard_help_message)

"""
Added as a joke
"""
@bot.command(name="pog", help="")
async def pog(ctx):
    poggers_messages = [
        "poggy woggy", 
        "pogulus wogulus",
        "I hate braulio",
        "POGGERS"
    ]
    response = random.choice(poggers_messages)
    await ctx.send(response)

bot.run(TOKEN)

"""
Client implementation:
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{client.user} is connected to the following guild:")
    print(f"{guild.name}, id: {guild.id}")

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise

@client.event
async def on_message(message):
    if message.author == client.user: # So bot doesn't respond to its own messages. 
        return
    if message.content == "ping":
        await message.channel.send("pong")

client.run(TOKEN)
"""


"""
Code to iterate/get members of a server:

members = '\n - '.join([member.name for member in guild.members])
print(f'Guild Members:\n - {members}')
"""
# note to self: venv name = botenv