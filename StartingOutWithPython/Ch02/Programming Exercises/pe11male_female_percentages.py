# Write a program that asks the suer for the number of males 
# and females registered in a class
# Program should display the percentage of males and females

males = float(input('Enter the number of males reigstered in the class: '))
females = float(input('Enter the number of females registered in the class :'))
total = int (males + females)
print('The class has a total of' , total, 'students')

percentageMales = float(format(males /total, '.2f'))
print('The percentage of the class that are male is', percentageMales,)

percentageFemales = float(format(females / total, '.2f'))
print('The percentage of the class that are female is', percentageFemales,)