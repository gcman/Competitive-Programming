import sys
sys.stdin = open("1.in") # COMMENT THIS BEFORE SUBMIT
input = sys.stdin.readline

S = input().strip()

def isPal(s):
	return s == s[::-1]

def main():
	if not isPal(S):
		return len(S)
	else:
		PAL = []
		for i in range(len(S)+1):
			for j in range(i+1,len(S)+1):
				s = S[i:j]
				if not isPal(s):
					PAL.append(len(s))
		if PAL:
			return max(PAL)
	return 0
print(main())