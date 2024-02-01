# DMOJ problem bpc1j1, Facial Recognition

number_of_strings = int(input())
faces_count = 0
for i in range(number_of_strings):
	if input() == "face":
		faces_count = faces_count + 1

print(faces_count) 
