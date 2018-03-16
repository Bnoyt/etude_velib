"""
Script pour résoudre le problème statique sur le réseau choisi
"""
from time import clock 
d = 900	# Distance de connexité choisie
alpha = 3 	# Paramètre qui détermine quand on arrête la dichotomie de la recherche des centres
capacite = 20	# Capacité du camion choisie
A = []
for p in range(5,20):
	centres = recherchecentres(p,alpha)
	t1 = clock()
	reseaux = parcours(centres)
	A.append(clock() - t1)

print(A)
