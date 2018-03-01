"""
ID: manga1
LANG: PYTHON3
TASK: ride
"""
with open("ride.in", "r") as f:
	comet = f.readline()
	group = f.readline()

def value(a):
	to_mult = [ord(char.lower()) - 96 for char in a]
	count = 1
	for x in to_mult:
		count *= x
	return count % 47

with open("ride.out", "w") as f:
	if value(comet) == value(group):
		f.write("GO\n")
	else:
		f.write("STAY\n")