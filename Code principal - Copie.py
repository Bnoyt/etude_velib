from math import cos,sin,acos,pi
from random import randint

class station(object):

	def __init__(self, capacite, posx, posy, id):
		"""
		Toutes les caractéristiques de notre station
		"""
		self.capacite = capacite
		self.posx = posx
		self.posy = posy
		self.id = id
		self.clique = []
		self.Ninst = 0
		self.Nentrant = 0
		self.Npartant = 0
		self.I = 0
		self.tprec = 0
		self.ni = capacite//2
		self.nf = 0
		self.delta = self.nf - self.ni

	def proches(self,d,stations):
		self.clique = []
		for station in stations:
			if station != 0 and station.id != self.id and distance(self.id,station.id) <= d:
				self.clique.append(station.id)

	def attribution(self,total):
		"""
		A partir de la valeur de self.I, calcule l'état final souhaité, ainsi que le delta correspondant
		"""
		self.I = int(self.I / (total) + 0.5)
		if self.I > self.capacite:
			self.nf = self.capacite
		else:
			if self.I < 0:
				self.nf = 0
			else:
				self.nf = self.I
		self.delta = self.nf - self.ni

	def calculI(self,t,tipe):
		"""
		Calcul de l'intégrale point par point (de manière exacte puisque les fonctions sont en escalier)
		"""
		
		self.I += (self.capacite/2 + self.Npartant - self.Nentrant)*(t - self.tprec)

		if tipe:
			self.Npartant += 1
		else:
			self.Nentrant += 1

		self.tprec = t

	def donnerpos(self):
		return(self.posx,self.posy)


def max_dic(liste):
	"""
	Calcul de l'id max d'une liste de dictionnaires (fichier json)
	"""
	m = liste[0]["id"]
	for dic in liste:
		a = dic["id"]
		if a > m:
			m = a
	return m+1


def extraction_stations(liste):
	"""
	Extraction des stations à partir de la liste de dictionnaires (fichier json)
	"""
	m = max_dic(liste)
	stations = [0 for i in range(m)]
	for dic in liste:
		stations[dic["id"]] = station(dic["totalDocks"],dic["latitude"],dic["longitude"],dic["id"])
	return stations




def heure(chaine):
	"""
	Conversion de l'heure donnée en hh::mm:ss en secondes
	"""
	p = chaine.split(" ")
	a = p[1].split(":")
	return int(a[0])*3600 + int(a[1])*60 + int(a[2])



def extraction_trajets(fichier,maxheure):
	"""
	Création des deux listes trajets1 et trajets2 contenant les arrivées ou le départ, ainsi que l'heure correspondante
	"""
	fichier = open(fichier,"r")
	trajets1 = []
	trajets2 = []
	while True:
		ligne = fichier.readline()
		if ligne == '':
			break
		else:
			ligne = ligne.split('","')
			if heure(ligne[1]) < maxheure: 
				trajets1.append(  [heure(ligne[1]),int(ligne[3])]  )
				trajets2.append(  [heure(ligne[2]),int(ligne[7])]  )

	return trajets1, trajets2

def fusion(a,b) :
	"""
	fusion de deux listes triées
	"""
	c = [] 
	n = len(a)
	m = len(b)
	i = 0
	j = 0
	while i < len(a) and j < len(b):

		if a[i][0] < b[j][0]:  
			c.append(a[i] + [True])
			i = i + 1
		else:  
			c.append(b[j] + [False])
			j = j + 1

	if i == len(a):
		for j in range(j,len(b)):  
			c.append(b[j] + [False])
	else :
		for j in range(i,len(a)):  
			c.append(a[i] + [True])
	
	return c


def calculnf(trajets,total):
	"""
	A partir de la liste des trajets, on calcule le nf pour tout le monde
	"""
	for trajet in trajets:
		if stations[trajet[1]] != 0:
			stations[trajet[1]].calculI(trajet[0],trajet[2])
	for station in stations:
		if station != 0: 
			station.attribution(total)
			#c'est le (maigre) prix a payer de notre implementation initiale en vecteur
	return None


def recupL(stations):
	"""
	Renvoie la liste formée de L_+ et L_- tamisées
	"""
	c = []
	for station in stations:
		if station !=0:
			c.append(station.id)
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
		if A!= []:
			D.append(A.pop()[1])
		if B != []:
			D.append(B.pop(0)[1])

	return D




def distance(ids1,ids2):
	R = 6370000
	"""
	Distance euclidienne entre deux stations
	"""
	if ids1 == ids2:
		return 0
	x1,y1 = stations[ids1].donnerpos()
	x2,y2 = stations[ids2].donnerpos()
	return R*acos(cos(x1*pi/180)*cos(x2*pi/180)*cos((y1-y2)*pi/180)+sin(x1*pi/180)*sin(x2*pi/180))

def distance2(x1,y1,x2,y2):
	"""
	Distance euclidienne entre deux points dont on ne connait que les coordonnées sphériques de la terre
	"""
	R = 6370000
	return R*acos(cos(x1*pi/180)*cos(x2*pi/180)*cos((y1-y2)*pi/180)+sin(x1*pi/180)*sin(x2*pi/180))

def coord(v):
	"""
	Renvoie les coordonnées d'un chemin
	"""
	C = []
	for i in range(len(v)-1):
		C.append(distance(v[i],v[i+1]))
	return C

def norme(v):
	"""
	Renvoie la norme d'un vecteur
	"""
	A = 0
	for lop in coord(v):
		A += (abs(lop))
	return A

def echanger(L,i,j):
	"""
	Echange deux éléments d'une liste
	"""
	a = L[i]
	L[i] = L[j]
	L[j] = a
	return L

def permut2(chemin):
	"""
	Renvoie la liste de toutes les permutations de deux éléments d'un chemin
	"""
	n = len(chemin)
	L = [chemin]
	for i in range(n):
		for k in range(i+1,n):
			L.append(echanger(chemin[:],i,k))
	return L



def qualite(v,capacite):
	"""
	Qualité d'un chemin donné en essayant de satisfaire au maximum à chaque instant le delta des stations
	"""
	A = 0
	Q = 0
	P = 0
	for sid in v:
		delta = stations[sid].delta
		if delta > 0:
			if A >= delta:
				A -= delta
			else:
				Q += delta - A
				A = 0
			P += delta
		if delta < 0:
			if A <= (capacite + delta): #delta est negatif
				A -= delta
			else:
				Q += A - capacite - delta 
				A = capacite
			P -= delta
	if P == 0: #Pour éviter de diviser par 0..
		return 1
	else:
		return 1 - Q/P

def g(v,r,x):
	"""
	La fonction g, qui à un chemin essaye d'en renvoyer un meilleur
	"""
	A = permut2(v)
	minimum = norme(v)
	for perm in A:
		a = norme(perm)
		if a < minimum and qualite(perm,x) >= r:
			minimum = a
			v = perm

	return v
	



	
