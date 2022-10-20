# Tuples
# Tuples cannot be changed or modified but Lists can be modifed and changed in a new varaible
# You can have Tuples in a list array

from ast import Num


coordinates = (4, 5)

print(coordinates[0])

# Function

def say_hi(name, age):
    print("Hello " + name + age)

varname = "Steve, "
birth = 22
say_hi(varname, str(birth))
say_hi("Tony ", "35")

# Return Statement 
def cube(num):
    return num*num*num

result = cube(4)
print(result)

#If Statement
is_male = True
is_tall = False 

if is_male and is_tall:
    print("Tu Madre!")
elif is_male and not(is_tall):
    print("Aye!!")
else:
    print("Es mi familia")

#If Statement and Compar
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(30, 4, 5))

# Dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June"
}

print(monthConversions["Feb"])
print(monthConversions.get("Apr"))

#While Loop

i = 1
while i <=10:
    print(i)
    i += 1

print("Done with loop!")

#Exponent Function

def raise_to_power(base_num, pow_num):
    resulta = 1
    for index in range(pow_num):
        resulta = resulta * base_num
    return resulta

print(raise_to_power(3, 3))