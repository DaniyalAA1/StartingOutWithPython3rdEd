# write a program that asks the user for a number in the range
# of 1 through 7
# The program shold display the corresponding day of the week
# where 1 = monday, 2= tuesday, 3 = wednesday, 4 = thursday,
# 5 = friday, 6 = saturday, 7 = sunday
# The program should display an error message if the user enters 
# a number that is outside the range of 1 through 7 

monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5 
saturday = 6
sunday = 7
range = (1,7)

number = int(input('Enter a number that is in\
the range of 1 through 7:' ))

if number < 1 or number > 7:
    print('Error, number entered is not with given range')