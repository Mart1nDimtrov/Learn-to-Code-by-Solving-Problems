# DMOJ problem aac3p2, Monkey Potato

digit_input = input().split()
k = int(digit_input[0])
d = int(digit_input[1])
digits = input().split()

min_digit = ""
min_digit = str(min([int(d) for d in digits if d != "0"], default="0"))

if min_digit == "0":
	print(-1)
elif "0" in digits and k > 2:
	print(min_digit + ("0" * (k - 2)) + min_digit)
else:
	print(min_digit * k)

