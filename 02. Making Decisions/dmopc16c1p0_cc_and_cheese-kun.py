# 4.DMOJ problem dmopc16c1p0, C.C. and Cheese-kun

pizza_units = int(input())
pizza_coverage = int(input())
statement = ""

if pizza_units == 3 and pizza_coverage >= 95:
	statement = "absolutely"
elif pizza_units == 1 and pizza_coverage <= 50:
	statement = "fairly"
else:
	statement = "very"


print(f"C.C. is {statement} satisfied with her pizza.")
