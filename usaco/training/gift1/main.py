"""
ID: manga1
LANG: PYTHON3
TASK: gift1
"""
with open("gift1.in", "r") as f:
	n = int(f.readline())
	account = {}
	initial = {}
	order = []
	for i in range(n):
		name = f.readline().strip()
		account[name] = 0
		order.append(name)
	for i in range(n):
		giver = f.readline().strip()
		money = f.readline().split()
		gifts = int(money[1])
		money = int(money[0])
		account[giver] += money
		initial[giver] = money
		for j in range(gifts):
			recipient = f.readline().strip()
			account[recipient] += money // gifts
			account[giver] -= money // gifts

with open("gift1.out", "w") as f:
	for x in order:
		f.write(x + " " + str(account[x] - initial[x]) + "\n")