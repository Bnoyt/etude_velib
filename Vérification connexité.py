def verif(d):
	for station in stations:
		if station != 0:
			station.proches(d,stations)
	etats = [True]*len(stations)
	i = 0
	while stations[i] == 0:
		i += 1
	P = stations[i].clique[:]
	while P != []:
		a = P.pop()
		etats[a] = False
		for p in stations[a].clique:
			if etats[p]:
				P.append(p)
	return not(toutfaux(etats))
	
def meilleureco(a,b):
	if b-a < 0.0005:
		return b
	d = (a+b)/2
	print(d)
	if verif(d):
		meilleureco(a,d)
	else:
		meilleureco(d,b)