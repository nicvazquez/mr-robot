import discord
from discord.ext import commands, tasks
import random
from variables import (token)
from commandsText.help import help
from commandsText.programacion import programacion
from commandsText.frontend import frontend
from commandsText.backend import backend
from commandsText.quotes import mr_robot_quotes
from utilities.getEmbed import getEmbed
from getMemes import getMemes

helpVar = help
programacionVar = programacion
frontendVar = frontend
backendVar = backend
client = discord.Client()

client  = commands.Bot(command_prefix='_', description="Fsociety Bot", help_command=None)

# Check the ping
@client.command() 
async def ping(ctx): 
    await ctx.send('Pong! in {0}'.format(round(client.latency, 1)) + 'ms')

# Help command
@client.command()
async def help(ctx):
    await ctx.send(embed = getEmbed(ctx, helpVar))

# Programming branches
@client.command()
async def programacion(ctx):
    await ctx.send(embed = getEmbed(ctx, programacionVar))

# Frontend guide
@client.command()
async def frontend(ctx):
    await ctx.send(embed = getEmbed(ctx, frontendVar))

# Backend guide
@client.command()
async def backend(ctx):
    await ctx.send(embed = getEmbed(ctx, backendVar))

# Answer a message
@client.event
async def on_message(message):
    userMsg = message.content.lower()
    if message.author == client.user:
        return
    if 'buen dia' in userMsg or 'buenas' in userMsg:
        await message.channel.send("Buen día!")
    elif 'buenas noches' in userMsg:
        await message.channel.send("Buenas noches!")
    elif 'chau' in userMsg or 'adios' in userMsg:
        await message.channel.send("Hasta la vista, baby!")
    elif 'hola' in userMsg:
        await message.channel.send("Hola! Como estás?")

    # Mr Robot random quotes
    if 'mr robot' in userMsg:
        response = random.choice(mr_robot_quotes)
        await message.channel.send(response)
    await client.process_commands(message)

# Send a meme every 12 hours
@tasks.loop(hours=12)
async def send_meme():
    message_channel = client.get_channel(874641359242412092)
    await message_channel.send(getMemes())
@send_meme.before_loop
async def before():
    await client.wait_until_ready()

# Change bot status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Hacking..."))
    print("Hello world!")

send_meme.start()
client.run(token)