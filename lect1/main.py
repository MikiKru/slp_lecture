# Cheetsheet
# CTRL + /              - comment
# CTRL + SHIFT + F10    - run
# CTRL + D              - duplicate line

# signature -> name
# value -> 'Michael'
# = -> assign
name = 'Michael'
last_name = "Kruczkowski"
height = 185
salary_net = 12000.45

print("Name = " + name)
print("Salary = " + str(salary_net) + " PLN")
print("Salary = ", salary_net, "PLN")
# CSV - comma separated value
print(name, last_name, height, salary_net, sep=";")
del(name)       # name is removed
# print(name, last_name, height, salary_net, sep=";")

# check data types
print(type(last_name))
print(type(salary_net))
print(type(height))

decision = True
print(type(decision))

# real = 10
# img = -5
complex_number1 = 10 + (-5j)
complex_number2 = complex(10, -5)
print(complex_number1, type(complex_number1))
print(complex_number2, type(complex_number2))

introduction1W = "I'm Michael"
introduction2W = "I\'m Michael, this is my favourite qute\t \"xxx\""
introduction3W = "\\pbs.edu.pl\\index"
print(introduction1W)
print(introduction2W)
print(introduction3W)

example_object_1 = "1 day"

# if_1 = "...";

print(10 % 3)
print(9 % 2 == 0)

# comparison
print(1 >= 4)
print("Mike" > "Michael")
# print("Mike" == "Michael")
# index 0 -> M M
# index 1 -> i i
# index 2 -> k c
print(10 == 1+3*5 )

input_value = 'T'

print(input_value == 'q' or input_value == 'Q')
print(input_value.upper() == 'Q')

# input data from user
name_usr = input("What's your name?")
try:
    number_usr = int(input("What's your favourite number?"))
    print(name_usr, type(name_usr))
    print(number_usr, type(number_usr))
    print(number_usr % 2 == 0)
except:
    print("Your choice is not a number!!!")




