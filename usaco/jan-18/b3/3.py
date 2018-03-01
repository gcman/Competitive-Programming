def selectionSort(a):
	sorts = set()
	for x in range(len(a)-1,0,-1): #x represents a slot to be considered for sorting
		sorts.add(tuple(a))
		max_pos = 0
		for loc in range(1,x+1):
			if a[loc] > a[max_pos]:
				max_pos = loc
		temp = a[x]
		a[x] = a[maxpos]
		a[maxpos] = temp
	return(len(sorts)-1)

to_sort = []

with open("outofplace.in", "r") as f:
	n = int(f.readline().strip())
	for i in range(n):
		to_sort.append(int(f.readline().strip()))

with open("outofplace.out", "w") as g:
	g.write(str(selectionSort(to_sort)))