# Python program to read
# json file

import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
	print(i)

# Closing file
f.close()

# Python program to read
# json file


# JSON string
a = '{"name": "Bob", "languages": "English"}'

# deserializes into dict
# and returns dict.
y = json.loads(a)

print("JSON string = ", y)
print()


# JSON file
f = open ('data.json', "r")

# Reading from file
data = json.loads(f.read())

# Iterating through the json
# list
for i in data['emp_details']:
	print(i)

# Closing file
f.close()

# Python program to demonstrate
# Creation of Set in Python



# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)

# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)
