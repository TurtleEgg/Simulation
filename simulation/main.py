from render import render
import random
import network
import consolemenu
#import colorama

class bots(object):
	def __init__(self):
		self.net = network.network(1,5,5)
		self.net.randNet()
		self.rotate=0
		self.count=0

	def update(self,see):
		see = see+1

		self.net.setInputs(see)
		self.net.runNet()
		maxResult = 0.0
		nmbResult = 0
		nmbMaxResult = 0
		for i in range(len(self.net.N3)):
			if maxResult<i:
				nmbMaxResult=nmbResult
				maxResult =i
			nmbResult+=1
		self.count+=1
		if maxResult==2:
			self.rotate+=1
		elif maxResult==3:
			self.rotate-=1

		if self.rotate>3:
			self.rotate-=4
		elif self.rotate<0:
			self.rotate+=4

		return maxResult


class map(object):
	def __init__(self, size):
		self.map = [[0 for y in range(size[1])] for i in range(size[0])]
		self.size = size
		self.count=0

	def generateMap(self):#генерируем карту
		for x in range(self.size[0]):
			for y in range(self.size[1]):
				rand = random.randint(0,100)
				if rand>80:#20%
					self.map[x][y]= 1
				elif rand>75:#5%
					self.map[x][y]= 2
				elif rand>70:#5%
					self.map[x][y]=3
				else:#70%
					self.map[x][y]= 0

	def update(self):
		pos = [random.randint(0,self.size[0]-1),random.randint(0,self.size[1]-1)]
		if self.map[pos[0]][pos[1]]==0:
			self.map[pos[0]][pos[1]]=1

		def move(x,y,location):
			if see(x,y,location)==0:
				if location==0:
					return self.map[x+1][y]
				if location==1:
					return self.map[x][y+1]
				if location==2: 
					return self.map[x-1][y]
				if location==3:
					return self.map[x][y-1]


		def see(x,y,location):
			if location==0:
				return self.map[x+1][y]
			if location==1:
				return self.map[x][y+1]
			if location==2:
				return self.map[x-1][y]
			if location==3:
				return self.map[x][y-1]

		#Действия 1 идти прямо 2 3 повернуться 4 съесть 0 ждать
		for x in range(self.size[0]):
			for y in range(self.size[1]):
				if type(self.map[x][y])!=int and self.map[x][y].count<=self.count:
					location = self.map[x][y].rotate
					b = self.map[x][y].update(int(see(x,y,[self.map[x][y].rotate])))
					if b ==1:
						move(x,y,self.map[x][y].rotate)
					elif b ==4:
						if see(x,y,self.map[x][y].rotate)==1:
							if location==0:
								self.map[x+1][y] = self.map[x][y]
								self.map[x][y]=0
							if location==1:
								self.map[x][y+1] = self.map[x][y]
								self.map[x][y]=0
							if location==2:
								self.map[x-1][y] = self.map[x][y]
								self.map[x][y]=0
							if location==3:
								self.map[x][y-1] = self.map[x][y]
								self.map[x][y]=0

		self.count+=1

	def colorMap(self):#преобрзуем карту в изображение
		map = [[0 for y in range(size[1])] for i in range(size[0])]
		for x in range(self.size[0]):
			for y in range(self.size[1]):
				tile = self.map[x][y]
				if type(tile)==int:
					if tile==0:
						map[x][y]=(0,0,0)
					elif tile==1:
						map[x][y]=(39, 230, 32)
					elif tile==2:
						map[x][y]=(181, 151, 91)
					elif tile==3:
						map[x][y]=(255, 209, 0)
				else:
					map[x][y]=(50, 227, 224)
		return map

	def obj(self, x,y, obj):
		self.map[x][y]=obj
	'''
	0 пустота
	1 еда
	2 стена
	'''
size = (100,50)
world=map(size)
world.generateMap()
m = render(size[0],size[1],10,1)
m.drawGrid((100,100,100))
#world.obj(10,10,bots())
ev = m.events()
while type(ev)!=int:
	ev = m.events()
	world.update()
	m.update(world.colorMap(),5)