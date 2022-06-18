from random import randint
from PIL import ImageColor
from colorir import sRGB, HSV


class Colors:
	success = 0x38c48c
	error   = 0xff045c
	general = 0xfad4fb
	
	
	def RGB2HEX(RGB):
		return ''.join(f'{i:02X}' for i in RGB)
	
	
	def HEX2RGBtuple(HEX):
		return ImageColor.getcolor(HEX, 'RGB')
	
	
	def RGB2HSVtuple(RGB):
		r, g, b = RGB
		H, S, V = sRGB(r, g, b).hsv(round_to=1)
		return H, S, V
	
	
	def HSV2RGBtuple(HSV_):
		h, s, v = HSV_
		R, G, B = HSV(h, s, v).sRGB()
		return R, G, B
	
	
	def genRGBtuple():
		return (randint(0, 255), randint(0, 255), randint(0, 255))


class Emojis:
	success = '<:svTick_sim:975225579479646258> | '
	neutral = '<:svTick_Neutro:975225608697159830> | '
	error = '<:svTick_Nao:975225649029578782> | '
	interrogation = '<:help:975225718822809650> | '
	unknown_file = '<:unknown_file:975886833181421661> | '
	unavailable_filter = '<:unavailable_filter:975888355051044874> | '
	architecture = '<:arquitetura:975501599633977404> | '
	disnake_icon = '<:disnake:975495299067965471> | '
	python_icon = '<:python:975497682149863444> | '
	botTag = '<:BOT:975225765836767252>'
	tools = '🛠️ | '
	entertainment = '🪀 | '
	image = '🖼️ | '
	owner = '🐺 | '
	administration = '⚙️ | '


class MediaUrl:
	noguildicon = 'https://i.postimg.cc/KvpGZvz3/9152fdef6eda843249ed83a5606fa745279afbae7681b1b33a8f1b43746cdb99-3.jpg'
	commandoncooldownbanner = 'https://i.postimg.cc/vHmfqMN7/102-Sem-Titulo-20220604000113.png'
	notownerbanner = 'https://i.postimg.cc/QxVSBphr/102-Sem-Titulo-20220604001852.png'
	missingpermissionsbanner = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png'
	botmissingpermissionsbanner = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png'
	noprivatemessagebanner = 'https://i.postimg.cc/Twx8JtQS/102-Sem-Titulo-20220604141342.png'