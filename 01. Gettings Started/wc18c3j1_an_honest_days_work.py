# 5.DMOJ problem wc18c3j1, An Honest Day’s Work (Hint: how can you determine the number 
# of bottle caps and the total paint required by those bottle caps?)

p = int(input())
b = int(input())
d = int(input())

earned = ((p // b) * d) + (p % b)
print(earned)