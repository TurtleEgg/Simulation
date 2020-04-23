import pygame


class render(object):
	def __init__(self, x,y,tileSize, gridSize=0):
		self.size = (x,y)
		self.tSize = tileSize
		self.sc = pygame.display.set_mode((x*tileSize,y*tileSize))
		self.clock = pygame.time.Clock()
		self.gSize = gridSize

	def update(self, param, time):
		for x in range(len(param)):
			for y in range(len(param[x])):
				self.draw((x,y),param[x][y])
		pygame.display.update()
		if time != 0:
			self.clock.tick(time)

	def updateSC():
		pygame.display.update()

	def events(self):
		ev = pygame.event.get()
		for i in ev:
			if i.type == pygame.QUIT:
				return 1
				exit()
		return ev

	def draw(self,pos,color):
		pygame.draw.rect(self.sc, color, (pos[0]*self.tSize + self.gSize, pos[1]*self.tSize + self.gSize, self.tSize - self.gSize*2, self.tSize - self.gSize*2))

	def drawGrid(self, color=(255,255,255)):
		for x in range(self.size[0]):
			for y in range(self.size[1]):
				pygame.draw.rect(self.sc, color, (x*self.tSize, y*self.tSize, self.tSize, self.tSize),self.gSize)

