# 2.DMOJ problem wc15c2j1, A New Hope

# Get the input as a number.
far_number = int(input())
far_word = "A long time ago in a galaxy "

# Use the range function for faster processing.
for step in range(far_number):
	if step == far_number - 1:
		far_word += "far "
	else:
		far_word += "far, "

far_word += "away..."
print(far_word)