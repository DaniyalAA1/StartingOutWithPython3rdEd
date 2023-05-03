# Write a program that asks the user to enter
# the total swuare feet in a tract of land
# and calculates the number of acres in the tract

total_square_feet = input('Enter the total square feet in your tract of land: ')
acres = int(total_square_feet) // 43,560
print('Based on your total square footage, you have', acres,'acres of land')