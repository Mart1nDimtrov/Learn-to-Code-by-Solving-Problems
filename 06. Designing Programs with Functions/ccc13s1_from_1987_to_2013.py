# 1.DMOJ problem ccc13s1, From 1987 to 2013

def check_unique(year_list):
	"""Accept a year as a list 
	and check if every digit is unique.
	Return the year if it is,
	false otherwise"""
	is_unique = True

	for i in range(len(year_list)):
		if len([d for d in year_list if d == year_list[i]]) > 1:
			is_unique = False
			return is_unique

	return is_unique

year = int(input())
year_found = 0
while year_found == 0:
	year = year + 1
	year_list = str(year)

	if check_unique(year_list) == True:
		print(year)
		year_found = 1