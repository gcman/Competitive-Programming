start = {}
stop = {}
w = []
total = 0
alone = {}
wstart = 0
astart = 0
temp = 0

def do_alone(start,stop):
	if w[0] not in alone:
		alone[w[0]] = 0
	alone[w[0]] += stop - start

with open("lifeguards.in", "r") as f:
	n = int(f.readline())
	for i in range(1,n+1):
		t1, t2 = map(int, f.readline().split())
		start[t1] = i
		stop[t2] = i
	for x in sorted(list(start.keys()) + list(stop.keys())):
		if x in start:
			w.append(start[x])
			if len(w) == 1:
				wstart = x
		if x in stop:
			w.remove(stop[x])
			if len(w) == 0:
				total += x - wstart
				wstart = 0
		if len(w) == 1:
			astart = x
			temp = w[0]
		else:
			y = w[0] if len(w) != 0 else temp
			if y not in alone:
				alone[y] = 0
			alone[y] += x - astart

with open("lifeguards.out", "w") as f:
	f.write(str(total - min(alone.values())))