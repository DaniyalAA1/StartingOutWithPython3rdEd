p1 = " "
p2 = " "
p3 = " "
p4 = " "
p5 = " "
p6 = " "
p7 = " "
p8 = " "
p9 = " "

choice = int(input("First move, choose postion (1-9): "))
if choice == 1:
    p1 = "x"
elif choice == 2:
    p2 = "x"
elif choice == 3:
    p3 = "x"
elif choice == 4:
    p4 = "x"
elif choice == 5:
    p5 = "x"
elif choice == 6:
    p6 = "x"
elif choice == 7:
    p7 = "x"
elif choice == 8:
    p8 = "x"
elif choice == 9:
    p9 = "x"
else:
    "you entered something bad... program ending"

print(f"""
[{p1}][{p2}][{p3}]
[{p4}][{p5}][{p6}]
[{p7}][{p8}][{p9}]
""")

choice = int(input("next move, choose postion (1-9): "))
if choice == 1:
    p1 = "o"
elif choice == 2:
    p2 = "o"
elif choice == 3:
    p3 = "o"
elif choice == 4:
    p4 = "o"
elif choice == 5:
    p5 = "o"
elif choice == 6:
    p6 = "o"
elif choice == 7:
    p7 = "o"
elif choice == 8:
    p8 = "o"
elif choice == 9:
    p9 = "o"
else:
    "you entered something bad... program ending"

print(f"""
[{p1}][{p2}][{p3}]
[{p4}][{p5}][{p6}]
[{p7}][{p8}][{p9}]
""")

if p1 == "o" and p2 == "o" and p3 == "o":
    print("o wins, GAME OVER")

