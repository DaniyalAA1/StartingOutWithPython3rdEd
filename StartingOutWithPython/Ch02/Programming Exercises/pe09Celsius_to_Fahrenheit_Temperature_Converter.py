# Write a program that converts celsius temperature to fahrenheit temperatures
# formula is F = ((9/5) * C) + 32
# ask user to enter temp in Cel then display the temp in Fahr

celsius = float(input('Enter a temperature in Celsius: '))
fahrenheit = float(format((9/5 * celsius) + 32, '.2f'))
print('Your temperature in Fahrenheit is', fahrenheit, 'degrees')