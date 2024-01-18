# 6.DMOJ problem ccc19j3, Cold Compress

rows = int(input())

for row in range(rows):
	message = input()
	message_len = len(message)
	new_message = ""
	symbol = ""
	symbol_count = 0
	for i in range(message_len):
		if i == 0:
			symbol = message[i]
			symbol_count = 1
		elif i == message_len - 1:
			if symbol == message[i]:
				symbol_count = symbol_count + 1
				new_message = new_message + str(symbol_count) + " " + symbol
			else:
				new_message = new_message + str(symbol_count) + " " + symbol + " "
				new_message = new_message + str(1) + " " + message[i]
		elif symbol == message[i]:
			symbol_count = symbol_count + 1
		elif symbol != message[i]:
			new_message = new_message + str(symbol_count) + " " + symbol + " "
			symbol = message[i]
			symbol_count = 1

	print(new_message)


