# DMOJ problem ccc13j2, Rotating letters

sign = input()
acceptable_letters = "IOSHZXN"
length_filtered = len([x for x in sign if x in acceptable_letters])

if length_filtered == len(sign):
	print("YES")
else:
	print("NO")