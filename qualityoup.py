def qualite_youp(v,capacite):
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
		return Q,P