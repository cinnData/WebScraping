# [WEB-03] Python data containers

## Lists

Python has many **data container** types. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets. A list can contain items of different type, although this is not frequent. A simple example of a list, of **length** 4, is:

```
In [1]: mylist = ['Messi', 'Cristiano', 'Neymar', 'Haaland']
```

The function `len` returns the length of the list, that is, the number of items contained:

```
In [2]: len(mylist)
Out[2]: 4
```

Empty data containers play a role in Python programming. In particular, the **empty list** `[]`  will appear in the examples of this course. It has zero length:

```
In [3]: len([])
Out[3]: 0
```

Lists can be concatenated in a very simple way in Python:

```
In [4]: newlist = mylist + [2, 3]
   ...: newlist
Out[4]: ['Messi', 'Cristiano', 'Neymar', 'Haaland', 2, 3]
```

Now, the length of `newlist` is 6:

```
In [5]: len(newlist)
Out[5]: 6
```

## Extracting items from a list

Every item of a list has an **index**. The first item has index 0, the second item has index 1, and so on. An item can be extracted from the list by indicating its index between square brackets. For instance, to extract the first item:

```
In [6]: mylist[0]
Out[6]: 'Messi'
```

The second item is extracted as `mylist[1]`, the third one as `mylist[2]`, etc. Negative indexes mean that we start counting backwards from the end. In particular, the last item can be extracted as `mylist[-1]`:

```
In [7]: mylist[-1]
Out[7]: 'Haaland'
```

Sublists can be extracted with a range of indexes, as in:

```
In [8]: mylist[0:2]
Out[8]: ['Messi', 'Cristiano']
```

Note that `0:2` includes `0` but not `2`. This is a general rule of indexing in Python, the left limit is included but the right limit is not. Other examples:

```
In [9]: mylist[2:]
Out[9]: ['Neymar', 'Haaland']
```

```
In [10]: mylist[:3]
Out[10]: ['Messi', 'Cristiano', 'Neymar']
```

If a third index is specified, it stands for the **step**:

```
In [11]: mylist[0::2]
Out[11]: ['Messi', 'Neymar']
```

In particular, we can reverse a list with a step `-1`:

```
In [12]: mylist[::-1]
Out[12]: ['Haaland', 'Neymar', 'Cristiano', 'Messi']
```

## Membership operators

The **membership operators** `in` and `not in` can be used to check whether an object is contained in a list. Examples:

```
In [13]: yourlist = [4, 7]
    ...: 2 in yourlist
Out[13]: False
```

```
In [14]: 2 not in yourlist
Out[14]: True
```

## Ranges

A **range** is like a sequence of integers, but the terms of the sequence are not saved as in a list. Instead, only the procedure to create the sequence is saved. The syntax is `myrange = range(start, end, step)`. Example:

```
In [15]: myrange = range(0, 10, 2)
    ...: list(myrange)
Out[15]: [0, 2, 4, 6, 8]
```

Note that the items from a range cannot printed directly. So, I have converted the range to a list here with the function `list`. If, in the specification of a range, the step is omitted, it is assumed to be 1:

```
In [16]: list(range(5, 12))
Out[16]: [5, 6, 7, 8, 9, 10, 11]
```

If the start is also omitted, it is assumed to be 0:

```
In [17]: list(range(10))
Out[17]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## For loops

As `while` loops, `for` loops are used to control the repeated execution of a code chunk. But, instead of repeating an action while a condition holds, in the `for` loop the number of repetitions is fixed. The process is controlled by extracting items from a data container, such as a list or a range. A typical syntax would be 

```
for i in list: action
```

An example:

```
In [18]: for i in range(3): print('Hello world!')
Hello world!
Hello world!
Hello world!
```

If the action is specified in one or several separate lines, these have to be indented. Frequently, every execution involves extracting an item from a data container and using it in calculation. A trivial example:

```
In [19]: squares = []
    ...: for i in range(1, 5):
    ...:     squares = squares + [i**2]
    ...: squares
Out[19]: [1, 4, 9, 16]
```

## List comprehensions

When the purpose of the `for` loop is to transform a list into another list by means of an expression, you can pack everything in a single formula with a **list comprehension**. For instance, you can create the list of squares in a one shot with:

```
In [20]: [i**2 for i in range(1, 5)]
Out[20]: [1, 4, 9, 16]
```

If you wish to filter out some items from the original list, you can do it with an `if` expression. For instance, suppose that you wish to get a list with the squares of the numbers which are not divisible by 3, up to 20. Taking advantage of the operator `%`, which returns the remainder of the division of two integers, you can use:

```{r eval=FALSE}
In [21]: [i**2 for i in range(1, 21) if i % 3 != 0]
Out[21]: [1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361, 400]
```

## Other data container types

This course only uses lists and ranges, though Python provides other built-in types of data containers. A **tuple** is like a list, but represented with parentheses instead of square brackets:

```
mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')`
```

A **dictionary** is a set of pairs **key/value**. For instance, the following dictionary contains three features of an individual:

```
mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}`
```

## Homework

1. A **nested list** is a list of lists, that is, a list whose items are lists. For instance, `[[1, 2], [], ['a']]`. Write a function which *flattens* a nested list, transforming it into a new list whose items are the items contained in the items of the original list. Given the above example, that function would return `[1, 2, 'a']`.

2. The **Fibonacci numbers** are 1, 1, 2, 3, 5, 8, 13, 21, etc. Except for the first two terms of this sequence, both equal to 1, every term is the sum of the two preceding terms. Use a loop to calculate the first 10 Fibonacci numbers. Based on that loop, write a function which, given a number, returns a list of Fibonacci numbers of that length.
