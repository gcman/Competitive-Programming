import sys
input = sys.stdin.readline

def prefix(p):
	m = len(p)
	pi = [0]*m
	j = 0 
	for i in range(1,m):
		while j >= 0 and p[j] !=p [i]:
			if j-1 >= 0:
				j = pi[j-1]
			else:
				j = -1 
		j += 1
		pi[i] = j
	return pi

def makeArray(s):
	s += s[::-1]
	pre = prefix(s)
	pre[0] = -1
	for i in range(len(s)):
		k = pre[i]
		while k >= 0 and s[k] != s[i]:
			k = pre[k]
		if i + 1 < len(s):
			pre[i+1] = k+1
	L = min(len(s)//2,pre[len(s)-1])
	P = [False for _ in range(len(s)//2+1)]
	while L >= 0:
		P[L] = True
		L = pre[L]
	return P

def findGreatestInd(s):
	return [i for i,x in enumerate(makeArray(s)) if x == True][::-1]

def KMP(text, pattern):
	pattern = list(pattern)
	shifts = [1] * (len(pattern) + 1)
	shift = 1
	for pos in range(len(pattern)):
		while shift <= pos and pattern[pos] != pattern[pos-shift]:
			shift += shifts[pos-shift]
		shifts[pos+1] = shift
	startPos = 0
	matchLen = 0
	for c in text:
		while matchLen == len(pattern) or matchLen >= 0 and pattern[matchLen] != c:
			startPos += shifts[matchLen]
			matchLen -= shifts[matchLen]
		matchLen += 1
		if matchLen == len(pattern):
			yield startPos

def findPalPre(s):
	for x in findGreatestInd(s):
		if len(list(KMP(s,s[:x]))) >= 2:
			return x

S = input().strip()
print(findPalPre(S))