# This program demonstrates variable reassignment.
# Assign a value to the dollars variable. 
dollars = 2.75
print('I have', dollars, 'in my account.')

# Reassign dollars so it references
# a different value
dollars = 99.95
print(f'But now I have {dollars} in my account!\n\n')

# deomnstateing multi line strings
dollars = 45.456
print(f"""But now I have {dollars} in my account!
But now I have {dollars:.2} in my account!
But now I have {dollars:.1} in my account!
But now I have {dollars:10.4} in my account!
""")