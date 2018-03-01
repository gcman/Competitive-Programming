t_max = []
with open("lifeguards.in", "r") as f:
	def lines():
		f.seek(1)
		return ((k[0],k[1]) for k in [l.strip().split(" ") for l in f] if k != [""])
	for line_cut in lines(): #add all lines except for one
		t = set()
		for line in lines():
			if line[1] != line_cut[1]:
				t1 = int(line[0])
				t2 = int(line[1])
				for k in range(t1,t2):
					t.add(k)
		t_max.append(len(t))
print(max(t_max))
with open("lifeguards.out", "w") as f:
	f.write(str(max(t_max)))