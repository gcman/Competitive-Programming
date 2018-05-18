import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

def most_common (lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

print(most_common([S[i:i+2] for i in range(N-1)]))