# 1.DMOJ problem wc16c1j1, A Spooky Season

# Get the input as a number.
spooky_number = int(input())
# Use a list comprehension to have the correct number of  o's and 
# then join the list into a string.
spooky_word = "sp" + "".join(['o' for x in range(spooky_number)]) + "ky"
print(spooky_word)
