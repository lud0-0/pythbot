import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime
import random

chat_filter = ["SHIT"]
calendar_list = ["CALENDAR", "CHECK CALENDAR", "DATE", "NOVEMBER", "DECEMBER", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "MONTH", "YEAR", "DAY"]
pyth_ar = ["Type `Commands` for more interesting conversations", "That's my name", "What's up!", "**Type** `Commands` **for more interesting conversations**"]
time_list = ["TIME", "CLOCK", "HOUR", "MINUTE", "TIMEZONE"]
me_wordslist = ["AM", "I'M", "YOU'RE", "ME", "WHO AM I", "LOOK", "ME?", "YOU?", "YOU"]
youare_list = ["You might be a python snake.", "You look like a giraffe.", "I have no clue"]
uptime = datetime.datetime.now()
seven_magic_number = ["Yes 7", "just, magic", "S7e7v7e7n", "Somebody once told me the world was gonna roll me..."]
not_magic_nrs = ["1", "2", "3", "4", "5", "6", "8", "9", "0"]
no_good = ["What are you trying to say", "Just, no", "Please stop saying bad numbers", "You can not be serious"] #Pyth just likes 7, that's all
greatings_list = ["HI", "HELLO", "WHATSUP", "HELO", "HEY", "HEY!", "WHASSUP", "DOING", "DOIN", "DOIN'"]
hi_ar = ["Hello.", "What's up!", "still here", "Talking to me?"]
def datetime_now():
    time = datetime.datetime.now()
    result = time.strftime
    return result

Client = discord.Client()
bot = commands.Bot(command_prefix = "")
@bot.event
async def on_ready():
        print("Bot is connected to Discord")
@bot.event
async def on_message(message):
    if message.content.upper().startswith('CLAP'):
        if message.author != bot.user:
            await bot.send_message(message.channel, "What :clap: you :clap: think :clap: that :clap: we :clap: think :clap: is :clap: cool")
    elif message.content.upper().startswith('WHAT ARE Y'):
        if message.author != bot.user:
            await bot.send_message(message.channel, "I'm a GIRAFFE!")
    elif message.content.startswith('10'):
        if message.author != bot.user:
            await bot.send_message(message.channel, "That's not even a number, ha!")
    elif message.content.upper().startswith('WHO ARE Y'):
        if message.author != bot.user:
            await bot.send_message(message.channel, "I'm Pyth")
    elif message.content.upper().startswith('CODE'):
            await bot.send_message(message.channel, "origin...")
    elif message.content.upper().startswith('LANG'):
        if message.author != bot.user:
            await bot.send_message(message.channel, ":snake:")
    elif message.content.upper().startswith('ORIGIN'):
            await bot.send_message(message.channel, "I'm made with code :snake:")
    elif message.content.upper().startswith('PYTH'):
        if message.author != bot.user:
            await bot.send_message(message.channel, random.choice(pyth_ar))
    elif message.content.upper().startswith('UPTIME'):
        if message.author != bot.user:
            await bot.send_message(message.channel, uptime.strftime("I woke up at %H:%M:%S, %d %B %Y"))
    elif message.content.upper().startswith('COMMANDS'):
        if message.author != bot.user:
            await bot.send_message(message.channel, "\n####### **COMMANDS** #######\n -   **Hi**\n -   **Lang / Language**\n -   **Pyth**\n -   **What/Who are you?**\n -   **You are/You're [something]**\n -   **Clap**\n -   **Uptime**\n -   **Origin**\n -   You can ask me freely about time, date and the calendar! :snake:\n -   You can ask questions about yourself too :snake:\n -   *Remember, Pyth likes the number 7*")

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
                    await bot.send_message(message.channel, datetime_now()("It's the **%d %B %Y**"))  # month/date
                except discord.errors.NotFound:
                    return
        if word.upper() in time_list:
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, datetime_now()("*It's* %H:%M:%S"))  # time
                except discord.errors.NotFound:
                    return
        if word.upper() in not_magic_nrs:
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, random.choice(no_good))  # not liking numbers != 7
                except discord.errors.NotFound:
                    return
        if word.upper().startswith("7"):
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, random.choice(seven_magic_number))  # yes 7
                except discord.errors.NotFound:
                    return
        if word.upper().startswith("THIS"):
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, ("This. is. SPARTA!"))
                except discord.errors.NotFound:
                    return
        if word.upper() in greatings_list:
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, random.choice(hi_ar))
                except discord.errors.NotFound:
                    return
        if word.upper() in me_wordslist:
            if message.author != bot.user:
                try:
                    await bot.send_message(message.channel, random.choice(youare_list))  # answer to questions about youself
                except discord.errors.NotFound:
                    return

bot.run("secret key") #CAN BE FOUND AT https://discordapp.com/developers/applications/ then on your bots general info page (click reveal then copy pastaaa)