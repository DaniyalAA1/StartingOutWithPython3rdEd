# Write a program that asks for the price of each item 
# and then displays the subtotal of the sale, 
# the amount of sales tax, and the total
# the sales tax is 7 percent

item1 = float(input('What is the price of your first item?: '))
subtotal = (item1)
print('Your subtotal is', subtotal)

item2 = float(input('What is the price of your second item?: '))
subtotal = (item1 + item2)
print('Your new subtotal is ', subtotal)

item3 = float(input('What is the price of your third item?: '))
subtotal = (item1 + item2 + item3)
print('Your new subtotal is', subtotal)

item4 = float(input('What is the price of your fourth item?: '))
subtotal = (item1 + item2 + item3 + item4)
print('Your new subtotal is', subtotal)

item5 = float(input('What is the price of your fifth item?: '))
subtotal = (item1 + item2 + item3 + item4 + item5)
print('Your new subtotal is', subtotal)

print('The sales tax is 7 percent')
sales_tax = 0.07 * subtotal

total = float(sales_tax + subtotal)
print('Your total is $', \
      format(total,'.2f') )