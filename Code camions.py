def comp(m):
	"""
	Utile seulement quand on a besoin de trier une liste
	"""
	return m[0]

def carre(idstation,maille,origine):
	"""
	on retourne les coordonnées du carré
	qui contient notre station 
	"""
	a = int(distance2(origine[0],origine[1],stations[idstation].posx,origine[1]) / maille)
	b = int(distance2(origine[0],origine[1],origine[0],stations[idstation].posy) / maille)
	
	return a,b


def quadrillage(maille, h, l,origine):
	"""
	Renvoie tous les carrés pour un quadrillage donné
	"""
	a = int(h/maille) + 1 #le nombre de hauteurs
	b = int(l/maille) + 1 #le nombre de longueurs
	#ok +1 mais au pire on aura des carre vides
	#c'est pas grave
	n = a*b
	L = [[] for i in range(n)]
	"""
	On va numeroter les carres 
	horizontalement de gauche a droite
	"""
	P = 0
	for station in stations:
		if station != 0:
			x,y = carre(station.id,maille,origine)
			L[x*a + y] .append(station.id)
			P += 1 #le nombre de vraies stations
	u = P // (2*n)
	A = 0
	H = []
	for i in range(len(L)):
		if len(L[i]) > u:
			A += 1
			H.append([len(L[i]),L[i]])
	return A,H

def bornes():
	"""
	Retourne les bornes du reseau entier
	"""
	xmin =  360
	ymin =  360
	xmax = -360
	ymax = -360
	for station in stations:
		if station != 0:
			if station.posx < xmin:
				xmin = station.posx
			if station.posx > xmax:
				xmax = station.posx
			if station.posy < ymin:
				ymin = station.posy
			if station.posy > ymax:
				ymax = station.posy
	origine = [xmin,ymin]
	h = distance2(xmin,ymin,xmin,ymax)
	l = distance2(xmin,ymin,xmax,ymin)
	#On neglige ici localement la courbure de la terre
	return origine,h,l

def meilleur(liste):
	"""
	On prend le meilleur élément de la liste : celui qui a le plus petit delta négatif (c'est toujours mieux pour commencer)
	"""
	k = liste[0]
	m = stations[k].delta
	for i in liste:
		if stations[i].delta < m:
			k = i
			m = stations[i].delta
	return k


def recherchecentres(p,d):
	"""
	La recherche dichotomique des centres
	"""
	origine,h,l = bornes()
	mmax = max(h,l)
	mmin = mmax / p
	
	while mmax - mmin > d:
		maille = (mmax + mmin) / 2
		c,S = quadrillage(maille,h,l,origine)
		if c > p:
			mmin = maille
		else:
			mmax = maille

	if c < p:
		c,S = quadrillage(mmin,h,l,origine)
		#Si la maille à la fin de la boucle ne convient pas
		#On garde le min (oui, tout est inversé)
	
	S.sort(key = comp)
	H = []
	p = min(len(S),p)
	"""
	On prend les p plus gros sous-résaux
	"""
	for i in range(p):
		H.append(S[i][1])

	return [meilleur(liste) for liste in H]
	
def ajoutsmart(etats,L,P):
	"""
	Ajoute les stations de la liste P à la liste L, si et seulement si elles n'ont pas encore été visitées
	On a besoin de cette fonction dans prochain
	"""
	for elem in P:
		if etats[elem]:
			L.append(elem)

	return L




class reseau(object):

	def __init__(self,centre):

		"""
		Toutes les caractéristiques d'un réseau
		"""

		self.L = [[centre]] #la liste des différents niveaux de stations adjacentes
		self.stations = [centre] #la liste des stations du réseau
		self.delta = stations[centre].delta #le delta du réseau



	
	def minidelta(self,etats, liste):
		"""
		On cherche dans la liste donnée en arguments la station la plus adaptée à continuer le réseau qui n'a pas encore été ajoutée à un autre réseau
		le triplet renvoyé est composé d'un triplet donnant (dans l'ordre) :
			-	la station qu'il faut
			-	la liste privée de cette station
			-	un booléen qui vaut True si on n'a trouvé personne, False sinon
		"""
		if self.delta < 0:
			#le meilleur des +delta
			a = True
			for i in liste:
				if stations[i].delta > 0 and etats[i]:
					a = False
					b = i
		else:
			#le meilleur des -delta
			a = True
			for i in liste:
				if stations[i].delta < 0 and etats[i]:
					a = False
					b = i

		if a:
			#le moins pire des delta
			d = abs(liste[0])
			for i in liste:
				if abs(stations[i].delta) <= d and etats[i]:
					d = abs(stations[i].delta)
					a = False
					b = i

		if a:
			return 0,[], True
		liste.remove(b)
		if liste == None:
			liste = []
		return b,liste,False



	def prochain(self,etats):
		"""
		Met à jour le réseau en fonction du vecteur etats

		A ameliorer en mettant tout le début dans une seule boucle while 

		"""

		k = True

		while k:
			#Si personne ne convenait dans la liste précédente, il faut chercher dans les suivantes, sachant qu'au départ personne ne convient, il faut donc chercher
			A = []
			n = len(self.L)
			i = 0
			while A == [] and i < n:
			#On recherche le premier niveau non vide
				A = self.L[i][:]
				i += 1
			i -= 1
			
			if A == []:			
				return etats,"fini"
			
			station,self.L[i],k = self.minidelta(etats,A) 
			
		#On change l'état de la station trouvée
		etats[station] = False
		#On rajoute sa clique au bon niveau
		#Mais surtout, on n'ajoute les stations que si elles ne sont pas déjà affectées à un réseau
		if i < n-1:
			self.L[i+1] = ajoutsmart(etats,self.L[i+1],stations[station].clique)
		else:
			self.L.append(ajoutsmart(etats,[],stations[station].clique))
		self.stations.append(station)
		self.delta += stations[station].delta
		return etats,"rien"


def toutfaux(L):
	"""
	Sert à dire si le vecteur etats vaut False pour tout le monde
	"""
	A = 0
	for i in L:
		if not(i):
			A += 1
	return A < 329 #329 est le nombre de stations (connu)

def parcours(centres):
	"""
	Crée les réseaux à partir des centres
	"""
	
	etats = [True for station in stations]
	
	reseaux = [reseau(centre) for centre in centres]
	
	finis = [True for res in reseaux]
	
	while toutfaux(etats):
		for i in range(len(reseaux)):
			if finis[i]:
				etats,f = reseaux[i].prochain(etats)
				if f == "fini":
					finis[i] = False
			
			
	return reseaux

def adapter(c):
	"""
	A partir d'un chemin c, crée un chemin alternant station avec faible delta, et station avec fort delta, pour optimiser la qualité de la redistribution du chemin à partir duquel on commence la recherche de point fixe
	"""
	for i in range (len(c)):
		c[i] = [stations[c[i]].delta,c[i]]
	A = []
	B = []
	for i in c:
		if i[0] > 0:
			A.append(i)
		else:
			B.append(i)
	A.sort()
	B.sort()
	D = []
	while A != [] or B != []:
		if B != []:
			D.append(B.pop(0)[1])
		if A!= []:
			D.append(A.pop()[1])

	return D[:]

def resoudrepb(reseau,s):
	"""
	Pour résoudre le problème, on applique g plein de fois pour garder le meilleur chemin
	"""
	c = adapter(reseau.stations[:])
	q = min(qualite(c,s),0.8)
	for i in range(100):
		a = c[:]
		q = min(qualite(c,s),0.8)
		c = g(c,q,s)
		if c == a:
			break
	return c


def touteslesroutes(reseaux,s):
	"""
	A partir de la liste des réseaux, on renvoie la liste des routes à effectuer
	"""
	A = []
	for reseau in reseaux:
		A.append(resoudrepb(reseau,s))
	return A




def toutleprobleme(p,d,alpha,s):
	"""
	Cette fontion résout tout le problème avec p le nombre de camions, d la distances pour calculer proches, alpha et le minimum de quadrillage
	"""
	for station in stations:
		if station != 0:
			station.proches(d,stations)
	centres = recherchecentres(p,alpha)
	reseaux = parcours(centres)
	routes = touteslesroutes(reseaux,s)
	return routes,reseaux




