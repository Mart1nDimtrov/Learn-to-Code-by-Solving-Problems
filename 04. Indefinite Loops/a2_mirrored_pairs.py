# DMOJ problem a2, Mirrored Pairs

pair = input().lower()
print("Ready")

while pair != "  ":

	if "q" in pair and "p" in pair:
		print("Mirrored pair")
	elif "b" in pair and "d" in pair:
		print("Mirrored pair")
	else:
		print("Ordinary pair")

	pair = input().lower()


