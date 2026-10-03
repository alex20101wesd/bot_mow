from asyncio import wait

import discord                                                        #librerita dsicord
from discord.ext import commands
from app import generar_password

permisos = discord.Intents.default() 
permisos.message_content = True

catmeow = commands.Bot(command_prefix="/",intents=permisos)


@catmeow.event
async def on_ready():
    print(f"bot en linea {catmeow.user} ")

@catmeow.command()
async def hola(ctx):
    await ctx.send(f"**hola :slight_smile: , soy catmeow ¿en que puedo ayudarte** {ctx.author.mention} ?")

#crear un comando
@catmeow.command()
async def ayuda(ctx):
    await ctx.send(f"los comandos son /hola,/ayuda, /tonto, /ping, /info")

@catmeow.command()
async def tonto(ctx):
    await ctx.send(f"tonto tu abuela {ctx.author.mention} :rage: ")

@catmeow.command()
async def ping(ctx):
    await ctx.send("pong :thumbsup: ")

@catmeow.command()
async def info(ctx):
    await ctx.send(f"mi nombre es **{catmeow.user}** y mi id es **{catmeow.user.id}**")

@catmeow.command()
async def password(ctx,longitud:int):
    nueva_password = generar_password(longitud)
    await ctx.send(f"tu nueva contraseña es: **{nueva_password}** {ctx.author.mention} :lock: ")


catmeow.run("")