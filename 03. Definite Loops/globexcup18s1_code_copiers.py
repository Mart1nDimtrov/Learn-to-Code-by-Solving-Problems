# DMOJ problem globexcup18s1, Code Copiers

coders = int(input())
coders_list = set(list(map(int, input().split())))

print(coders - len(coders_list) + 1)