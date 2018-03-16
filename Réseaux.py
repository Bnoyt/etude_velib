"""
Ce script affiche la représentation des réseaux par des points de différentes couleurs
"""


from pylab import *
from math import sqrt
a = reseaux
X = [0 for i in a]
Y = [0 for i in a]
T = [0 for i in a]
for i in range(len(a)):	
	X[i] = [stations[k].posx for k in a[i].stations]
	Y[i] = [stations[k].posy for k in a[i].stations]
	T[i] = [i**(0.9) for k in Y[i]]

def concat(L):
	D = []
	for i in L:
		D += i
	return D

scatter(concat(X),concat(Y), s=200, c=concat(T), alpha=1)
plt.show()