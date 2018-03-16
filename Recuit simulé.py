from random import randint,random
from math import exp

def recuit(miou,N,Tmin,T,alpha,r):
	"""
	Méthode du recuit simulé appliquée à un chemin u0 donné en entrée
	"""
	n = len(miou)
	u = miou[:]
	while T > Tmin:
		i = 0
		while i < N:
			k,p=randint(0,n-1),randint(0,n-1)
			v = u[:]
			v = echanger(v,k,p)
			if norme(v) <= norme(u) and qualite(v,20) >= r:
				u = v[:]
				i = N
			elif qualite(v,20) >= r:
				p = random()
				if p <= exp(-(norme(v)-norme(u))/T):
					u = v[:]
					i = N
				else:
					i += 1
			else:
				i += 1
		T = T*alpha
	return u
	
def resoudrepb(reseau,s):
	"""
	Pour résoudre le problème, on applique g plein de fois pour garder le meilleur chemin
	"""
	c = adapter(reseau.stations[:])
	
	q = min(qualite(c,s),0.8)
	for i in range(100):
		a = c[:]
		c = g(c,q,s)
		if c == a:
			break
		
	return recuit(c,1000,0.005,10000,0.85,min([qualite(c,s),0.8]))
	
def recuitinv(u0,N,Tmin,T,alpha):
	n = len(u0)
	u = u0[:]
	while T > Tmin:
		i = 0
		while i < N:
			k,p=randint(0,n-1),randint(0,n-1)
			v = u[:]
			v = echanger(v,k,p)
			if qualite(v,20) >= qualite(u,20):
				u = v[:]
				i = N
			else:
				p = random()
				if p <= exp((qualite(v,20)-qualite(u,20))/T):
					u = v[:]
					i = N
				else:
					i += 1
		T = T*alpha
	return u
	