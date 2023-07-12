## [WEB-03] Python data containers ##

# Lists #
mylist = ['Messi', 'Cristiano', 'Neymar', 'Haaland']
len(mylist)
len([])
newlist = mylist + [2, 3]
newlist
len(newlist)

# Extracting items from a list #
mylist[0]
mylist[-1]
mylist[0:2]
mylist[2:]
mylist[:3]
mylist[0::2]
mylist[::-1]

# Membership operators #
yourlist = [4, 7] 
2 in yourlist
2 not in yourlist

# Ranges #
myrange = range(0, 10, 2)
list(myrange)
list(range(5, 12))
list(range(10))

# For loops #
for i in range(3): print('Hello world!')
squares = []
for i in range(1, 5):
    squares = squares + [i**2]
squares

# List comprehensions #
[i**2 for i in range(1, 5)]
[i**2 for i in range(1, 21) if i % 3 != 0]
