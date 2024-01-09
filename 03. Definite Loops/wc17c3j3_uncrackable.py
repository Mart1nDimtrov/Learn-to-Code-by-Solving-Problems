# 1.DMOJ problem wc17c3j3, Uncrackable

password = input()
upper_count = 0
lower_count = 0
digit_count = 0

for char in password:
	if char.isupper():
		upper_count = upper_count + 1
	elif char.islower():
		lower_count = lower_count + 1
	elif char.isdigit():
		digit_count = digit_count + 1

if (upper_count >= 2 
	and lower_count >= 3
	and digit_count >= 1 
    and (upper_count + lower_count + digit_count) >= 8
    and (upper_count + lower_count + digit_count) <= 12):
	print("Valid")
else:
	print("Invalid")