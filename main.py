import numpy as np
import matplotlib.pyplot as plt
from method import LSE, Newton
from utils import *


x_data = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y_label = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

lambd = 0
n = 2
N = int(len(x_data))
X = X_polybases(x_data, N, n=n)
y = [y_label[i] for i in range(N)]

if(True):
    model = LSE()
    model.fit(X,y, lmbd=lambd)
    model.predict(X)
    model.visualize(X,y)

    model = Newton()
    model.fit(X,y)
    model.predict(X)
    model.visualize(X,y)