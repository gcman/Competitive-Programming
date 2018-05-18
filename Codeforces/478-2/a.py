import sys
input = sys.stdin.readline

N = int(input())
S = input().split()

unique = set()

for x in S:
	out = set()
	for char in x:
		out.add(char)
	unique.add("".join(sorted(out)))
print(len(unique))