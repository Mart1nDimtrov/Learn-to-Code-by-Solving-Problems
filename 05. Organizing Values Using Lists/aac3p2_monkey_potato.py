# DMOJ problem aac3p2, Monkey Potato

digit_input = list(map(int, input().split()))
k = digit_input[0]
d = digit_input[1]
digits = list(map(int, input().split()))

final_digit = str(min([d for d in digits if d > 0])) * k

if final_digit[0] != "0":
	print(final_digit)
else:
	print(-1)