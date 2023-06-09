# This program calculates sales commissions

# Create a variable to control the loop.
keep_going ='y'

# Calculate a series of commissions.
while keep_going == 'y':
    # Get salesperson's sales and comission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the comission
    comission = sales * comm_rate

    # Display the commission
    print('The commission is $', \
          format(comission, ',.2f'), sep='')
    # See if the user wants to do another one
    keep_going = input('Do you want to calculate another ' + \
                       'commission (Enter y for yes): ')