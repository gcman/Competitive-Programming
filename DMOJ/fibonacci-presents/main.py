NMAX = 1000001
K,N = map(int, input().split())
cool = [0]*NMAX
dp = [0]*NMAX

for i in range(N+1):
	cool[i] = int(input())

def santa():
	if K == 1 and N >= 2:
		return max(cool[1],cool[2])
	if N + 1 < K:
		return -1

	dp[1] = cool[1]
	dp[2] = cool[1] + cool[2]

	for i in range(3, K):
		dp[i] = max(cool[i] + cool[i-1], cool[i] + dp[i-2])

	ans = dp[K-1]
	if N >= K:
		ans = max(ans, cool[K])
	return ans

print(santa())