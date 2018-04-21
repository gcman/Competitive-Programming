import sys

def add(a,b): # Take reversed as argument
	if len(a) > len(b):
		a,b = b,a
	A = len(a)
	B = len(b)
	out = ""
	carry = 0
	for i in range(A):
		S = int(a[i]) + int(b[i]) + carry
		out += str(S % 10)
		carry = S // 10
	for i in range(A,B):
		S = int(b[i]) + carry
		out += str(S % 10)
		carry = S // 10
	if carry:
		out += str(carry)
	return out

total = "0"
current = "0"
n = int(input())
instructions = sys.stdin.readline().strip()

for x in instructions:
	if x == "-":
		current = current[1:]
	else:
		current = x + current
	total = add(current,total)
print(total[::-1])	