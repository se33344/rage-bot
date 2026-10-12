import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding='UTF-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Ready!")

@bot.command()
@commands.has_role("━ Generator Access ━")
async def generate(ctx):
    await ctx.reply("Ai primit un fivem ready in privat!")
    await ctx.author.send(f"{ctx.author.mention} FiveM Ready ia la muie")

@generate.error
async def generate_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.reply("Nu ai permisiunea de a genera un fivem ready!")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
