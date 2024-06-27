# DMOJ problem stnbd3, Rinslet Laurenfrost

known_word = input()
new_word = input()

add = 0
remove = 0

known_word_dict = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
new_word_dict = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}

for l in known_word:
	known_word_dict[l] = known_word_dict[l] + 1

for l_2 in new_word:
	new_word_dict[l_2] = new_word_dict[l_2] + 1

for key, value in known_word_dict.items():
	if value != 0:
		if new_word_dict[key] > value:
				remove = remove + (new_word_dict[key] - value)
		elif new_word_dict[key] < value:
				add = add + (value - new_word_dict[key])
	else:
		if new_word_dict[key] != 0:
			add = add + new_word_dict[key]

print(add + remove)



