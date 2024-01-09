# 2.DMOJ problem coci18c3p1, Magnus

message = input()
block = ""
block_count = 0

for char in message:
	if block == "" and char == "H":
		block = char
	elif block == "H" and char == "O":
		block = block + char
	elif block == "HO" and char == "N":
		block = block + char
	elif block == "HON" and char == "I":
		block = ""
		block_count = block_count + 1

print(block_count)

