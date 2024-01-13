# 6.DMOJ problem coci13c3p1, Rijeci
import math

n = int(input())
n_2 = n - 1
current_number = int(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n ) // (2**n * math.sqrt(5)))
previous_number = int(((1 + math.sqrt(5))**n_2 - (1 - math.sqrt(5))**n_2 ) // (2**n_2 * math.sqrt(5)))
#use another string to concatenate the new result

print(f"{previous_number} {current_number}")
