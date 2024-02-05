# DMOJ problem ccc01j1, Dressing Up
import math

h = int(input())
change = h // 2
stars = 1
for i in range(h):
	if i >= change:
		print((stars * "*") + (((h * 2) - (stars * 2)) * " ") + (stars * "*"))
		stars = stars - 2
	else:
		print((stars * "*") + (((h * 2) - (stars * 2)) * " ") + (stars * "*"))
		stars = stars + 2
