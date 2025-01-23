import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "==", intents = intents)

@bot.event
async def on_ready():
    print(f"Bot iniciado{bot.user}")

@bot.command(name="Hi")
async def welcome(ctx):
    await ctx.send("Hello")

@bot.command(name = "File")
async def file(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save (f"./{attachment.filename}")
            await ctx.send(f"Guarda la imagen en ./{attachment.filename}")
    else:
        await ctx.send("No subiste el archivo :(")

bot.run(token)