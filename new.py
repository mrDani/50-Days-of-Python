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
else:
    print("Es mi familia")

