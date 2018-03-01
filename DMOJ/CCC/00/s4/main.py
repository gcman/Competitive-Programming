goal = int(input())
n = int(input())
clubs = sorted([int(input()) for i in range(n)])

dp_min = [goal+1 for i in range(goal+1)]
dp_min[0] = 0

for i in range(1,goal+1):
	for j in range(n):
		if clubs[j] <= i and dp_min[i - clubs[j]] + 1 < dp_min[i]:
			dp_min[i] = dp_min[i - clubs[j]] + 1

if dp_min[goal] == goal+1:
	print("Roberta acknowledges defeat.")
else:
	print("Roberta wins in {} strokes.".format(dp_min[goal]))