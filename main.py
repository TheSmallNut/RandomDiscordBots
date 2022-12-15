from discord.ext import commands
import API.secret as secret
import os
import discord
import asyncio

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)


async def loadModules():
    # Change "cogs" to your folder name
    for filename in os.listdir("./modules"):
        if filename.endswith(".py"):
            await bot.load_extension(f"modules.{filename[:-3]}")
            await bot.start(secret.DISCORD_BOT_TOKEN)


asyncio.run(loadModules())