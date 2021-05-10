# < is left aligned
# and 3/4 is character width

for i in range(1, 13):
    print("No. {} squared is {:<3} and cubed is {:<4}".format(i, i ** 2, i ** 3))

name = input("Please enter your name: ")
age = int(input("How old are you, {}?".format(name)))
print("{} is {} years old".format(name, age))

