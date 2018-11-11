import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime
import random

chat_filter = ["GIRAFFE", "SHIT"]
calendar_list = ["CALENDAR", "CHECK CALENDAR", "DATE", "NOVEMBER", "DECEMBER", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "MONTH", "YEAR", "DAY"]
pyth_ar = ["Type `Commands` for more interesting conversations", "That's my name", "What's up!", "**Type** `Commands` **for more interesting conversations**"]
hi_ar = ["Hello.", "What's up!", "still here", "Talking to me?"]
time_list = ["TIME", "CLOCK", "HOUR", "MINUTE", "TIMEZONE" "UPTIME" "RUNTIME" "STARTUP"]
x = datetime.datetime.now()

Client = discord.Client()
bot = commands.Bot(command_prefix = "")
@bot.event
async def on_ready():
        print("Bot is connected to Discord")

@bot.event
async def on_message(message):
    if message.content.upper().startswith('CLAP'):
            await bot.send_message(message.channel, "What :clap: you :clap: think :clap: that :clap: we :clap: think :clap: is :clap: cool")

    elif message.content.upper().startswith('HI'):
            await bot.send_message(message.channel, random.choice(hi_ar))

    elif message.content.upper().startswith('WHAT ARE Y'):
            await bot.send_message(message.channel, "I'm a GIRAFFE!")

    elif message.content.upper().startswith('WHO ARE Y'):
            await bot.send_message(message.channel, "I'm Pyth")

    elif message.content.upper().startswith('CODE'):
            await bot.send_message(message.channel, "origin...")

    elif message.content.upper().startswith('LANG'):
            await bot.send_message(message.channel, ":snake:")

    elif message.content.upper().startswith('ORIGIN'):
            await bot.send_message(message.channel, "made with code :snake:")

    elif message.content.upper().startswith('PYTH'):
            await bot.send_message(message.channel, random.choice(pyth_ar))

    elif message.content.upper().startswith('COMMANDS'):
            await bot.send_message(message.channel, "\n####### **COMMANDS** #######\n -   **Hi**\n -   **Lang / Language**\n -   **Pyth**\n -   **What/Who are you?**\n -   **Clap**\n -   **Origin**\n -   You can ask me freely about my time since startup, date and the calendar! :snake:\n")


    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, "```diff\n- That word is out of the function\n```") # You can change what words it reacts to with anger in the list named chat_filter
                except discord.errors.NotFound:
                    return
        if word.upper() in calendar_list:
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, x.strftime("It's %d %B %Y"))  # month/date array
                except discord.errors.NotFound:
                    return
        if word.upper() in time_list:
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, x.strftime("I have been awake since %H:%M:%S %d %B"))  # time_array, note that it only shows time since startup since the problem isn't yet fixed
                except discord.errors.NotFound:
                    return

bot.run("client secret") #CAN BE FOUND AT https://discordapp.com/developers/applications/ then on your bots general info page (click reveal then copy pastaaa)
