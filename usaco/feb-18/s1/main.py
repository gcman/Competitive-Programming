with open("reststops.in", "r") as f:
	L, N, vf, vb = map(int, f.readline().split())
	stops = []
	for i in range(N):
		pos, taste = map(int, f.readline().split())
		stops.append((pos,taste))

STOPAT = []
max_taste = 0
stops.reverse()
for x in stops:
	if x[1] > max_taste:
		STOPAT.append(x)
		max_taste = x[1]
STOPAT.reverse()

pos = 0
total = 0
for x in STOPAT:
	d = x[0] - pos
	t = d*(vf - vb)
	total += t*x[1]
	pos = x[0]

with open("reststops.out", "w") as f:
	f.write(str(total))