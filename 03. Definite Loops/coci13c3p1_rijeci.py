# 6.DMOJ problem coci13c3p1, Rijeci

numbers_pressed = int(input())
previous_number = 0
current_number = 1
#use another string to concatenate the new result

for number in range(numbers_pressed-1):
	swap = current_number
	current_number = previous_number + current_number
	previous_number = swap

print(f"{previous_number} {current_number}")
