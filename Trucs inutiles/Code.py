# Données à rentrer pour la simulation
fichier = "listestation.json"

d = 300

c

# Classes

def extraction_stations(Dic):
	stations = []
	for element in Dic
		temp = station(Dic["totalDocks"],Dic["latitude"],Dic["longitude"],Dic["id"])
		stations.append(temp)
	return stations


def fusion(l1,l2):

"""
La fusion de deux listes triees renvoie une liste triee (dans l'odre croissant)
"""

	n1,n2 = len(l1),len(l2)
	i1 = 0
	i2 = 0
	liste = [0 for i in range(n1+n2)]
	while i1 < n1 or i2 < n2:
		if i1 >= n1:
			liste[i1+i2] = l2[i2]
			i2 += 1
		else:
			if i2 >= n2:
				liste[i1+i2] = l1[i1]
				i1 += 1
			else:
				if l1[i1].id > l2[i2].id:
					liste[i1+i2] = l2[i2]
					i2 += 1
				else:
					liste[i1+i2] = l1[i1]
					i1 += 1
	return liste

def tri_fusion(liste):

"""
Sauf erreur, le tri fusion bete et mechant
"""

	if liste == []:
		return []

	else:

		if len(liste) == 1:
			return liste
		else:
			n = len(liste)
			a = n//2
			g = [liste[k] for k in range(a)]
			d = [liste[k] for k in range(a,n)]

			return fusion(tri_fusion(g),tri_fusion(d))







class AbrVide(object):
	def __init__(self):
		self.etiquette = None

	def creer_arbre_equilibre(self,liste):
		"""
		la liste donnee en argument est supposee triee par ordre croissant d'id
		"""
		if liste = []:
			return AbrVide()
		else:
			n = len(liste)
			a = n//2
			g = [liste[k] for k in range(a)]
			d = [liste[k] for k in range(a+1,n)]
			fg = AbrVide().creer_arbre_equilibre(g)
			fd = AbrVide().creer_arbre_equilibre(d)
			return Abr(liste[a],fg,fd)

	def map_abr_all(self,fonction):
		return None


class Abr(object):
	def __init__(self,etiquette,fg,fd):
		self.etiquette = etiquette
		self.fg = fg
		self.fd = fd

	def ajout(self,elem):
		"""
		On suppose qu'on ajoute uniquement des elements qui ne sont pas deja dans l'arbre
		"""
		if elem.id > self.etiquette.id:
			if self.fd.etiquette = None:
				self.fd = Abr(elem,AbrVide(),AbrVide())
			else:
				self.fd.ajout(elem)

		else:
			if self.fg.etiquette = None:
				self.fg = Abr(elem,AbrVide(),AbrVide())
			else:
				self.fg.ajout(elem)


	def map_abr_one(self,id,fonction):
		"""
		On suppose qu'on donne en entree un id qui est deja dans l'arbre
		"""
		if self.etiquette.id = id:
			etiquette.fonction()
		else:
			if id > self.etiquette.id:
				self.fd.map_abr(id,fonction):
			else:
				self.fg.map_abr(id,fonction)

	def map_abr_all(self,fonction):
		self.etiquette.fonction()
		self.fg.map_abr_all(fonction)
		self.fd.map_abr_all(fonction)





def extraction_trajets(fichier,heure):
	fichier = open(fichier,"r")
	while True:
		ligne = fichier.readline()
		if ligne = '':
			break
		else:





class station(object):

	def __init__(self, capacite, posx, posy, id):
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

	def changerstatut(self, mode, nbre):
		self.ninst = self.ninst + nbre*mode

	def proches(self,stations,distances,d):
		for station in station:
			if distances[self.id][station.id] <= d:
				self.clique.append(station.id)

	def attribution(self,total):

		self.I = int(self.I / (total**3) + 0.5)
		if self. I > self.C:
			self.nf = self.C
		else:
			if self.I < 0:
				self.nf = 0
			else:
				self.nf = self.I



	def calculI(self,t,tipe):
		if tipe:
			self.Npartant += 1
		else:
			self.Nentrant += 1
		self.I += (self.C/2 + Npartant - Nentrant)*(t**3 - tprec**3)
		tprec = t

	def donnerpos(self):
		return(self.posx,self.posy)



def calculnf(trajets,total):
	for trajet in trajets:
		stations.map_abr_one(trajet[0],calculI(trajet[1],trajet[2]))
	stations.map_abr_all(attribution(total))









class camion(object):
	def __init__(self, capacite, position, remplissage):
		self.capacite = capacite
		self.remplissage = remplissage
		self.position = position
		self.trajet = [position]

	def changerstatut(self, mode, nbre, station):
		self.remplissage += mode*nbre
		station.changerstatut(self, -mode, nbre)

	def voyager(self,destination):
		self.position = destination
		self.trajet.append(destination)

		return()


class supercalculator(object):
	def __init__(self, fichier, d):

		self.dcarac = d 
		self.distances = [[self.calculdistance(k,p) for k in stations] for p in stations]

	def calculclique(self):
		for station in self.stations:
			station.clique(self.stations,self.distances, self.dcarac)

	def calculdistance(self,k,p):
		return formuleatrouver(k,p)

	def recherche_Dic(self):
		#importation du fichier json a effectuer

	def extraction_stations(self, Dic):
		stations = []
		for element in Dic
			temp = station(Dic["totalDocks"],Dic["latitude"],Dic["longitude"],Dic["id"])
			stations.append(temp)
		return stations



def distance(ids1,ids2):
	"""
	Distance euclidienne entre deux stations
	"""
	x1,y1 = stations.map_abr_one(ids1,donnerpos)
	x2,y2 = stations.map_abr_one(ids2,donnerpos)
	return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def coord(v):
	"""
	Renvoie les coordonnées d'un chemin
	"""
	C = []
	for i in range(len(v)-1)
		C.append(distance(v[i],v[i+1]))
	return C

def norme(v):
	"""
	Renvoie la norme d'un vecteur de else
	"""
	A = 0
	for coord in coord(v):
		A.append(abs(coord))
	return A

def permutations(k):
	"""
	Renvoie la liste des permutations de [1,k-1]
	"""
	if k == 1:
		return [[0]]
	else:
		a = permutations(k-1)
		A = []
		for perm in a:
			for i in range(k):
				A.append(perm[:i]+ [k-1] + perm[i:])
		return A

def permutalpha(alpha, L):
	"""
	Renvoie une liste de tuple contenant la liste de toutes les permutation
	des alpha elements, et la liste restante.
	Tous les elemnts de la liste sont supposes distincts
	alpha <= len(L) evidemment
	"""
	if alpha == 1:
		return [[[L[i]], L[:(i)] + L[(i+1):]] for i in range(len(L))]
	else:
		a = permutalpha(alpha - 1, L)
		A = []
		for perm in a:
			for i in range(len(perm[1])):
				print (perm[1][i])
				A.append([perm[0][::].append(perm[1][i]),perm[1][:i] + perm[1][(i+1):]])
		return A


def permut_to_path(permutations,L):
	A = []
	for permut in permutations:
		a = tri_fusion(permut)
		k = 0
		P = []
		for i in range(len(L)):
			if a[k] == i:
				P.append(L[permut[k]])
				if k < len(a) - 1:
					k += 1
			else:
				P.append(L[i])
		A.append(P)
	return A

def g_alpha(alpha,v,r):
	A = permut_to_path(permutalpha(alpha,v), v)
	minimum = norme(coord(v))
	for perm in A:
		a = norme(coord(perm))
		if a < minimum and qualite(perm) <= r:
			minimum = a
			v = perm

	return v












