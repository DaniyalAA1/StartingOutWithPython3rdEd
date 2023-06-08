from datetime import date
# for i in range(3,10):
#     print(f"""\telif choice == {i}:
# \t\tp{i} = \"x\"""")
    

title = "Something else"
name = "Daniyal A"
description = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet quasi neque autem! Autem similique consequatur perferendis perspiciatis dolore dolorum repellat neque incidunt optio impedit laboriosam illum, quod accusantium itaque atque! "
"55/55/5555"

def centerText(txt):
    COUNT = 80
    stringLength = len(txt)
    space = (COUNT - stringLength)//2
    return space*" " + txt

def headerTemplate(title, name, desc):
    # todayDate = date.today()
    return f"""=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
{centerText(title)}`
Author: {name}
Description: {desc}

Date: {date.today()}
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*==*=*=*=*=*=*=*"""

print(headerTemplate("square numbers", "Daniyal", "a programm that demonstrates how to calculate the square root of a number"))