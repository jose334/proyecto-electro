#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:21:27 2020

@author: joseramos
@author: raul aguilar
@author: julio lazo

PROYECTO TEORIA ELECTROMAGNETICA

PARA MEJORES RESULTADOS CORRER EN LA TERMINAL O IDLE PERO NO SPYDER


"""

import numpy as np

from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()

bw = cm.gray
warm = cm.coolwarm


"""La pregunta 3.2
"""

sin = np.sin
pi = np.pi

def h(y):
    return 2*y**3+5

cosh = np.cosh
sh = np.shape
cos = np.cos

dr = 0.1

R = 3
r = np.arange(0,R*2,dr)
t = np.linspace(0,pi,len(r))

dt = pi/len(r)

X,Y = np.meshgrid(r,t)

a1 = 3/10
a3 = -12/(35*R**2)
b1 = a1*R**3
b3 = a3*R**7
    
def p3(x):
    y = 1/2*(5*cos(x)**3-3*cos(x))
    return y

def V(r,t):
    v = np.zeros((len(r),len(t)))
    n = int(len(r))
    k = 0
    p = 0 
    Ri = len(r[:int(len(r)/2)])
    for rad in r[:Ri]:
        p = 0
        for th in t:
            v[k][p] = rad*a1*cos(th) + a3*rad**3*p3(th)
            p += 1
        k += 1
    for rad in r[Ri:]:
        p = 0
        for th in t:
            v[k][p] = b1*cos(th)/(rad**2)+b3/(rad**4)*p3(th)
            p += 1
        k+=1
    return v

#x,y = np.meshgrid(x,y)


def graficarV():
    v = V(r,t)
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X,Y,v, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_ylabel(r'$\theta$ (radianes)')
    ax.set_xlabel('R (m)')
    ax.set_title('Potencial (V)')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def menu():
    print('quiere graficar: \n'
          '1. el campo electrico\n'
          '2. el potencial\n'
          'ingrese el numero de la opcion que desea por favor')
    ans = input('')
    if '2' in ans:
        v = graficarV()
    elif '1' in ans:
        theta = np.linspace(0,1,3)
        v = V(r,t)
        ex, ey = np.gradient(v, dr, dt)
        fig, ax = plt.subplots()
        ax.set_title('Campo eléctrico (V/m)')
        ax.set_ylabel(r'$\theta$ (radianes)')
        ax.set_xlabel('R (m)')
        Q = ax.quiver(X,Y, ex, ey, linewidth = 0.01)
        plt.show()
        
menu()
