import discord
import components.handler
from importlib import reload

admins = []
with open("secrets/admins.txt") as adminFile:
    admins = [int(line.strip()) for line in adminFile.readlines()]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!reload" and message.author.id in admins:
        reload(components.handler)
        return

    components.handler.Handler().handle(message, client)

if __name__ == "__name__":
    with open("secrets/token.txt") as token:
        client.run(token.read().strip())