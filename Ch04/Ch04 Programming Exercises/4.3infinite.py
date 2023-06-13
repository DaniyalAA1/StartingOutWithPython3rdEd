# This program demonstrates an infinite loop.
# Create a variable to control the loop.
keep_going = 'y'

# Warning! infinite loop!
while keep_going =='y':
    #get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the comission.
    commission = sales * comm_rate

    # Display the comission.
    print('The comission is $', \
         format(commission, ',.2f'),sep='')