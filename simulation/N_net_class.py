import numpy as np
import numpy.random as rand

class network(object):
    def __init__(self, NL=1, Nn=2, Ni=10, No=4, seed=8800, mutType =1, mutRate=0.5):
        #NL количество слоев
        #Nn количество нейронов в слое
        #Ni количество входов
        #No количество выходов
        #mutRate предел случайного измененеия значения при мутации
        #mutType =1 - меняются все нейроны на случайную величину в интервале -mutRate..mutRate;
        #mutType =2 - меняется один нейрон
        self.NL = NL
        self.Nn = Nn
        self.Ni = Ni
        self.No = No
        self.seed= seed
        self.mutRate=mutRate
        self.mutType=mutType
        rand.seed(seed)
        # W - матрицы весов
        # B - векторы порогов
        # Инициализируются случайные значения в диапазоне -1..1
        self.B = -np.ones((Nn, NL)) + 2 * rand.random((Nn, NL))
        self.W = -np.ones((Nn, Nn, NL))+ 2 * rand.random((Nn, Nn, NL))
        self.Bi = -np.ones((Nn))+ 2 * rand.random((Nn))
        self.Wi = -np.ones((Ni, Nn))+ 2 * rand.random((Ni, Nn))
        self.Bo = -np.ones((No))+ 2 * rand.random((No))
        self.Wo = -np.ones((No, Nn))+ 2 * rand.random((No, Nn))

    def go(self, In):
        NL = self.NL
        Nn = self.Nn
        Ni = self.Ni
        No = self.No
        B= self.B
        W= self.W
        Bi=self.Bi
        Wi=self.Wi
        Bo=self.Bo
        Wo=self.Wo


        L = np.zeros((Nn, NL)) #возбуждения нейронов

        L[:, 0] = np.sign(np.dot(Wi[:, 0], In) + Bi)

        for iL in range(1, NL):
            L[:, iL] = np.sign(np.dot(W[:, :, iL], L[:, iL - 1]) + B[:, iL])

        Out = np.sign(np.dot(Wo, L[:, NL - 1]) + Bo)
        self.L=L
        return Out

    def mutate(self):
        rand.seed()
        rate=self.mutRate
        NL = self.NL
        Nn = self.Nn
        Ni = self.Ni
        No = self.No

        if self.mutType==1:
            self.B += rate * (-1+ 2 * rand.random((Nn, NL)) )
            self.W += rate * (-1+ 2 * rand.random((Nn, Nn, NL)) )
            self.Bi += rate * (-1+ 2 * rand.random((Nn)) )
            self.Wi += rate * (-1+ 2 * rand.random((Ni, Nn)) )
            self.Bo += rate * (-1+ 2 * rand.random((No)) )
            self.Wo += rate * (-1+ 2 * rand.random((No, Nn)) )

        elif self.mutType==2:

            #Запускаем лотерею
            Bspin = np.array(rand.random((self.Nn, self.NL)))
            Wspin = rand.random((self.Nn, self.Nn, self.NL))
            Bispin = rand.random((self.Nn))
            Wispin = rand.random((self.Ni, self.Nn))
            Bospin = rand.random((self.No))
            Wospin =  rand.random((self.No, self.Nn))
            # Определяем максимальные очки
            maxSpin=[Bspin.max, Wspin.max, Bispin.max, Wispin.max, Bospin.max, Wospin.max]
            matrices=[Bspin, Wspin, Bispin, Wispin, Bospin, Wospin]
            # общее количество элементов матрица
            numN=np.array( [np.prod(Bspin.shape), np.prod(Bspin.shape), np.prod(Bspin.shape), np.prod(Bspin.shape), np.prod(Bspin.shape), np.prod(Bspin.shape) ])
            #
            choice=rand
            if i==0:
                print(Bspin>maxSpin)
            if i==1:
                print(Wspin>maxSpin)
            if i==2:
                print(Bispin>maxSpin)
            if i==3:
                print(Wispin>maxSpin)
            if i==4:
                print(Bospin>maxSpin)
            if i==5:
                print(Wospin>maxSpin)

        else:
            return 1
        return 0

