import sys
import heapq
#sys.stdin = open("data.txt")
input = sys.stdin.readline

N,X = map(int,input().split())
T = {}
for _ in range(N):
	s,j = map(int,input().split())
	if s not in T:
		T[s] = [0,0]
	if j not in T:
		T[j] = [0,0]
	T[s][0] += 1
	T[j][1] += 1

sandwiches = []
heapq.heapify(sandwiches)
cnt = 0
prev_time = 0
for time in sorted(T.keys()):
	t = time - prev_time
	to_hand_in = T[time][1] if time in T else 0
	for i,x in enumerate(sandwiches):
		cnt += max(0,(t + X - x) // X)
		if (t-x) % X == 0 and to_hand_in > 0: # Don't zap what you could hand in
			cnt -= 1
			to_hand_in -= 1
			new = 0
		else:
			new = X - (t - x) % X
		sandwiches[i] = new
		if new > x: # Restore heap
			heapq._siftup(sandwiches, i)
		elif new < x:
			heapq._siftdown(sandwiches, 0, i)
	if time in T:
		for _ in range(T[time][0]): # Cook
			heapq.heappush(sandwiches,X)
		for _ in range(T[time][1]):
			heapq.heappop(sandwiches)
	prev_time = time
print(cnt)