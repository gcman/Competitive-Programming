N = int(input())

for i in range(N):
	count = 2
	s = input().strip()
	for j in range(1,len(s)):
		for k in range(len(s) - j + 1):
			if s.index(s[k:j+k]) == k:
				count += 1
	print(count)