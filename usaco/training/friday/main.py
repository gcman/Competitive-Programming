"""
ID: manga1
LANG: PYTHON3
TASK: friday
"""
with open("friday.in", "r") as f:
	n = int(f.readline())

freq = [0] * 7
date = [1, 1, 1900]

def end_day(m):
	month = m[1]
	year = m[2]
	if month in [4,6,9,11]:
		return 30
	elif month == 2:
		if year % 4 == 0:
			if year % 100 == 0:
				if year % 400 == 0:
					return 29
				else:
					return 28
			return 29
		else:
			return 28
	else:
		return 31

def increment_day(m):
	if m[0] == end_day(m):
		m[0] = 1
		if m[1] == 12:
			m[1] = 1
			m[2] += 1
		else:
			m[1] += 1
	else:
		m[0] += 1

count = 2 # Starts on Monday
while date != [31, 12, 1900+n-1]:
	count += 1
	increment_day(date)
	if date[0] == 13:
		freq[count%7] += 1

with open("friday.out", "w") as f:
	f.write(" ".join(map(str, freq)) + "\n")