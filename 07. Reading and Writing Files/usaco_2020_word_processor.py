# USACO 2020 January Bronze Contest problem Word Processor

new_string = ""

input_file = open("word.in", "r")
input_params = input_file.readline().split()
n = int(input_params[0])
k = int(input_params[1])
count = 0
words = input_file.readline().split()

for i in range(len(words)):
	if len(words[i]) + count <= k:
		count = count + len(words[i])
		if i == 0:
			new_string = new_string + words[i]
		else:
			new_string = new_string + " " + words[i]
	else:
		count = len(words[i])
		if i == 0:
			new_string = new_string +  words[i]
		else:
			new_string = new_string + "\n" + words[i]

input_file.close()

output_file = open("word.out", "w")
output_file.write(new_string)

output_file.close()