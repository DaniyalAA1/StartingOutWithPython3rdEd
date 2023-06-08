# Write a program that asks the user to enter
# the total swuare feet in a tract of land
# and calculates the number of acres in the tract

total_square_feet = float(input('Enter the total square feet in your tract of land: '))
acres = float(total_square_feet) / 43560
print('Based on your total square footage, you have', 
      format(acres, '.2f') ,'acres of land')