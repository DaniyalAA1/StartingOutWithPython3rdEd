# Write a program that asks the user to enter
# the amount of a purchase
# Create a program that computes state and 
# county taxes. State tax is 5 percent
# county tax is 2.5 percent
# the program will display the purchase amount
#, the state sales tax, the county sales tax, the
# total sales tax, and the total of the sale

purchase = float(input('What is the amount of your purchase? :'))
state_tax = (purchase * 0.05)
print('The state sales tax on your purchase is', \
      format(state_tax, '.2f'))
county_tax = (purchase * 0.025)
print('The county tax on your purchase is', \
      format(county_tax, '.2f'))
total_sales_tax = county_tax + state_tax
print('Your total sales tax is',  
      format(total_sales_tax, '.2f'))
total_price = purchase + total_sales_tax
print('Your total price is', total_price)