import discord # Para conectarse con el bot
from discord.ext import commands # Importar los comandos
import datetime 
import random
from variables import (token)
from commandsText.help import help
from commandsText.programacion import programacion
from commandsText.frontend import frontend
from commandsText.backend import backend
from commandsText.quotes import mr_robot_quotes

helpVar = help
programacionVar = programacion
frontendVar = frontend
backendVar = backend
client = discord.Client()

# Declarando la variable bot para que nos ayude a conectarnos con éste
client  = commands.Bot(command_prefix='_', description="Bot Fsociety", help_command=None)

#Primer tarea del bot
@client.command() #Crea un comando
async def ping(ctx): #Funcion que se encarga de manejar ese comando
    await ctx.send('pong') #Envio del mensaje


#Comando help
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description = helpVar,
    timestamp = datetime.datetime.utcnow(),
    color = discord.Color.blue())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))


    await ctx.send(embed=embed)


#Ramas de la programacion
@client.command()
async def programacion(ctx):
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description = programacionVar,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.red())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))


    await ctx.send(embed=embed)

#Guia frontend
@client.command()
async def frontend(ctx):
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description = frontendVar,
    timestamp =datetime.datetime.utcnow(),
    color = discord.Color.red())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))


    await ctx.send(embed=embed)

#Guia backend
@client.command()
async def backend(ctx):
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description = backendVar,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.red())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))


    await ctx.send(embed=embed)

#Sumar 2 numeros
@client.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

#Multiplicar 2 numeros
@client.command()
async def mult(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne * numTwo)

#Enviar memes

#Responder a un mensaje
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'buen dia' or message.content == 'buen día' or message.content == 'Buen día' or message.content == 'Buen dia':
        await message.channel.send("Buen día!")
    elif message.content == 'buenas noches' or message.content == 'Buenas noches':
        await message.channel.send("Buenas noches!")
    elif message.content == 'chau' or message.content == 'Chau' or message.content == 'adios' or message.content == 'Adios':
        await message.channel.send("Hasta la vista, baby!")
    elif message.content == 'hola' or message.content == 'Hola' or message.content == 'hello' or message.content == 'Hello':
        await message.channel.send("Hola! Como estás?")

    #Frases random de mr robot
    if message.content == 'mr robot' or message.content == "Mr robot" or message.content == "Mr Robot":
        response = random.choice(mr_robot_quotes)
        await message.channel.send(response)
    await client.process_commands(message)


#Cambiar el estado del bot
@client.event
async def on_ready():
    #Playing status
    await client.change_presence(activity=discord.Game(name="Hacking..."))
    print("I'm alive")

client.run(token)