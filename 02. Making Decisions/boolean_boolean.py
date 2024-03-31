# DMOJ problem boolean, Boolean

boolean_input = input().split()

if len(boolean_input) % 2 == 1 and boolean_input[-1] == "True":
	print("True")
elif len(boolean_input) % 2 == 0 and boolean_input[-1] == "False":
	print("True")
else:
	print("False")