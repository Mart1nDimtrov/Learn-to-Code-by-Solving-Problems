# DMOJ problem coci08c3p2, Secret Sentence

word = list(input())
word_length = len(word)
i = 0
vowels = "aeiou"

while i < word_length:

	if word[i] in vowels:
		word.pop(i+1)
		word.pop(i+1)

	i = i + 1
	word_length = len(word)

print("".join(word))