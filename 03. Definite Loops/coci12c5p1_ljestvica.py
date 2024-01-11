# 5.DMOJ problem coci12c5p1, Ljestvica

notes = input()
start = 1
a_minor = 0
c_major = 0

for tone in notes:
	if tone != '|' and start == 1:
		if tone == "A" or tone == "D" or tone == "E":
			a_minor = a_minor + 1
			start = 0
		elif tone == "C" or tone == "F" or tone == "G":
			c_major = c_major + 1	
			start = 0
	elif tone == "|":
		start = 1

if a_minor > c_major:
	print("A-mol")
elif c_major > a_minor:
	print("C-dur")
elif notes[-1] == "C":
	print("C-dur")
elif notes[-1] == "A":
	print("A-mol")