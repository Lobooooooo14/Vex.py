import disnake
from disnake.ext import commands
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl

from datetime import timedelta

import config

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.Cog.listener()
	async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error: commands.CommandError):

		if isinstance(error, commands.CommandOnCooldown):
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			second = str(round(error.retry_after, 2))

			if day > 0:
				waiting_time = str(day) + 'dia' if len(day) == 1 else 'dias'
			elif hour > 0:
				waiting_time = str(hour) + 'hora' if len(hour) == 1 else 'horas'
			elif minute > 0:
				waiting_time = str(minute) + 'minuto' if len(minute) == 1 else 'minutos'
			else:
				waiting_time = second + 'segundo' if len(second) <= 1 else 'segundos'

			embed = disnake.Embed(
					title=f'{E.error}Comando em cooldown!',
					description=f'{inter.author.mention}, este comando está em cooldown, você só poderá executá-lo novamente em `{waiting_time}`.',
					color=C.error)
			embed.set_image(url=MediaUrl.commandoncooldownbanner)
			embed.set_footer(text='Você está executando comandos rapidamente!')
			await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NotOwner):
				embed = disnake.Embed(
					title=f'{E.error}Não desenvolvedor!',
					description='Apenas pessoas especiais podem utilizar este comando.',
					color=C.error)
				embed.set_image(url=MediaUrl.notownerbanner)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.MissingPermissions):
				embed = EB(
						title=f'{E.error}Sem permissão!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Você preciza das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Você preciza da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=C.error)
				embed.set_image(url=MediaUrl.missingpermissionsbanner)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.BotMissingPermissions):
				embed = EB(
					title=f'{E.error}Não autorizado!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Eu precizo das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Eu precizo da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=C.error)
				embed.set_image(url=MediaUrl.botmissingpermissionsbanner)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NoPrivateMessage):
				embed = EB(
					title=f'{E.error}Apenas para servidores!',
						description='Este comando só pode ser utilizado em servidores!', 
						color=C.error) 
				embed.set_image(url=MediaUrl.noprivatemessagebanner)
				await inter.send(embed=embed, ephemeral=True)
		else:
			print(error)
	
	
def setup(bot):
	bot.add_cog(Events(bot))
