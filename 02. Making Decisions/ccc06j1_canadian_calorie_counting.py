# 1.DMOJ problem ccc06j1, Canadian Calorie Counting

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

# Use a list to avoid conditions.
burger_menu = [461, 431, 420, 0]
drink_menu = [130, 160, 118, 0]
side_menu = [100, 57, 70, 0]
dessert_menu = [167, 266, 75, 0]

total = burger_menu[burger - 1] + drink_menu[drink - 1] + side_menu[side - 1] + dessert_menu[dessert - 1]

print(f"Your total Calorie count is {total}.")