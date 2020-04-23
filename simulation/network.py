import random

class network(object):
	def __init__(self, In, Hide, Out):
		self.N1 = [0 for i in range(In)]#Входной 
		self.N2 = [0 for i in range(Hide)]#Средний
		self.N3 = [0 for i in range(Out)]#Выходной

		self.C1 = [[] for i in range(Hide)]#Связи между N1 и N2
		self.C2 = [[] for i in range(Out)]#Связи между N2 и N3

		self.count = (In, Hide, Out)#кол-во связей
		self.randNet()

	def setInputs(self,arr):
		self.N1=arr

	def randNet(self):
		#Заполнение весов C1
		for i in range(len(self.C1)):
			for y in range(len(self.N2)):
				self.C1[i].append(random.random())
		# C2
		for i in range(len(self.C2)):
			for y in range(len(self.N3)):
				self.C2[i].append(random.random())
	def setNet(self, C1, C2):
		self.C1 = C1
		self.C2 = C2


	def progonN1inN2(self):
		for i in range(len(self.N2)):
			result = 0
			for n in range(len(self.N1)):
				result += self.N1[n]*self.C1[i][n]
			self.N2[i] = result

	def progonN2inN3(self):
		for i in range(len(self.N3)):
			result = 0
			for n in range(len(self.N2)):
				result += self.N2[n]*self.C2[i][n]
			self.N3[i] = result

	def runNet(self):
		self.progonN1inN2()
		self.progonN2inN3()
		for i in range(len(self.N3)):
			self.N3[i] = 1/ self.N3[i]

if __name__ == '__main__':
	for i in range(1):
		net = network(2,5,5)
		net.setInputs([1,1])
		net.runNet()
		for i in net.N3:
			print(1/i)
	input()