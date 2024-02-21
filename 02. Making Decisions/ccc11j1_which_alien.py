# DMOJ problem ccc11j1, Which Alien?

n_antennae = int(input())
n_eyes = int(input())


if n_antennae >= 3 and n_eyes <= 4:
	print("TroyMartian")
if n_antennae <= 6 and n_eyes >= 2:
	print("VladSaturnian")
if n_antennae <= 2 and n_eyes <= 3:
	print("GraemeMercurian")