m = int(input())
n = int(input())
rot = {0:0, 1:1, 8:8, 6:9, 9:6}
count = 0
for i in range(m, n+1):
	num = i
	n = len(list(map(int, str(i))))
	rev = 0
	for j in range(n):
		if i % 10 in rot.values():
			rev = rev*10 + rot[i % 10]
			i = (i - i % 10)/10
		else:
			num == None
			break
	if rev == num:
		count += 1
print(count)