# DMOJ problem tle17c6p1, Molecules

molecules_lenght = int(input())
molecules = input()
molecules_dict = {}

for i in range(molecules_lenght):
	if molecules[i] in molecules_dict:
		molecules_dict[molecules[i]] = molecules_dict[molecules[i]] + 1
	else:
		molecules_dict[molecules[i]] = 1

if max(molecules_dict.values()) <= molecules_lenght // 2 and molecules_lenght % 2 == 0:
	print("Yes")
else:
	print("No")


