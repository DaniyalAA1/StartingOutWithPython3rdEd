# Checkpoint Questions Chapter 3

3.1 : What is a control struture? A control structure is a logical design that controls the order in which a set of statements execute

3.2 : What is a decision structure? A decision structure is a control structure that can execute a set of statements only under certain circumstances (alson known as selection structures)

3.3 : What is a single alternative decision structure? A single alternative decision structure is a decision structure that provides only one alternative path of execution. If the condition in the diamond symbol is true, you take the alternative path

3.4 : What is a Boolean expression? A Boolean expression is an expression that is tested by the if statement. They have either true or false outputs.

3.5 : What types of relationships between values can you test with relational operators?  With relational operators, you can determine if a specific relationship exists between two values. For example, the > operatore tests if the value on the left side of the operator is greater than the value on the right side of the operator
3.6 : Write an if statement that assigns 0 to x if y is equal to 20. 
if y == 20:
    x= 0


3.7 : # Write an if statement that assigns 0.2 to 
commissionRate if sales is greater than or equal to 10000.

if sales >= 10000:
    commissionRate = 0.2

3.8 : How does a dual alternative decision strucutre work? A dual alternative decision structure is the flowchart for an if-else statement. One path is taken if the given condition is true, and another path is taken if the condition is false. 

3.9 : What statement do you use in Python to write a dual alternative decision structure? To write a dual alternative decision structure, you use the if-else statement

3.10 : When you write an if-else statement, under what circumstances do the statements that appear after the else clause execute? The statements that appear after the else clause execute if the condition is false. 

3.11 : What would the following code display?
    if 'z' < 'a':
        print('z is less than a.')
    else:
        print('z is not less than a.')
The following code will display z is not less than a.

3.12 : What would the following code display? 
s1 = 'New York'
s2 = 'Boston'

if s1 > s2: 
print(s2)
print(s1)
else:
print(s1)
print(s2)

The following code would display 
Boston 
New York

3.13 : Convert the following code to an if-elif-else statement:
if number ==1
    print ('One)
else:
    if number ==2:
        print('Two)
    else: 
        if number ==3:
            print('Three)
        else:
            print('Unknown)