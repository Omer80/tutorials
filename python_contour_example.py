#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:10:13 2017

@author: ohm
"""

import matplotlib.pylab as plt
import numpy as np

plt.figure(1)
# Create a grid with linear x and y coordinates
X,Y = np.meshgrid(np.linspace(-10,10,20),np.linspace(-10,10,20))
# Calculate F
F = X**2+4.0*Y**2
# Plot contour
plt.contourf(X,Y,F)
# plot gradient vectors on the grid
dFdx = 2.0*X
dFdy = 8.0*Y
plt.quiver(X,Y,dFdx,dFdy)
plt.show()

