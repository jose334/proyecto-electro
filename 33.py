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


"""La pregunta 3.3
"""

pi = np.pi
dr = 0.1
cos = np.cos
sh = np.shape
r = np.arange(1,1000,dr)

e0 = 10

phi = np.linspace(0,pi,len(r))
    
R, P = np.meshgrid(r,phi)

v = -e0*R*(1-1/(R**2))*cos(P)

ax = fig.gca(projection='3d')
surf = ax.plot_surface(R,P, v, cmap=cm.coolwarm,
                       linewidth=0)
ax.set_ylabel(r'$\phi$ (radianes)')
ax.set_xlabel('R (m)')
ax.set_title('Potencial (V)')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()


