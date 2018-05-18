import sys
input = sys.stdin.readline

N,A,B = map(int,input().split())

POS = {}

for _ in range(N):
	x,vx,vy = map(int,input().split())
	v = (vx,vy)
	score = vy - A*vx
	if score not in POS:
		POS[score] = {}
	if v not in POS[score]:
		POS[score][v] = 0
	POS[score][v] += 1

COL = 0
for x in POS:
	size = sum([POS[x][v] for v in POS[x]])
	COL += size*(size-1)//2 - sum([max(0,POS[x][v]*(POS[x][v]-1)//2) for v in POS[x]])
COL *= 2
print(COL)