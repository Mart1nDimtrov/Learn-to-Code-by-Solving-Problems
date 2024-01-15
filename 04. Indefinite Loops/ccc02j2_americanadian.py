# 3.DMOJ problem ccc02j2, AmeriCanadian

word = input()
vowels = "aeiouy"
while word != "quit!":
	if (word[-3] not in vowels and 
		word[-2:] == "or" and
		len(word) > 4):
		print(word[:-2] + "our")
	else:
		print(word)
	word = input()