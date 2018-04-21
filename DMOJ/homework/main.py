N = 10**7

primacity = [0]*(N+1)
for i in range(2,N+1):
  if primacity[i] == 0:
    for j in range(i,N+1,i):
      primacity[j] += 1

T = int(input())
for i in range(T):
  A,B,K = map(int, input().split())
  count = sum([1 for x in range(A,B+1) if primacity[x] == K])
  print("Case #{}: {}".format(i+1,count))