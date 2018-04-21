N,K = map(int,input().split())
dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
print(dp)
for x in range(N):
	for y in range(N):
		for z in range(N):
			print(x,y,z)
			ans = dp[x][y+1][z+1]
			ans += dp[x][y][z+1]
			ans += sum([dp[x][y+2][z-i+1] for i in range(y+1)])
			dp[x+1][y+1][z+1] = ans
print(dp[N][0][K])