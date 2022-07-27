# made by yux
# don't skid pls

import os
import requests
import json
import ascii2text
from discord.ext import commands
from colorama import Fore, Back, Style, init
import discord.utils
init()

tocopy = 000
overwrites_to = {}
topaste = 000

with open('config.json') as config_file:
	data = json.load(config_file)

bot = commands.Bot(command_prefix='server cloner made by yuxontop on github')



tocopy = input('server you want to copy : ')
topaste = input('server you want to paste in : ')


scrapped_channel = []
scrapped_category = []
scrapped_role = []

def get_overwrite(guild, channel):
	overwrites_to = {}
	for key, value in channel.overwrites.items():
		role = discord.utils.get(guild.roles, name=key.name)
		overwrites_to[role] = value
	return overwrites_to

@bot.event
async def on_ready():
	os.system('cls')
	print('Copying ...')
	
	for guild in bot.guilds:

		if int(guild.id) == int(tocopy):

			try:
				for category in guild.categories:
					scrapped_category.append(category)
					print(f'	[+] Copied Category : {category.name} in {guild.name}')
					for channel in category.channels:
						scrapped_channel.append(channel)
						print(Fore.GREEN + f'	[+] Copied Channel : {channel.name} in {category.name}')
			except:
				print(Fore.RED + f'	[X] Error Copying Channels')
				pass

			for role in guild.roles:
				try:
					scrapped_role.append(role)
					print(Fore.GREEN + f'	[+] Copied Role : {role.name} in {guild.name}')
				except:
					print(Fore.RED + f'	[X] Error Copying Role : {role.name} in {guild.name}')
					pass



	for guild in bot.guilds:
		if int(guild.id) == int(topaste):

			for channel in guild.channels:
				try:
					await channel.delete()
					print(Fore.GREEN + f'	[-] Deleted Channel : {channel.name} in {guild.name}')
				except:
					print(Fore.RED + f'	[X] Error Deleting Channel : {channel.name} in {guild.name}')
					pass

			for role in guild.roles:
				try:
					await role.delete()
					print(Fore.GREEN + f'	[-] Deleted Role : {role.name} in {guild.name}')
				except:
					print(Fore.RED + f'	[X] Error Deleting Role : {role.name} in {guild.name}')
					pass

			for category in scrapped_category:
				try:

					category_created = await guild.create_category(str(category.name), overwrites=get_overwrite(guild, channel))
					for channel in category.channels:
						if 'text' in str(channel.type):

						

							try:
								await guild.create_text_channel(str(channel.name), category=category_created, overwrites=get_overwrite(guild, channel), topic=channel.topic, position=channel.position, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw)
							except:
								await guild.create_text_channel(str(channel.name), category=category_created, overwrites=get_overwrite(guild, channel))

							print(Fore.GREEN + f'	[+] Pasted Text Channel : {channel.name} in {category.name}')
						elif 'voice' in str(channel.type):
							try:
								await guild.create_voice_channel(str(channel.name), category=category_created, overwrites=get_overwrite(guild, channel), bitrate=channel.bitrate, user_limit=channel.user_limit)
							except:
								await guild.create_voice_channel(str(channel.name), category=category_created, overwrites=get_overwrite(guild, channel))
							print(Fore.GREEN + f'	[+] Pasted Voice Channel : {channel.name} in {category.name}')
						else:
							print(Fore.RED + f'	[X] Error Pasting Channel : {channel.name} in {category.name}')
							pass
				except:
					pass

			for role in scrapped_role:
				try:
					await guild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
					print(Fore.GREEN + f'	[+] Pasted Role : {role.name} in {guild.name}')
				except:
					print(Fore.RED + f'	[X] Error Pasting Role : {role.name} in {guild.name}')
					pass

			print(Fore.YELLOW + f'\n\n\n FINISHED COPYING {tocopy} TO {topaste} !')
			input()
			os.system('cls')

bot.run(data['token'], bot=False) # if you use a bot token then set to True


#	enjoy !
