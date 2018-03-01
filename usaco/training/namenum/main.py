"""
ID: manga1
LANG: PYTHON3
TASK: namenum
"""
with open("dict.txt","r") as f:
	NAMES = [line.strip() for line in f.readlines()]

conv = {"2": ["A","B","C"],
		"3": ["D","E","F"],
		"4": ["G","H","I"],
		"5": ["J","K","L"],
		"6": ["M","N","O"],
		"7": ["P","R","S"],
		"8": ["T","U","V"],
		"9": ["W","X","Y"]}

def product(ar_list):
	if not ar_list:
		yield ()
	else:
		for a in ar_list[0]:
			for prod in product(ar_list[1:]):
				yield (a,)+prod

with open("namenum.in", "r") as f:
	out = [name for name in ["".join(list(x)) for x in product([conv[x] for x in f.readline().strip()])] if name in NAMES]

with open("namenum.out", "w") as f:
	if not out:
		f.write("NONE\n")
	for x in out:
		f.write(x + "\n")