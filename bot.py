import discord
import requests
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def pokemon(ctx, arg):
    try: 
        pokemon =  arg.split(' ', 1)[0]### para obtener el pokemon que escrib el usuario eliminarle los espacios a lo que escriba el usuario 
        result=requests.get('https://pokeapi.co/api/v2/pokemon/'+ pokemon)  ###agregarle el pokemon que escribio el usuario al enlace d ela api

        if result.text == 'Not found':
            await ctx.send('pokemon no encontrado en la api')
        else:
            image_url = result.json()['sprites']['front_default']  ### para acceder a la clave sprites que está en el link de la api
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print('Error',e)

@bot.command()
async def limpiar(ctx):
    await ctx.send.purge()
    await ctx.send('mensajes eliminados', delete_after = 3)


####funcion con la cual detectará cuando la persona a dado el comando pokemon pero no ha añadido argumentos y le diga al usuario que debe enviar argumentos
@pokemon.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('tienes que pasarme el nombre de un pokemon como argumento')  ###limpiar el canal 3 seg despues de enviar el comando limpiar
    



bot.run("YOUR DICORD BOT'S TOKEN HERE")
