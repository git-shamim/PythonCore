# < is left aligned
# and 3/4 is character width
for i in range(1, 13):
    print("No. {} squared is {:<3} and cubed is {:<4}".format(i, i ** 2, i ** 3))


name = input("Please enter your name: ")
age = int(input("How old are you, {}?".format(name)))
print("{} is {} years old".format(name, age))


age = int(input("Your age: "))
if age >= 18:
    print("you are eligible to vote")
    print("Please put an x in the box")
else:
    print("You can vote after {} years".format(18 - age))
# ============================
if age < 18:
    print("You can vote after {} years".format(18 - age))
else:
    print("you are eligible to vote")
    print("Please put an x in the box")




