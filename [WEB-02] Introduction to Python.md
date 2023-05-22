# [WEB-02] Introduction to Python

## What is Python?

**Python** is a programming language, introduced in 1991. The current version is Python 3.11. To work with Python, you will pick an interface to a Python interpreter among the many available choices. You can have several instances of the interpreter, called **kernels**, running independently in your computer.

## The Anaconda distribution

There are many distributions of Python. In the data science community, **Anaconda** (`anaconda.com`) is the favorite one. The current Anaconda distribution comes with Python 3.9. Downloading and installing Anaconda will leave you with the `Anaconda Navigator`, which opens in the browser and allows you to choose among different interfaces to Python.

Among the many interfaces offered by Anaconda, I recommend you **Jupyter Qt Console**, which is an input/output text interface. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. Qt Console is the result of adding a graphical interface (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, with a toolkit called Qt.

Part of the popularity of the IPython shell was due to the **magic commands**, which were extra commands written as `%cmd. For instance, `%cd allowed you to change the **working directory**. These commands are not part of Python. Some textbooks and tutorials are still very keen on magic commands, which are occasionally mentioned in this course. To get more information about them, enter `%quickref` in the console. Although, in practice, you can omit the percentage sign (so `%cd` works exactly the same as cd), it is always safer to keep using it to distinguish the magic commands, which are NOT Python, from the Python code.

Jupyter provides an alternative approach, based on the **notebook** concept. In a notebook, you can combine input, output and ordinary text. In the notebook arena, **Jupyter Notebook** is the leading choice. Notebooks are multilingual, that is, they can be used with other languages, like R, besides Python. Most data scientists prefer the console for developing their code, but use notebooks for diffusion, specially for posting their work on platforms like GitHub.

Besides the Jupyter tools, Anaconda also offers a Python IDE (Integrated Development Environment) called **Spyder**, where you can manage a console and a text editor for your code. If you have previous experience with this type of interface, for instance from working with R in RStudio, you may prefer Spyder to Qt Console.

Alternatively, you can bypass the navigator calling those interfaces in a shell application. To start Qt Console, enter `jupyter qtconsole`. To get access to the notebooks in the default browser, enter `jupyter notebook`. To start Spyder, enter `spyder`.

*Note*. Use *Terminal* in Mac and *Anaconda Prompt* in Windows. Don't use the standard Windows prompt, because it will not find the Anaconda apps unless you specify the path.

## Typing Python code

Let me assume that you are using Jupyter Qt Console, though almost everything would be also valid in other interfaces, with minor adjustments. When you start the console, it opens a window where you can type or paste your code. You can resize the window and zoom inside it as in a browser (*e.g*. Google Chrome).

As the browser, the console can have several tabs working independently. To open a new tab, enter either *Cmd+T* (Macintosh) or *Ctrl+T* (Windows), or use the menu *File >> New tab with New Kernel*. Each of these tabs is an interface between you and a Python kernel. These kernels run independently.

The console produces input prompts (such as `In[1]:`), where you can type a command and press *Return*. Then Python returns either an output (preceded by `Out[1]:`, a (typically long and difficult) error message, or no answer at all. Here is a supersimple example:

```
In [1]: 2 + 2
Out[1]: 4
```

So, if you enter `2 + 2`, the output will be the result of this calculation. But, if you want to store this result for later use (in the same session), you will enter it with a name, as follows:

```
In [2]: a = 2 + 2
```

In Pyhton, when you use a name that is already taken, the old assignment is forgotten. Note that the value of 2 + 2 is not shown now. If you want to see it, you have to ask for that explicitly:

```
In [3]: a
Out[3]: 4
```

The extra white space between the symbols is ignored by Python, but improves readability. So, it is recommended to allow the mathematical expressions to "breath". Also, note that Python is **case sensitive**:

```{r eval=FALSE}
In [4]: A
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/378453753.py in <module>
----> 1 A

NameError: name 'A' is not defined
```

You can input several lines of code at once, by copypasting them from a text editor, or by pressing *Ctrl+Return* after every line. In that case, you will only get the output for the last line. If the cursor is not at the end of the last line, you have to press *Shift+Return* to get the output. Here is a simple example:

```
In [5]: b = 2 * 3
   ...: b - 1
   ...: b**2
Out[5]: 36
```

*Note*. You would probably have written `b^2` for the square of 2, but the caret symbol plays a different role in Python.

## Python packages

Many additional resources have been added to Python in the form of **modules**. A module is just a text file containing Python code. Modules are grouped in libraries, also called **packages**, because their elements are packed according to some specific rules which allow you to install and call them together. Python can be extended by more than 300,000 packages. Some big packages, like scikit-learn, are not single modules, but collections of modules, which are then called subpackages.

Since the basic Python toolkit (without any package) is quite limited, you will need additional resources for practically everything. For instance, suppose that you want to do some math, and calculate the square root of 2. You will then **import** the package math, whose resources include the square root and many other mathematical functions. 

```
In [6]: import math
```

Once the package has been imported, all its functions are available. You can then apply the function `math.sqrt`. This notation indicates that `sqrt` is a function of the module `math`. In the console, the square root calculation shows up as:

```
In [7]: math.sqrt(2)
Out[7]: 1.4142135623730951
```

Alternatively, you can import only the functions that you plan to use:

```
In [8]: from math import sqrt
   ...: sqrt(2)
Out[8]: 1.4142135623730951
```

We will use both ways in this course, following always the recommended import style. Packages are imported just for the current kernel. You finish the session by either closing the console or by restarting the kernel. You can do this with *Kernel >> Restart current Kernel* or by typing *Ctrl+.*.

With Anaconda, most packages used in this course are already available and can be directly imported. If it is not the case, you have to **install** the package (only once). There is a basic installation procedure in Python, which uses a package installer called `pip` (see `pypi.org/project/pip`). Using pip you can have a conflict of versions between packages which are related. If this is the case, ayou can use an alternative installer called `conda`, which checks your Anaconda distribution, taking care of the conflicts. Mind that, due to all those checks, `conda` is much slower than `pip`.

## Data types

As in other languages, data can have different **data types** in Python. The data type can be learned with the function `type`. Let us start with the numeric types. First, the **integers** have type `int`:

```
In [9]: type(2)
Out[9]: int
```

Another numeric type is that of **floating-point** numbers (`float`):

```
In [10]: type(2.4)
Out[10]: float
```

Note that, in Python, integers are not, as in the mathematics textbook, a subset of the real numbers, but a different type. Besides numbers, we can also manage **strings** with type `str`:

```
In [11]: type('Miguel')
Out[11]: str
```

Strings are always enclosed by quote marks, either single or double (but same way on both sides). We also have **Boolean** (`bool`) data, which are either `True` or `False`:

```
In [12]: type(True)
Out[12]: bool
```

Mind that it is `True` and `False` in Python, not `TRUE` and `FALSE`, or `true` and `false`, as in other languages. Remember: Python is case sensitive.

## Type conversions

The functions `int` and `float` can be used to convert numbers from one type to another type (sometimes at a loss):

```
In [13]: float(2)
Out[13]: 2.0
```

```
In [14]: int(2.3)
Out[14]: 2
```

Sometimes, you can convert numbers to strings and conversely:

```
In [15]: int('27')
Out[15]: 27
```

```
In [16]: float('27')
Out[16]: 27.0
```

```
In [17]: str(27)
Out[17]: '27'
```

Boolean variables can be converted to `int` and `float` type with the functions mentioned above, but also by means of a mathematical operator:

```
In [18]: 1 + True
Out[18]: 2
```

```
In [19]: math.sqrt(False)
Out[19]: 0.0
```

## Comparison operators

Let me show how the **comparison operators** work in Python. For sure, you know the *lower than* symbol:

```
In [20]: 5 < a
Out[20]: False
```

When you input an expression involving a comparison operator, Python evaluates it, returning either `True` or `False`. The following example uses the **equality operator**, which is denoted in Python by a double equal sign:

```
In [21]: a == 4
Out[21]: True
```

Why two equal signs? The reason is that a single equal sign is used to assign names. So `a = 4` is interpreted, not as asking whether `a` is equal to `4`, but as creating a variable named `a` whose value is `4`. The *not equal* operator is denoted by an equal sign preceded by an admiration symbol (`!`):

```
In [22]: a != 4
Out[22]: False
```

Other examples involving comparison operators:

```
In [23]: 'a' > 'b'
Out[23]: False
```

```
In [24]: 'A' <= 'a'
Out[24]: True
```

Numbers and booleans can be compared irrespective of their types:

```
In [25]: 3 == 3.0
Out[25]: True
````

```
In [26]: 0.7 < True
Out[26]: True
```

## Logical operators

The **logical operators** allow operations between booleans. They are `and`, `or` a `not`. They work in the same way as in other languages: (a) `x and y` is true when both `x` and `y` are true, (b) `x or y` is true when at least one of them is true, and (c) `not x` is true when `x` is false. Examples:

```
In [27]: True and False
Out[27]: False
```

```
In [28]: True or False
Out[28]: True
```

```
In [29]: not True
Out[29]: False
```

Since expressions involving comparison operators are evaluated and turned into either `True` or `False`, we can combine them with logical operators. Example:

```
In [30]: 5 < 7 and ' ' <= '6'
Out[30]: True
```

## Functions

A **function** takes a collection of **arguments** and performs an action. The functions that appear in this course will **return** a value and, sometimes, **print** a message. Besides the built-in functions like `type` and those coming in the packages that you may import, you can define your own functions. The definition will be forgotten when the session is closed, so you have to include it in your code.

A simple example of a user-defined function follows. Note the indentation after the colon, which is created automatically by the Jupyter interface (either console or notebook).

```
In [31]: def f(x):
    ...:     y = 1/(1 - x**2)
    ...:     return y
```

When you define a function, Python just takes note of the definition, accepting it when it is syntactically correct (parentheses, commas, etc). The function can be applied later to different arguments (during the same session).

```
In [32]: f(2)
Out[32]: -0.3333333333333333
```

If you apply the function to an argument for which it does not make sense, Python will return an error message which depends on the values supplied for the argument.

```
In [33]: f(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/1567560659.py in <module>
----> 1 f(1)

/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/1722558193.py in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return y

ZeroDivisionError: division by zero
```

```
In [34]: f('Mary')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/2381081837.py in <module>
----> 1 f('Mary')

/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/1722558193.py in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return y

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

Functions can have more than one argument, as in:

```
In [35]: def g(x, y): return x*y/(x**2 + y**2)
````

```
In [36]: g(1, 1)
Out[36]: 0.5
```

Note that, in the definition of `g`, I have used a shorter way. Many programmers would prefer to make it longer, with more than one line, as I did previously for `f`.

## If statements

**Conditional logic**, operationalized through **if-then-else** commands, is ubiquitous in programming. You also have this in Python. The shortest version has the following syntax:

```
if condition: action
```

A simple example follows.

```
In [37]: if 3 < 5: print('Minor')
Minor
```

When the action is specified in a different line (or lines), that line has to be indented, as in a `def` statement. A longer version with two possible actions:

```
if condition: action1
else: action2
```

An example:

```
In [38]: if 3 == 5: print('Equal')
    ...: else: print('Not equal')
Not equal
```

This looks like Excel, right? The Excel version would be `IF(condition, action1, action2)`. An even longer version includes an `elif` (else if) clause:

```
if condition1: action1
elif condition2: action2
else: action3
```

You can add as many `elif` clauses as needed. Example:

```
In [39]: if math.sqrt(1) < 1: print('Minor')
    ...: elif math.sqrt(1) == 1: print('Equal')
    ...: else: print('Major')
Equal
```

## While loops

**Loops** are used in practically all programming languages. So, you are already familiar with them if you have programming experience. With loops, you avoid repeating code chunks. In particular, a `while` loop executes a code chunk until a stopping condition is met. The syntax is:

`while condition: action`

Again, if the action is specified in separate lines, these have to be indented. A simple example follows. Suppose that you wish to find the first integer whose square is higher than 1,000. You start with:

```
In [40]: x = 1
```

Then, you increase `x` until `x**2` exceeds the threshold value:

```
In [41]: while x**2 <= 1000: x = x + 1
```

Indeed, you got 32, whose square is 1,024:

```
In [42]: x
Out[42]: 32
```

What if the condition is never met? Then, the loop will go on until you interrupt the process (*Ctrl+C*) or restart the kernel (*Ctrl+.*). An example follows, in which I have allowed the process to run for a few seconds:

```
In [43]: x = 1
    ...: while x > 0: x = x + 1
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/2854391691.py in <module>
      1 x = 1
----> 2 while x > 0: x = x + 1

KeyboardInterrupt: 
````

```
In [44]: x
Out[44]: 277583313
```

## Homework

1. Write a Python function which, given three integers, returns `True` if any of them is zero, and `False` otherwise.

2. Write a Python function which, given three integers, returns `True` if they are in order from smallest to largest, and `False` otherwise. Modify your function so that it returns `1`/`0` instead of `True`/`False`.

3. Given two positive integers `a` and `b`, you can get the remainder of the integer division of `a` by `b` with `a%b`. So `7%3` returns `1`, and `9%5` returns `4`. Write a function which, given an integer, prints 'Yes, it is a multiple of 3' if that integer is a multiple of 3, and 'Bad luck!' otherwise.

4. Calculate the square root of 2 and take the square of it. Do you get 2? Why?

5. Evaluate the expressions `1/3 + 1/3 + 1/3 + 1/3 == 4/3` and `1/3 + 1/3 + 1/3 + 1/3 + 1/3 == 5/3`. One is true and the other one is false. Is Python crazy?
