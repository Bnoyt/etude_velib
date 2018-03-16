"""
Ce script affiche pour le réseau choisie la route renvoyée par l'algorithme
"""


gna = 1 # Indice du réseau que l'on veut voir

from pylab import *

l = routes[gna]
X = [stations[k].posx for k in l]
Y = [stations[k].posy for k in l]

T = [0 for i in l]

scatter(X,Y, s=120, c=T, alpha=0.5)
plot(X,Y)
plt.show()