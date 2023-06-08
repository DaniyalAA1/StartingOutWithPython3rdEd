print(1>2)
print(3>2)
a = 4<5
b = False
print(a)
print(f"Line 6: a: {a}")
print(f"Line 7: b: {b}")

if a:
    print("a was true on line 9")
if b:
    print("b was true on line 11")
else:
    print("b was false on line 11")
print('We\'re done with the print statments\n\n')

c = 1
if c == 1:
    print("c is one")
elif c == 2: # else-if
    print("c is 2")
elif c > 3:
    print("c is large")
else:
    print("c is smaller than one")
print("we're done with the elif example\n\n")


# nested conditions
c = 1
if c == 1:
    print("c is one")
else:
    if c == 2: # else-if
        print("c is 2")
    else:
        if c > 3:
            print("c is large")
        else:
            print("c is smaller than one")
print("we're done with the elif example\n\n")


# not equivalent to
c = 1
if c == 1:
    print("c is one")
if c == 2: # else-if
    print("c is 2")
if c > 3:
    print("c is large")
else:
    print("c is smaller than one")
print("we're done with the elif example\n\n")