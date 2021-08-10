import discord # Para conectarse con el bot
from discord.ext import commands # Importar los comandos
import datetime 
import random
from variables import (token)

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
    des = """
    Estos son mis comandos\n

    > Prefijo:  _

    > _ping: El bot te responde pong

    > _programacion: Ramas de la programación

    > _frontend: Ruta de aprendizaje frontend

    > _backend: Ruta de aprendizaje backend

    > _sum: Suma 2 números. Por ejemplo: **_sum 10 10**

    > _mult: Multiplica 2 números. Por ejemplo: **_mult 2 24**

    Hecho con amor ❤️\n

    """
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description= des,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.blue())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))


    await ctx.send(embed=embed)


#Ramas de la programacion
@client.command()
async def programacion(ctx):
    des = """
    Ramas de la programación\n

    > **Programación Web**: 
    Cuando hablamos de la web, nos referimos a todo aquello que puede funcionar sobre un navegador (Chrome, Firefox, Internet Explorer, Edge, Safari)\n
    > **Programación Mobile**: 
    Se refiere al desarrollo de aplicaciones para teléfonos celulares\n
    > **Machine Learning**: 
    Se encarga de los sistemas de aprendizaje automático a partir del suministro de grandes volúmenes de datos\n
    > **Programación de Videojuegos**: 
    Si tienes la suerte de arrancar en un proyecto de cero podrás participar de la etapa de generación de ideas y de “stories” para el nuevo juego, del modelado y diseño de niveles. Si no tienes esa suerte, por lo general, colaboras con las tareas de prueba de los juegos desarrollados, creando casos de prueba automatizados y reportando mejoras\n
    > **Programación Embebida**: 
    Se trata de programas sencillos que están incorporados a una placa electrónica o chip. Por lo general, se encuentran instalados en electrodomésticos\n
    > **Programación Desktop**: 
    Son sistemas que requieren ser instalados en el sistema operativo de la computadora del usuario, ya sea, Windows, MacOS o Linux\n
    > **Programación de Sistemas Operativos**: 
    Se trata del desarrollo y/o mantenimiento de sistemas operativos

    """
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description= des,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.red())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))


    await ctx.send(embed=embed)


#Guia frontend
@client.command()
async def frontend(ctx):
    des = """
    Habilidades necesarias para ser un desarrollador frontend\n

    > **HTML - CSS - JavaScript**\n
    > **Frameworks/Librerias de JavaScript**: 
    React, Angular, Vue o Svelte\n
    > **Frameworks/Pre procesadores de CSS**: 
    Bootstrap / TailwindCSS / Chakra UI y Sass\n
    > **Diseño**: 
    UX - UI\n
    > **Linea de comandos/Version de control**: 
    Git y Github/Gitlab/Bitbucket\n
    > **Pruebas**: 
    Jest para pruebas unitarias o de integracion. Cypress para realizar pruebas funcionales\n
    > **Herramientas de automatización**: 
    Webpack, ESLint, Prettier\n
    > **Herramientas del navegador**: 
    Dev tools

    """
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description= des,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.red())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))


    await ctx.send(embed=embed)


#Guia backend
@client.command()
async def backend(ctx):
    des = """
    Habilidades necesarias para ser un desarrollador backend\n

    > **Servidores web**:
    Procesar aplicaciones del lado del servidor \n
    > **HTTP**: 
    GET, POST, PUT, DELETE\n
    > **Base de datos**: 
    SQLite, SQLServer, MySQL, PostgreSQL, MongoDB, etc\n
    > **Patrones de arquitectura**: 
    MVC (Modelo Vista Controlador), microservicios, monolíticos, CQRS\n
    > **Autenticación**: 
    Manejar tokens (JSON Web Tokens), encriptar contraseñas, manejo de sesiones, manejo de middlewares para hacer validaciones\n
    > **WebSockets**: 
    Manejar información en tiempo real\n
    > **Lenguajes y frameworks**: 
    Java - Spring\n
    PHP - Laravel (o Simfony)\n
    Ruby - Ruby on Rails\n
    JavaScript (Node.js) - Express\n
    Python - Django\n
    C# - .NET\n
    > **Linea de comandos / Control de versiones**: 
    Git y Github / Gitlab / Bitbucket

    """
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description= des,
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
    mr_robot_quotes = [
        "Lo estás perdiendo, chico. Solo se suponía que iba a ser tu profeta, y se suponía que tú serías mi dios.",
        "Dale a un hombre una pistola y atracará un banco, pero dale a un hombre un banco y atracará el mundo.",
        "Una cosa es cuestionar tu mente y otra es cuestionar tus ojos y oídos. ¿Pero acaso no es lo mismo?",
        "Demonios… No paran de trabajar. Siempre están activos. Ellos seducen. Ellos manipulan. Son nuestros dueños.",
        "Los gobiernos del mundo y sus líderes corporativos no quieren que hablemos, ¿por qué?. Porque liberamos verdades, destapamos villanos, exorcizamos demonios.",
        "Después de todo ¿No es por eso por lo que nos rodeamos de tantas pantallas? ¿Para poder evitar vernos?",
        "Queremos estar sedados. Porque es doloroso no fingir, porque somos cobardes.",
        "En 90 segundos, este código cambiara, si no lo usa para acceder desde mi ordenador antes de entonces, habré perdido contra el tiempo.",
        "El mundo en sí es un gran engaño.",
        "Puede que las guerras no se ganen. Puede que simplemente continúen en el tiempo.",
        "La política es para las marionetas",
        "Antes de que abras cualquier puerta hay un mundo lleno de posibilidades delante de ti. Y no es hasta que la abres cuando se hacen realidad.",
        "Solo estás viendo lo que hay delante de ti. No estás viendo lo que hay encima de ti."
    ]
    if message.content == 'mr robot' or message.content == "Mr robot" or message.content == "Mr Robot":
        response = random.choice(mr_robot_quotes)
        await message.channel.send(response)
    await client.process_commands(message)


#Cambiar el estado del bot
@client.event
async def on_ready():
    #Playing status
    await client.change_presence(activity=discord.Game(name="Hacking..."))
    print('My bot is ready')




client.run(token)