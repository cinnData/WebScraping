## [WEB-02] Introduction to Python ##

# Typing Python code #
2 + 2
a = 2 + 2
a
A
b = 2 * 3
b - 1
b**2

# Python packages #
import math
math.sqrt(2)
from math import sqrt
sqrt(2)

# Data types #
type(2)
type(2.4)
type('Miguel')
type(True)

# Type conversions #
float(2)
int(2.3)
int('27')
float('27')
str(27)
1 + True
math.sqrt(False)

# Comparison operators #
5 < a
a == 4
a != 4
'a' > 'b'
'A' <= 'a'
3 == 3.0
0.7 < True

# Logical operators #
True and False
True or False
not True
5 < 7 and ' ' <= '6'

# Functions #
def f(x):
    y = 1/(1 - x**2)
    return y
f(2)
f(1)
f('Mary')
def g(x, y): return x*y/(x**2 + y**2)
g(1, 1)

# If statements #
if 3 < 5: print('Minor')
if 3 == 5: print('Equal')
else: print('Not equal')
if math.sqrt(1) < 1: print('Minor')
elif math.sqrt(1) == 1: print('Equal')
else: print('Major')

# While loops #
x = 1
while x**2 <= 1000: x = x + 1
x
x = 1
while x > 0: x = x + 1
x
