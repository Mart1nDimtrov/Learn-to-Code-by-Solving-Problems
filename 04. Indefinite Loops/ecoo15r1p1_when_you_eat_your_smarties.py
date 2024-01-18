# 5.DMOJ problem ecoo15r1p1, When You Eat Your Smarties
import math

smarties = input()
orange = 0
blue = 0
green = 0
yellow = 0
pink = 0
violet = 0
brown = 0
red = 0
box_count = 0
total = 0

while box_count < 10:
															
	if smarties == "red":
		red = red + 1
	elif smarties == "orange":
		orange = orange + 1
	elif smarties == "blue":
		blue = blue + 1
	elif smarties == "green":
		green = green + 1
	elif smarties == "yellow":
		yellow = yellow + 1
	elif smarties == "pink":
		pink = pink + 1
	elif smarties == "violet":
		violet = violet + 1
	elif smarties == "brown":
		brown = brown + 1
	elif smarties == "end of box":
		total = total + (red * 16)	
		total = total + (math.ceil(orange / 7) + math.ceil(blue / 7) +
				 math.ceil(green / 7) + math.ceil(yellow / 7) +
				 math.ceil(pink / 7) + math.ceil(violet / 7) +
				 math.ceil(brown / 7)) * 13 
		print(total)
		orange = 0
		blue = 0
		green = 0
		yellow = 0
		pink = 0
		violet = 0
		brown = 0
		red = 0
		total = 0
		box_count = box_count + 1

	if box_count < 10:
		smarties = input()








