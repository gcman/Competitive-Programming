n = int(input())

def main():
	if n == 1:
		return 0
	else:
		points = [list(map(int, input().split())) for i in range(n)]