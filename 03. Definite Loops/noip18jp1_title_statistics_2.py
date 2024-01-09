# DMOJ problem noip18jp1, Title Statistics

title = input()
char_count = 0

for char in title:
	if char != " " and char != "\n":
		char_count = char_count + 1


print(char_count)