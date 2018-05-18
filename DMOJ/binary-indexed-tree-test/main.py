import sys
sys.stdin = open("dt.txt")
input = sys.stdin.readline

N,M = map(int,input().split())
BIT = [0] * 100001
CNT = [0] * 100001

def update(tree,i,v): #tree, idx to update, val of update
	while i <= 100001:
		tree[i] += v
		i += -i & i

def getsum(tree,v):
	ans = 0
	while v > 0:
		ans += tree[v]
		v -= -v & v
	return ans
  
for i,x in enumerate(map(int,input().split()),start=1):
	update(BIT,i,x)
	update(CNT,x,1)
  
for _ in range(M):
	q = input().split()
	if q[0] == "C": # Update
		ind = int(q[1])
		new = int(q[2])
		old = getsum(BIT, ind) - getsum(BIT, ind - 1) # Get val here
		update(CNT, new, 1) # Make sure count agrees
		update(CNT, old, -1) 
		update(BIT, ind, new - old)
	elif q[0] == "S": # Sum from l to r: S(r) - S(l)
		left = int(q[1])
		right = int(q[2])
		print(getsum(BIT, right) - getsum(BIT, left - 1))
	else:  # Only other option left is num elem <= v
		ind = int(q[1])
		print(getsum(CNT, ind))