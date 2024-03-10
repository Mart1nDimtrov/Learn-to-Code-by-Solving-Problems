# DMOJ problem sac22cc4jp1, Obligatory DeMello Problem

vowels = "aeiouy"
word = input()
vowel_count = len([x for x in word if x in vowels])

if vowel_count >= 2:
	print("good")
else:
	print("bad")