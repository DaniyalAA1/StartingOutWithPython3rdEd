# Program calculates total amount of a meal purchased
# ask user fir the charge of the food
# calculate the amnount of an 18 percent tip
# calculate the 7 percent sales tax
# display all and the total

food = float(input('Enter the charge for the food $: '))
print(food)
tip = float(format(food * 0.18, '.2f'))
print('Your 18 percent tip of the food charge is $', tip)
tax = float(format(food * 0.07, '.2f'))
print('The 7 percent sales tax is $', tax)
total = float(format(food + tip + tax, '.2f'))
print('Your total for the charge of the food, the tip, and tax is $', total)