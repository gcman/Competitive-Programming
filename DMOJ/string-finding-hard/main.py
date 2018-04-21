from __future__ import generators
	
def kmpFirstMatch(pattern, text):
	shift = computeShifts(pattern)
	startPos = 0
	matchLen = 0
	for c in text:
		while matchLen >= 0 and pattern[matchLen] != c:
			startPos += shift[matchLen]
			matchLen -= shift[matchLen]
		matchLen += 1
		if matchLen == len(pattern):
			return startPos

# Construct shift table used in KMP matching
#
# Time analysis: each iteration of either loop increases shift+pos
# This quantity starts at 0 and ends at most at 2*p
# So total time is O(p).
#
def computeShifts(pattern):
	shifts = [None] * (len(pattern) + 1)
	shift = 1
	for pos in range(len(pattern) + 1):
		while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
			shift += shifts[pos-shift-1]
		shifts[pos] = shift
	return shifts

print(kmpFirstMatch("higuyshowsitgoinghiguys","higuys"))