q = int(input())
t1 = int(input())
t2 = int(input())
t3 = int(input())
count = 0
while q > 0:
	q -= 1
	if count % 3 == 0:
		t1 += 1
		if t1 % 35 == 0:
			q += 30
	elif count % 3 == 1:
		t2 += 1
		if t2 % 100 == 0:
			q += 60
	else:
		t3 += 1
		if t3 % 10 == 0:
			q += 9
	count += 1
print("Martha plays {} times before going broke.".format(count))