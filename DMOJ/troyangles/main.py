import sys
sys.stdin = open("data.txt")
input = sys.stdin.readline

N = int(input())
grid = [input().strip() for _ in range(N)]
dp = [[int(1e6) for _ in range(N)] for _ in range(N)]

S = 0
for i in range(N-1,-1,-1):
	for j in range(N):
		if grid[i][j] != "#":
			dp[i][j] = 0
		elif j in [0,N-1] or i == N-1 or grid[i+1][j] != "#":
			dp[i][j] = 1
		else:
			dp[i][j] = min(dp[i+1][j-1], dp[i+1][j+1]) + 1
		S += dp[i][j]
print(S)