# 1.DMOJ problem wc16c1j1, A Spooky Season

# Get the input as a number.
spooky_number = int(input())
spooky_word = "sp"

# Use the range function for faster processing.
for word in range(spooky_number):
	spooky_word += "o"

spooky_word += "ky"
print(spooky_word)