class Fourmi(object):

	def __init__(self, listestations, alpha, beta, capacite):
		"""
		On initialise la fourmi avec la liste des stations existantes (le vecteur stations sera toujours une variable globale)
		alpha et beta sont les paramètres choisis pour la simulatio
		"""
		self.stations = listestations
		self.alpha = alpha
		self.beta = beta
		self.reste = listestations[:]
		self.capacite capacite