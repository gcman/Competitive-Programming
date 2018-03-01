first_day, days = map(int, input().split())
out = "Sun Mon Tue Wed Thr Fri Sat\n"
for i in range(1,days + first_day):
	day = i - first_day + 1
	if day <= 0:
		out += "   "
	else:
		out += " "*(3 - len(str(day))) + str(day)
	if day != days and i % 7 != 0:
		out += " "
	if i % 7 == 0 or day == days:
		out += "\n"
print(out)