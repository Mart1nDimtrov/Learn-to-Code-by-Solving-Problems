# 3.DMOJ problem ccc11s1, English or French

rows = int(input())
english_letters = 0
french_letters = 0

for row in range(rows):
	text = input()
	french_letters = french_letters + text.count('s') + text.count('S')
	english_letters = english_letters + text.count('t') + text.count('T')

if english_letters > french_letters:
	print("English")
elif french_letters >= english_letters:
	print("French")