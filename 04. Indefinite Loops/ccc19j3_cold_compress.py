# 6.DMOJ problem ccc19j3, Cold Compress

rows = int(input())

for row in range(rows):
	message = input()
	message_len = len(message)
	new_message = ""
	symbol_count = 0
	for i in range(message_len):
		if i == 0:
			symbol = message[i]
			symbol_count = symbol_count + 1
		elif i == message_len - 1 and i == symbol:
			symbol_count = symbol_count + 1
			new_message = new_message + str(symbol_count) + " " + symbol
		elif symbol == message[i]:
			symbol_count = symbol_count + 1
		elif i != symbol:
			new_message = new_message + str(symbol_count) + " " + symbol + " "
			symbol_count = 1
			symbol = new_message[i]

	print(new_message)


