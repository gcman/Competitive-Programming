import sys
input = sys.stdin.readline
T = [0]*50000
H,D,E = map(int,input().split())
DEF = [tuple(map(int, input().split())) for i in range(D)]
if E > 0:
	for _ in range(E):
		start,dur,dmg = map(int, input().split())
		for i in range(start,start+dur):
			T[i] += dmg

for dmg in T:
	if DEF:
		H -= max(0,min([(dmg - x[1])*(100 - x[0])/100 for x in DEF]))
	else:
		H -= dmg
	if H <= 0:
		print("DO A BARREL ROLL!")
		break
if H > 0:
	print("{:.2f}".format(H))