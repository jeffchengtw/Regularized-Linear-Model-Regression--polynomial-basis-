from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt
from model import LSE, Newton



def X_polybases(data, N, n=1):
    X = [np.ones(N)]
    for j in range(n-1):
        X.append([data[i]**(j+1) for i in range(N)])
    return np.vstack(X[::-1]).T


x_data = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y_label = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

lambd = 0
n = 2
N = int(len(x_data))
X = X_polybases(x_data, N, n=n)
y = [y_label[i] for i in range(N)]

if(True):
    model = LSE()
    model.fit(X,y, lambd=lambd)
    model.predict(X)
    model.show_report(X,y)
    model.plot_res(X,y)

    model = Newton()
    model.fit(X,y)
    model.show_report()
    model.plot_res(X,y)