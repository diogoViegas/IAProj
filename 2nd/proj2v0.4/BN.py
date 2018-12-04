# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""
import numpy as np

class Node():
    def __init__(self, prob, parents = []):
        self.prob=prob
        self.parents=parents
        self.numberparent = len(self.parents)
    
    def computeProb(self, evid):
        res=[]

        if (self.numberparent==0):
            res.append(1-self.prob[0])
            res.append(self.prob[0])
            return res
        aux = ''
        aux1 = np.concatenate((self.prob[0], self.prob[1]), axis=None)  # arrays de arrays -> flatarray
        aux2 = list(evid)  # tuplo para lista para poder aceder ao index
        
        for i in range(0, len(self.parents)) :
            aux+=str(aux2[self.parents[i]])    #string vai ter o valor em binario dos pais
        aux3=int(aux, 2)                       #binario para decimal
        return [1-aux1[aux3], aux1[aux3]]      #posicao decimal no flat array

class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):
        defaultlist = list(evid)
        aux= defaultlist
        auxstr = ''
        index=[]
        counter, res1, res2=0, 0, 0
        indexcalc = 0
        for i in range(0, len(defaultlist)):
            if aux[i]==[]:
                auxstr +=str(0)
                index.append(i)
                counter +=1
            if aux[i]==-1:
                aux[i]=1
                indexcalc=i

        for j in range(0, counter):
            for l in range(0, len(index)):
                aux[l]=auxstr[l]
            res1+=self.computeJointProb(tuple(aux))
            auxstr = bin(int(auxstr, 2) + 1)[2:].zfill(counter)

        aux=defaultlist
        aux[indexcalc]=0
        for j in range(0, counter):
            for l in range(0, len(index)):
                aux[l]=auxstr[l]
            res2+=self.computeJointProb(tuple(aux))
            auxstr = bin(int(auxstr, 2) - 1)[2:].zfill(counter)


        pass
        
    def computeJointProb(self, evid):
        aux = list(evid)
        res=1
        for i in range(0,len(aux)):
            if aux[i]==0:
                res=res*self.prob[i].computeProb(evid)[0]
            else:
                res=res*self.prob[i].computeProb(evid)[1]

        return res

gra = [[],[],[0,1],[2],[2]]
ev = (1, 0, 1, 1, 1)
#p3 = Node( np.array([[.001,.29],[.94,.95]]), gra[2] )   # alarm
#print(p3.computeProb(ev))
#p1 = Node(np.array([.001]), gra[0])  # burglary
#print("p1 false %.4e p1 true %.4e" % (p1.computeProb(ev)[0], p1.computeProb(ev)[1]))

#p5 = Node( np.array([.01,.7]), gra[4] )
#print(p5.computeProb(ev))
p1 = Node( np.array([.001]), gra[0] )
print(p1.computeProb(ev))
p2 = Node( np.array([.002]), gra[1] )
print(p2.computeProb(ev))
p3 = Node( np.array([[.001,.29],[.94,.95]]), gra[2] )
print(p3.computeProb(ev))
p4 = Node( np.array([.05,.9]), gra[3] )
print(p4.computeProb(ev))
p5 = Node( np.array([.01,.7]), gra[4] )
print(p5.computeProb(ev))
prob = [p1,p2,p3,p4,p5]
bn = BN(gra,prob)
print(bn.computeJointProb((0,0,1,1,1)))