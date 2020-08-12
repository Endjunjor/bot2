import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
	print("Online")
	
	try:
		home = bot.get_guild(658117203866025995)
		role= home.get_role(743201327055634434)
		while True:
			color = [0xff0000, 0x000bff, 0x28ff00, 0xedff00, 0xff0084, 0xff7f00]
			r = random.choice(color)
			colors = discord.Colors(r)
			await role.edit(colour=colors)
			await asyncio.sleep(20)
	except Exeptions as error:
		print(error)


bot.run("NDgyNTMyNDk4NDQyODEzNDYx.W3__aA.gdVVMwDxdoDynGppfDDcfKP_-1M")
