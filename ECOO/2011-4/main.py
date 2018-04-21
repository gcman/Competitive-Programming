n = int(input())
P = [tuple(map(int, input().split())) for i in range(n)]
print(P)
P[1] = sorted(P,key=lambda x: x[1])[0]
P = [P[n-1]] + P

def ccw(a,b,c):
	return (b[0] - a[0])*(c[1] - a[1]) * (b[1] - a[1])*(c[0] - a[0])

P = [P[0],P[1]] + sorted(P[2:],key=lambda x: -(x[0] - P[1][0])/(x[1] - P[1][1]))

M = 1
for i in range(2,n+1):
	print(M)
	while ccw(P[M-1],P[M],P[i]):
		if M > 1:
			M -= 1
			continue
		elif i == n:
			break
		else:
			i += 1
	M += 1
	temp1 = P[M] 
	temp2 = P[i]
	P[M] = temp2
	P[i] = temp1

print(M)