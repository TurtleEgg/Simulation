import colorama
colorama.init()
from colorama import *
import os
#Размер консоли: 80 на 25
class consoleMenu(object):
	def __init__(self,size):
		self.size=size
		print(Style.BRIGHT,end='')
	def setMenu(self,buttons):
		os.system('cls')
		text = ''
		for i in buttons:
			symbols=self.size[0]
			for b in i:
				symbols-=(len(b)+1)
				text+=b+' '
			text+=(' '*symbols)
		print(text, end='')
		self.buttons=buttons
	def select(self,nmbB):
		os.system('cls')
		text = ''
		c=0
		for i in self.buttons:
			symbols=self.size[0]
			for b in i:
				symbols-=(len(b)+1)
				if c == nmbB:
					text+=Back.RED+Fore.YELLOW+b+Back.RESET+Fore.RESET+' '
				else:
					text+=b+' '
				c+=1
			text+=(' '*symbols)
		print(text, end='')


if __name__ == '__main__':
	import time
	menu = consoleMenu((80, 25))
	menu.setMenu([['buton1','button2'],['b3','b4']])
	for i in range(4):
		menu.select(i)
		time.sleep(1)
	menu.select(10)
	time.sleep(1)
	menu.setMenu([['new b1','button2'],['b3','b4']])
	for i in range(4):
		menu.select(i)
		time.sleep(1)
	input()