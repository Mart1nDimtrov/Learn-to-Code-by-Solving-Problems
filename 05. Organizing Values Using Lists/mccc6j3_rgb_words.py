# DMOJ problem mccc6j3, RGB Words

word_length = int(input())
word = input()
count = 0

for i in range(word_length):
	r = 0
	g = 0
	b = 0
	for j in range(i, word_length):
		if word[j] == "R":
			r = 1
		elif word[j] == "G" and r == 0:
			break
		elif word[j] == "B" and g == 0 and r == 0:
			break
		elif word[j] == "G" and g == 0 and r == 1:
			g = 1
		elif word[j] == "G" and g == 1:
			g = 1
			break
		elif word[j] == "B" and g == 1:
			b = 1
			count = count + 1

print(count)
