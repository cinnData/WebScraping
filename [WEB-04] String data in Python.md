# [WEB-04] String data in Python

## Strings

A **string** is a sequence of **characters**. This includes the (English) alphanumeric characters and also special characters like white space, punctuation, etc. Other symbols, like emoticons, can also appear in your data, specially in social networks data. Besides that, you can also find letters from other languages (Spanish, Portuguese, etc) or alphabets (Cyrillic, hiragana, etc), and even ideographs (such as Han characters).

There is a basic set of 127 characters, called the **ASCII characters**, which are encoded in the same way by all the computers, so you will never have trouble with them. They include the English letters (without accents), the numbers, basic punctuation (not curly quote marks or long dashes), white space, **control characters** such as the new line, represented in many computer languages (including Python) as `\n`, and other symbols familiar to you, such as the dollar (`$`) and the hash (`#`) symbols. The complete list can be easily found in Internet.

Non-ASCII characters can be encoded by different computers or different text editors in different ways. Mind that, if you capture string data on your own, you will probably find some of these characters in your data. Even when the documents are expected to be in English, they can be contaminated by other languages: Han characters, German dieresis, Spanish eñe, etc.

The preferred **encoding** is **UTF-8** (`utf-8`), which is the default encoding in Macintosh computers. Reading and writing text files in Pandas, the argument `encoding` allows you to manage both UTF-8 and the alternative encoding **Latin-1** (`latin1`). Windows computers use their own system, which is region specific. In US and Western Europe, this is **Windows-1252**, which is very close to Latin-1, though not exactly the same.

## Strings as sequences

In Python, strings and lists are two types of **sequences**, and some basic methods are common to both types. The following example will illustrate this.

```
In [1]: iese = 'IESE Business School'
```

First, the function `len` gives you the **number of characters** of a string:

```
In [2]: len(iese)
Out[2]: 20
```

Also, you can extract a **substring** from a string in the same way you extract a sublist from a list using a range of indexes:

```
In [3]: iese[5:]
Out[3]: 'Business School'
```

The plus sign (`+`) allows you to **concatenate strings**:

```
In [4]: iese[:4] + ', A way to learn'
Out[4]: 'IESE, A way to learn'
```

A difference between strings and lists is found in the use of `in`. For a list, it indicates that an object is among the elements of that list. For strings, that a string is contained in another string, as we see here:

```
In [5]: 'IE' in iese
Out[5]: True
```

## Python string methods

Besides the methods inherited from lists, Python has a collection of methods for manipulating strings. For instance, **conversion to lowercase**:

```
In [6]: iese.lower()
Out[6]: 'iese business school'
```

Conversion to uppercase is performed in a similar way. The typical *Find and Replace* method of text editors is implemented in Python by the method `replace`.

```
In [7]: iese.replace('IESE', 'Iese')
Out[7]: 'Iese Business School'
```

You can **split a string** with the method `split`. The split can be based on any **separator**. Two examples follow.

```
In [8]: iese.split(' ')
Out[8]: ['IESE', 'Business', 'School']
```

```
In [9]: iese.split('i')
Out[9]: ['IESE Bus', 'ness School']
```

If no separator is specified, any whitespace substring (containing only white space, line breaks or tabs) is a separator:

```
In [10]: iese.split()
Out[10]: ['IESE', 'Business', 'School']
```

The method `find` returns the lowest index in the string where a substring is found. With additional arguments `start` and `end`, the search can be restricted.

```
In [11]: iese.find('Business')
Out[11]: 5
```

`find` returns -1 if the substring is not found:

```
In [12]: iese.find('Negocios')
Out[12]: -1
```

Finally, the function `count` counts the number of occurrences of a substring within a string:

```
In [13]: iese.count('s')
Out[13]: 3
```

## Regular expressions

A **regular expression** is a pattern which describes multiple strings. Regular expressions can be used in many computer languages. In Python, the package `re`, which is part of the Python Standard Library, provides some functions which read an argument as a regular expression. Three useful `re` functions are `sub`, `split` and `findall`. It can be imported as:

```
In [14]: import re
```

Among regular expressions, **character classes** are the simplest case. They are built by enclosing a collection of characters in square brackets. The square brackets indicate *any* of the characters enclosed. For instance, `[0-9]` stands for any digit, `[a-z]` for any (ASCII) lowercase letter, and `[A-Z]` for any capital. 

The following example uses the `re` function `sub`, which works like `replace`, but admits a regular expression as the pattern to be replaced. Note that the string where the replacement is performed is entered as the third argument.

```
In [15]: re.sub('[a-z]', 'x', iese)
Out[15]: 'IESE Bxxxxxxx Sxxxxx'
```

Character classes get more powerful when complemented with **quantifiers**. For instance, followed by a plus sign (`+`), a character class indicates a sequence of any length. So, `[0-9]+` indicates any sequence of digits, in particular any number, and `[a-z]+` indicates any word in lower case. You can also specify the length of the sequence, as in `[A-Z]{2}`, or the minimum and maximum length, as in `[0-9]{1,3}`.

We see next the effect of introducing this quantifier in the preceding example.

```
In [16]: re.sub('[a-z]+', 'x', iese)
Out[16]: 'IESE Bx Sx'
```

The regular expressions `\w` and `\W`, which stand for any character that can be part of a word and the contrary, respectively, are very useful in practice. The following example uses `\W`, with a quantifier, to split by any sequence of white spaces and punctuation. 

```
In [17]: re.split('\W+', 'IESE: A way to learn, a mark to make')
Out[17]: ['IESE', 'A', 'way', 'to', 'learn', 'a', 'mark', 'to', 'make']
```

Properly speaking, the function `findall` is not a generalized version of a built-in Python function. It returns a list containing all the occurrences of a pattern. It can be used, as following example shows, to transform a string into a list of words.

```
In [18]: re.findall('\w+', iese)
Out[18]: ['IESE', 'Business', 'School']
```

In computer languages, a **wildcard** is a symbol which can match any single character (letter, digit, whitespace, etc). The wildcard of Python regular expressions is the dot (`.`). So, `.+` stands for *any* string. An example follows.

```
In [19]: re.sub(',.+', '', 'IESE: A way to learn, a mark to make')
Out[19]: 'IESE: A way to learn'
```

Some symbols, like `+`, `.` and `$` play special roles in regular expressions. You have to be careful when using them in a pattern in the first argument of one of these functions, because they can give unexpected results. The following example illustrates this.

```
In [20]: re.sub('$20', '$30', 'The price is $20')
Out[20]: 'The price is $20'
```

The solution is to write these characters with a **escape character** (`\`). Then, they are read literally:

```
In [21]: re.sub('\$20', '$30', 'The price is $20')
Out[21]: 'The price is $30'
```

## Homework

1. Write a function which anonymizes credit card numbers, turning, for instance, '2875765488882745' into 'Credit card ****745'. Write a short list containing credit card numbers and check that your function does the job.

2. VISA Electron card numbers have 16 digits. As in any credit card, the first digits identify the card issuer. In the case of VISA Electron, the **issuer identification number** (IIN) can be 4026, 417500, 4508, 4844, 4913 or 4917. Write a regular expression for VISA Electron card numbers.

3. You can see below a list containing the URL's for some **job postings** at the London-based financial technology company Wise. The sequence of digits in the middle of the URL make the ID of the position. Write a function which extracts a list of such URL's to a list containing their ID's.

```
['https://www.wise.jobs/role/3093508-design-director-onboarding-growth',
'https://www.wise.jobs/role/3234541-senior-implementation-manager',
'https://www.wise.jobs/role/3276007-senior-product-designer',
'https://www.wise.jobs/role/3350217-product-analyst-northam']
```
