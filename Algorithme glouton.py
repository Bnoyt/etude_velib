import itertools as it
from math import sqrt



s0 = station(50,0,0,0)
s1 = station(50,0,1,1)
s2 = station(50,1,0,2)
s3 = station(50,0,-1,3)
s4 = station(50,-1,0,4)
s5 = station(50,1,-1,5)
s6 = station(50,1,1,6)

s0.delta = 21
s1.delta = 15
s2.delta = -9
s3.delta = 5
s4.delta = 13
s5.delta = -19
s6.delta = -4

stations = [s0,s1,s2,s3,s4,s5,s6]

def respb():
	a = [0,1,2,3,4,5,6]
	P = list(it.permutations(a,len(a)))
	A = []
	K = []
	for i in P:
		if qualite(list(i),30) >= 0.7:
			A.append(list(i))
		K.append(list(i))
	A.sort(key = norme)
	return K,A

def distance(ids1,ids2):
	if ids1 == ids2:
		return 0
	x1,y1 = stations[ids1].donnerpos()
	x2,y2 = stations[ids2].donnerpos()
	return sqrt(   (x1-x2)**2 + (y1-y2)**2        )
	
def distance2(x1,y1,x2,y2):

	return sqrt(   (x1-x2)**2 + (y1-y2)**2        )

res = reseau(2)
res.stations = [0,1,2,3,4,5,6]
a = resoudrepb(res,30)
#K,A = respb()
#a = A[0]
routes=[a]