from responseSpectMain import SaSvSd
import numpy as np
dt=0.02
acc=np.loadtxt("acc.txt")
beta=0.05
T=[1,2,3,4,5]
sa,sv,sd=SaSvSd(acc,dt,T,beta)
