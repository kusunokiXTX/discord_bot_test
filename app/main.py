from core.start import DBot
import discord
import os

Token = os.environ.get("DISCORD_BOT_TOKEN")

# Bot立ち上げ
DBot(
    token=Token,
    intents=discord.Intents.all()
).run()
