"""
Script pour résoudre le problème statique sur le réseau choisi
"""
from time import clock
p = 10 	# Nombre de réseaux voulu (c'est à dire le nombre de camions) 
d = 900	# Distance de connexité choisie
alpha = 3 	# Paramètre qui détermine quand on arrête la dichotomie de la recherche des centres
capacite = 20	# Capacité du camion choisie
t1 = clock()
routes,reseaux = toutleprobleme(p,d,alpha,capacite)
moimoi = clock() - t1
# Toute la suite n'est qu'une sortie graphique (dans la console) de l'algorithme
a = 0
b = 0
i = 0
c = 0
d = 0
print("\n")
print("\n")
print("\n")
print("\n")
print( " 329 STATIONS ET " + str(p) + " CAMIONS")
print("\n")
print("\n")
print("\n")
print("\n")
for route in routes:
	a += norme(route)/len(route)
	c += norme(route)
	x,y = qualite_youp(route,20)
	b += x
	d += y
	i += 1
	print( "RESEAU N°" + str(i) + "	 : " + str(len(route)) + " stations \n")
	print( "Distance totale à parcourir : " + str(norme(route)/1000) + " km \n")
	print( "Distance moyenne entre chaque station : " + str(norme(route)/1000/len(route)) + " km \n")
	print( "Qualité du chemin suivi : " + str(qualite(route,20)) + "\n")
	print("\n")
	print("\n")

	
print("\n")
print("\n")
print("\n")	
print("\n")
print("Distance totale à parcourir : " + str(c/1000) + " km \n")
print("Distance totale cumulée pondérée : " + str(a/len(routes)/1000) + " km")
print("Qualité totale pondérée : " + str(1-b/d))
print("\n")	
print("\n")
print("Temps mis : " +str(moimoi) + " s")



