import matplotlib.pyplot as plt

A = []
for s in stations:
	if s != 0:
			A.append([s.capacite,s.nf])
A.sort()
		
plt.plot(A)