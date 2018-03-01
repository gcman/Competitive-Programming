n = int(input())
rivers = [int(input()) for i in range(n)]
while True:
	i = int(input())
	if i == 99:
		split = int(input()) - 1
		ratio = int(input())
		rivers.insert(split + 1, 0)
		transfer = rivers[split] * ratio/100
		rivers[split + 1] = rivers[split] - transfer
		rivers[split] = transfer
	elif i == 88:
		join = int(input()) - 1
		rivers[join] += rivers.pop(join + 1)
	elif i == 77:
	  break
print(" ".join(map(str, map(int, rivers))))