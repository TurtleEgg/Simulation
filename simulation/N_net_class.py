import numpy as np
import numpy.random as rand

class network(object):
    def __init__(self, NL=1, Nn=2, Ni=10, No=4, seed=8800):
        #NL количество слоев
        #Nn количество нейронов в слое
        #Ni количество входов
        #No количество выходов
        self.NL = NL
        self.Nn = Nn
        self.Ni = Ni
        self.No = No
        self.seed= seed
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


bot1=network()
bot1.Bo=[-1,-1,-1,-1]

In=(0,1,0,1,0,1,0,1,0,1) #входной сигнал
K=bot1.go(In)
print(K)
print('\n\n')
#print(bot1.W[:,:,0])
print(bot1.Bo)
print('\n\n')
print(bot1.B[:,0])
print('\n\n')
print(bot1.L[:,:])
print('\n\n')

