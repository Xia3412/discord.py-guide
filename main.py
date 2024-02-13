# importing the necessary modules

import discord
from discord.ext import commands

# Enabling all the intents for our discord bot

intents = discord.Intents.all()

# Creating an instance of the Bot class and setting up the command prefix

bot = commands.Bot(command_prefix = "!", intents = intents)

# Configuring an event that the bot will listen to when it comes online

@bot.event
async def on_ready():
   print(f"Logged in as {bot.user}")

# Making a "hello" command

@bot.command(aliases = ["HELLO", 'Hello'])
async def hello(ctx):
   await ctx.send(f"Hello {ctx.author.mention}")

@bot.command()
async def what_does_ctx_author_mention_do(ctx):
   await ctx.send(f"It will return a message with the user of the command being mentioned.. like this {ctx.author.mention}")

@bot.command()
async def what_does_ctx_author_id_do(ctx):
   await ctx.send(f"It will return a message with the User ID of the user who triggered the command.. like this:- {ctx.author.id}")

@bot.command()
async def what_does_ctx_author_name_do(ctx):
   await ctx.send(f"It will return a message with the username of the user who triggered the command.. like this:- {ctx.author.name}")

@bot.command()
async def what_does_ctx_author_avatar_url_do(ctx):
   await ctx.send(f"It will return a message with the url of the user's avatar who triggered the command.. like this:- ``{ctx.author.avatar.url}``")

@bot.command()
async def what_does_ctx_send_do(ctx):
   await ctx.send("Pretty self explanatory.. just **sends** a message")

@bot.command()
async def what_does_ctx_reply_do(ctx):
   await ctx.reply("This one's also pretty self explanatory.. just **replies** to the user's message who triggered the command")

# Running the bot using the bot.run() method

bot.run("INSERT YOUR BOT TOKEN HERE")