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
		self.ni = capacite//2
		self.nf = 0
		self.delta = self.nf - self.ni
		
	def changerstatut(self, mode, nbre):
		self.ninst = self.ninst + nbre*mode

	def proches(self,d,stations):
		for station in stations:
			if station != 0 and station.id != self.id and distance(self.id,station.id) <= d:
				self.clique.append(station.id)

	def attribution(self,total):
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
		if tipe:
			self.Npartant += 1
		else:
			self.Nentrant += 1
		self.I += (self.capacite/2 + self.Npartant - self.Nentrant)*(t - self.tprec)
		self.tprec = t

	def donnerpos(self):
		return(self.posx,self.posy)