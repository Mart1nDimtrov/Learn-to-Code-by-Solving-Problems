# 5.DMOJ problem coci12c5p1, Ljestvica

notes = input().split("|")
start = 1
a_minor = 0
c_major = 0

for i in range(len(notes)):
	if notes[i][0] == "A" or notes[i][0] == "D" or notes[i][0] == "E":
		a_minor = a_minor + 1
	elif notes[i][0] == "C" or notes[i][0] == "F" or notes[i][0] == "G":
		c_major = c_major + 1

if a_minor > c_major:
	print("A-mol")
elif c_major > a_minor:
	print("C-dur")
elif notes[-1][-1] == "C":
	print("C-dur")
elif notes[-1][-1] == "A":
	print("A-mol")