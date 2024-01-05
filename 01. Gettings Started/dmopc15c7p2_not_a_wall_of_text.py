# 6.DMOJ problem dmopc15c7p2, Not a Wall of Text

text = input()
word_count = 0
new_word = 0

for letter in text:
	if letter != " " and new_word == 0:
		word_count = word_count + 1
		new_word = 1
	elif letter == " ":
		new_word = 0

print(word_count)