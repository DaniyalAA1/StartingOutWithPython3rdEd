# A cookie recipe calls for the following ingredients
# 1.5 cups of sugaqr
# 1 cup of butter
# 2.75 cups of flour
# This recipe produces 48 cookies
# write a program that asks the user how man cookies they want to make
# and then displays the number of cups of each ingredient needed for 
# the specified number of cookies

number_of_cookies = int(input('How many cookies would you like to make: '))
cookies = 48
sugar = 1.5
butter = 1
flour = 2.75
sentence = "this is my..."

sugarModifiedBatch = (sugar * number_of_cookies) / cookies
butterModifiedBatch = (butter * number_of_cookies) / cookies
flourModifiedBatch = (flour * number_of_cookies) / cookies

print('The number of cookies that you would like to make is', number_of_cookies)
print('The number of cups of sugar you need is', format(sugarModifiedBatch, '.2f'))
print('The number of cups  butter you need is', format(butterModifiedBatch, '.2f'))
print('The number of cups of flour you need is', format(flourModifiedBatch, '.2f'))

