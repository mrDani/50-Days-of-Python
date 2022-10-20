
"""
Question:
Using clearly written python Code with comments. 
A. Extract the colors from the html file provided ‘python_class_test.html’, using regular expression. 
B. Store them in a dictionary, using color as key and their frequency as values. 
"""
import re
from collections import Counter

html_file = open('python_class_test.html')

read_html = html_file.read()

colors_regex = re.findall(r'<td>(.+?)</td>', read_html)

days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
for day in days:
    colors_regex.remove(day)
colors_regex = [word.replace(' ','') for line in ab for word in line.split(',')]
colors_regex.remove('')

all_colors = dict(Counter(colors_regex))
html_file.close()
# OUTPUT
"""
all_colors

{'GREEN': 10,
 'YELLOW': 5,
 'BROWN': 6,
 'BLUE': 30,
 'PINK': 5,
 'ORANGE': 9,
 'CREAM': 2,
 'RED': 9,
 'WHITE': 16,
 'ARSH': 1,
 'BLEW': 1,
 'BLACK': 1}

"""

"""
1.) Which color of shirt is the mean color? 
"""
color = all_colors.values()
count = 0
for co in color:
    count += 1
sum_of_colors = sum(all_colors.values())
total_no_of_colors = count

mean = sum_of_colors/total_no_of_colors

# OUTPUT
"""
Mean = 7.916666666666667
"""


"""
2.) Which color is mostly worn throughout the week? 
"""
colour_worn_throughout = max(all_colors.values())

# OUTPUT
"""
colour_worn_throughout = 30
Therefore, the colour worn throughout is BLUE

"""

"""
3.) Which color is the median? 
"""
import statistics as stat
median_color = stat.median(all_colors.values())

# OUTPUT
"""
median_color = 5.5 or 6 approximately
"""

"""
4.) BONUS Get the variance of the colors 
"""
import numpy as np
color_variance = np.var(list(all_colors.values()))

# OUTPUT
"""
color_variance = 63.243055555555564
"""


"""
5 BONUS if a colour is chosen at random, what is the probability that the color is red? 
"""
probability_of_picking_red = all_colors['RED']/total_no_of_colors
# OUTPUT
"""
probability_of_picking_red = 0.75
"""
"""
6 Save the colours and their frequencies in postgresql database
"""
import psycopg2
conn = psycopg2.connect(host='localhost',port='5432',dbname='bincomdb',user='postgres',password='hunter2')
cursor = conn.cursor()
try:
    cursor.execute('''
     CREATE TABLE IF NOT EXISTS colors(
        GREEN INTEGER NOT NULL,
        YELLOW INTEGER NOT NULL,
        BROWN INTEGER NOT NULL,
        BLUE INTEGER NOT NULL,
        PINK INTEGER NOT NULL,
        ORANGE INTEGER NOT NULL,
        CREAM INTEGER NOT NULL,
        RED INTEGER NOT NULL,
        WHITE INTEGER NOT NULL,
        ARSH INTEGER NOT NULL,
        BLEW INTEGER NOT NULL,
        BLACK INTEGER NOT NULL
        );
        ''')
    cursor.execute('''INSERT INTO colors(GREEN, YELLOW, BROWN, BLUE, PINK, ORANGE, CREAM, RED, WHITE, ARSH, BLEW, BLACK) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
''',list(all_colors.values()))
except psycopg2.Error as e:
        print('Error found')
        print(e)
    
    
# """
# 7 .)  BONUS write a recursive searching algorithm to search for a number entered by user in a list of  numbers
# """
def list_games():
    created_list = [2,3,4,5,6,7,8]
    inp = int(input('Guess a number: '))
    if inp in created_list:
        print('Yes this number is in the list')
    else:
        print('Game over')

"""
8.) Write a program that generates random 4 digits number of 0s and 1s and convert the  generated number to base 10 

"""
zeros_ones = np.linspace(0,1,4)
answer = np.log10(zeros_ones)

# OUTPUT
"""
array([-inf, -0.47712125, -0.17609126,  0. ])
"""

"""
9. Write a program to sum the first 50 Fibonacci sequence 

"""
def fibonacci():
    """
    Fibonacci Rule is xn = xn-1 + xn-2
    """
    lst = [0,1]
    sizes = range(0, 48)
    for size in sizes:
        ans = lst[-1] + lst[-2]
        lst.append(ans)
    return lst

# OUTPUT
"""
fibonacci() returns a list which are:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

the sum of fibonacci is :- 20365011073

"""