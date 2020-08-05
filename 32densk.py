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

pi = np.pi
dr = 0.5
cos = np.cos
sh = np.shape

R = 3
b = 3*R

r = np.arange(0,b,dr)
dt = pi/len(r)
Ri = len(r[:int(len(r)/3)])

r1 = np.arange(b,b*1.5,dr)
r = np.concatenate((r,r1))

t = np.linspace(0,pi,len(r))
X,Y = np.meshgrid(r,t)

a0 = -b/3
a1 = R*b/(3)
a2 = 4/(b*15)
a3 = -a2*R**5
    
def p3(x):
    y = 1/2*(3*cos(x)**2-cos(x))
    return y

def V(r,t,Ri):
    v = np.zeros((len(r),len(t)))
    k = Ri
    p = 0 
    for rad in r[Ri:Ri*3]:
        p = 0
        for th in t:
            v[p][k] = a0 + a1/(3*rad) + (a2*rad**2+a3/rad**3)*p3(th)
            p += 1
        k+=1
    for rad in r[Ri*3:]:
        p =0 
        for th in t:
            v[p][k] = a0 + a1/(3*rad) + (a2*rad**2+a3/rad**3)*p3(th)
            p += 1
        k+=1
    return v

#x,y = np.meshgrid(x,y)


def graficarV(Ri):
    v = V(r,t, Ri)
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
        v = graficarV(Ri)
    elif '1' in ans:
        theta = np.linspace(0,1,3)
        v = V(r,t, Ri)
        ex, ey = np.gradient(v, dr, dt)
        fig, ax = plt.subplots()
        ax.set_title('Campo eléctrico (V/m)')
        ax.set_ylabel(r'$\theta$ (radianes)')
        ax.set_xlabel('R (m)')
        Q = ax.quiver(X,Y, ex, ey, linewidth = 0.15)
        plt.show()
        
menu()
