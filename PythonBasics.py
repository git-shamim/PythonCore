
# input function
greetings = "Hello"
name = input("Please enter your name : ")
print(greetings + " " + name)

# new line
splitString = "This string has been \nsplit over\nseveral \nlines"
print(splitString)

anothersplitstring = """This string has been
split over
several
lines"""
print(anothersplitstring)

# join lines
jointline = """This string over \
several lines \
have been joined \
using backslash"""
print(jointline)

# tab
tabbedStrings = "1\t2\t3\t4\t5"
print(tabbedStrings)

# apostrophe
print("The shop owner said \"he's resting, he's cold \" .")
print(""""The shop owner said "he's resting, he's cold" .""")

# print("C\Users\tim\notes.txt")
print(r"C\Users\tim\notes.txt")
print("C\\Users\\tim\\notes.txt")

a = 4
b = 15
print(b/a)     # float division or normal division
print(b//a)    # integer division (round number)
# Note : for range, integer is required; float does not work in range

# separators
number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

# replacement field
age = 24
print("My age is " + str(age) + " years")
print("My age is {} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# adding width to the replacement values (no. of characters)
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# left aligned replacement values
# < is left aligned
# > is right aligned
# ^ centered
for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
for i in range(1, 13):
    print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

# r:w:p  r is replacement field, w is width of the replacement field, p is precision or number of floating points
print("pi is approximately {0:12}".format(22/7))

