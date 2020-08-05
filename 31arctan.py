#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:21:27 2020

@author: joseramos
@author: raul aguilar
@author: julio lazo

PROYECTO TEORIA ELECTROMAGNETICA

PARA MEJORES RESULTADOS CORRER EN LA TERMINAL O IDLE PERO NO SPYDER

algoritmo para calcular la divergencia fue sacado de aca
https://www.manongdao.com/article-250819.html


"""

import numpy as np

from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt

from matplotlib import cm

fig = plt.figure()

bw = cm.gray
warm = cm.coolwarm


"""La pregunta 3.1 
"""

sin = np.sin
pi = np.pi
arctan = np.arctan
sinh = np.sinh
sh = np.shape

a = 3

b = a*1.5

def cn(n):
    f = []
    for i in y:
        s = (sin(n*pi/b*i))
        f.append(s*arctan(i/a))
    t = sinh(n*pi*a/b)
    I = np.trapz(f)
    I = I*2/b
    I = I/t
    return I

n = [3,6,11,21]

def V(x,y,n):
    v = np.zeros((len(x),len(x)))
    const = []
    for k in range(1,n):
        c = cn(k)
        const.append(c)
        r = 0
        s = 0
        for i in x:
            for j in y:
                v[s][r] += c*sin(k*pi*j/b)*sinh(k*pi*i/b)
                s += 1
            r += 1
            s = 0
    return v

#x,y = np.meshgrid(x,y)

def divergence(f):
    num_dims = len(f)
    return np.ufunc.reduce(np.add, [np.gradient(f[i], axis=i) for i in range(num_dims)])

def graficarV(k, b):
    v = V(x,y,n[k])
    if b:
        plt.figure(k)
        plt.title('Potencial, con n = '+str(n[k]-1))
        plt.xlabel('X')
        plt.ylabel('Y') 
        plt.pcolormesh(x,y,v,cmap = bw)
        plt.show()
        fig = plt.figure(10-k)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X,Y,v, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        ax.set_title('Potencial, con n='+str(n[k]-1))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
    return v

def menu():
    global x
    global y
    global z
    global dy
    global dx
    global X
    global Y
    print('quiere graficar: \n'
          '1. el campo electrico\n'
          '2. el potencial\n'
          '3. la carga superficial\n'
          'ingrese el numero de la opcion que desea por favor')
    ans = input('')
    if '2' in ans:
        dx = 0.01
        x = np.arange(0,a,dx)
        y = np.linspace(0,b,len(x))
        dy = b/len(x)
        X,Y =np.meshgrid(x,y)
        for k in range(len(n)):
            v = graficarV(k,True)
    elif '1' in ans:
        z = np.linspace(0,1,3)
        dx = 0.3
        x = np.arange(0,a,dx)
        y = np.linspace(0,b,len(x))
        dy = b/len(x)
        v = graficarV(3,False)
        v = np.expand_dims(v, axis = 2)
        v = np.repeat(v, 3, axis = 2)
        X,Y,Z =np.meshgrid(x,y,z)
        ex, ey, ez = np.gradient(v, dx, dy, 0.333)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_title('Campo eléctrico')
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        ax.quiver(X,Y,Z, ex, ey, ez, length=0.25, normalize = True)
        plt.show()
        dx = 0.3
        x = np.arange(0,a,dx)
        y = np.linspace(0,b,len(x))
        dy = b/len(x)
        v = graficarV(3,False)
        X,Y =np.meshgrid(x,y)
        ex, ey = np.gradient(v, dx, dy)
        fig, ax = plt.subplots()
        ax.set_title('Campo eléctrico')
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        Q = ax.quiver(X,Y, ex, ey, linewidth = 0.01)
        plt.show()
    else:
        dx = 0.01
        x = np.arange(0,a,dx)
        y = np.linspace(0,b,len(x))
        dy = b/len(x)
        z = np.arange(0,2,dx)
        X,Y =np.meshgrid(x,y)
        v = graficarV(3,False)
        ex, ey = np.gradient(v, dx, dy)
        densidad = divergence([ex,ey])
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X,Y,densidad, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        ax.set_title('Densidad de superficie')
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
        
menu()
