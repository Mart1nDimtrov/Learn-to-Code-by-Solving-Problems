# 8.DMOJ problem dmopc14c4p1, New Key

# first find the right functions to use - ord(),chr()
message = input()

for letter in message:
	if ord(letter) >= 49 and ord(letter) <= 59:
		print(chr(ord(letter) + 16), end="")
	elif ord(letter) >= 66 and ord(letter) <= 74:
		print(chr(ord(letter) + 9), end="")
	elif ord(letter) >= 76 and ord(letter) <= 80:
		print(chr(ord(letter) + 9), end="")
	elif ord(letter) == 48:
		print('9', end="")
	elif ord(letter) == 65:
		print('J', end="")
	elif ord(letter) == 75:
		print('T', end="")
