# DMOJ problem mccc6j3, RGB Words

length = int(input())
word = input()

rgb_count = 0
i = 0
beginning = -1
while i < len(word):
	r_count = 0
	g_count = 0
	b_count = 0

	for j in range(i, len(word)):
		#print(i,j)
		if word[j] == "R":
			r_count = r_count + 1
			i = j
		elif word[j] == "G" and r_count == 1 and g_count == 0:
			g_count = 1
		elif word[j] == "G" and r_count == 1 and g_count == 1:
			break
		elif word[j] == "B" and r_count == 1 and g_count == 1:
			b_count = b_count + 1
			
	rgb_count = rgb_count + b_count
	i = i + 1

print(rgb_count)
