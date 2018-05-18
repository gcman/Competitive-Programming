import sys
input = sys.stdin.readline

S = list(map(int,input().split()))
SCORES = []

for i in range(14):
	TMP = [x for x in S]
	if TMP[i] != 0:
		stones = TMP[i]
		TMP[i] = 0
		TMP = [x+stones//14 for x in TMP]
		for j in range(stones%14):
			TMP[(i+j+1)%14] += 1
		SCORES.append(sum([x for x in TMP if x % 2 == 0]))
print(max(SCORES))