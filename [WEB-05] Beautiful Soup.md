# [WEB-05] Beautiful Soup

## What is Beautiful Soup?

**Beautiful Soup** is a Python package for extracting data from HTML files. Other packages, like **scrapy**, provide more powerful toolkits, but, since Beautiful Soup is much friendlier, most **web scraping** practitioners start there and do not leave Beautiful Soup unless their projects get really complex.

You can install Beautiful Soup by entering in the shell (or the console) `pip install bs4`. When the package is already installed, the recommended import style is:

```
In [1]: from bs4 import BeautifulSoup
```

This allows us to use the function `BeautifulSoup`, which can be applied to any string containing HTML code. `BeautifulSoup` **parses** the HTML code, learning the tree structure encoded there, which is then stored in a **soup object**. Let us see how this works in a supersimple example. 

## A toy HTML example

An extremely simple example of a **HTML document** follows. 

```
<html>
<head>
  <title>Data Viz</title>
</head>
<body>
  <div class="course">Data Visualization</div>
  <div class="program">MBA full-time</div>
  <a class="professor" href="faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a>
</body>
</html>
```

We create a string variable, whose value is the HTML document. Note that the end of the line is marked with the backslash (`\`).

```
In [2]: html_str = '<html>\
   ...: <head>\
   ...:   <title>Data Viz</title>\
   ...: </head>\
   ...: <body>\
   ...:   <div class="course">Data Visualization</div>\
   ...:   <div class="program">MBA full-time</div>\
   ...:   <a class="professor" href="faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a>\
   ...: </body>\
   ...: </html>'
```
This is stored as:

```
In [2]: html_str
Out[2]: '<html><head>  <title>Data Viz</title></head><body>  <div class="course">Data Visualization</div>  <div class="program">MBA full-time</div>  <a class="professor" href="faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a></body></html>'
```

## Parsing HTML code

To parse the string `html_str`, learning the tree structure, we enter:

```
In [4]: soup = BeautifulSoup(html_str, 'html.parser')
```

`BeautifulSoup` returns a soup object, which stores the contents of `html_str` in a way that the different HTML elements, called here **tags**, can be extracted. To get this, it uses a **parser**, which is a program which breaks the string into substrings based on the tags. 

Beautiful Soup does not come with a parser. It uses the one that it prefers among those available in your computer. If `'html.parser'` is specified, the choice is the parser provided by the Python Standard Library, so you do not need any additional package. Since this is a rather technical issue, Iwe follow here the recommended practice. 

The object `soup` has a special type:

```
In [5]: type(soup)
Out[5]: bs4.BeautifulSoup
```

The contents of `soup` can be displayed (don't do this for the source of a real web page, which will be too big to be read on the screen):

```
In [6]: soup
Out[6]: <html> <head> <title>Data Viz</title> </head> <body> <div class="course">Data Visualization</div> <div class="program">MBA full-time</div> <a class="professor" href="https://www.iese.edu/faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a> </body> </html>
```

The same is true por the elements contained in `soup`, as we will see below. But we have to see first how to extract this elements from the soup.

## The tree structure

Once you have a soup, you can easily explore the the content. For instance:

```
In [7]: soup.head
Out[7]: <head> <title>Data Viz</title> </head>
```

```
In [8]: type(soup.head)
Out[8]: bs4.element.Tag
```

Though, formally, `BeautifulSoup` and `Tag` are different types, a tag works in practice as a smaller soup, so you can extract elements within elements:

```
In [9]: soup.head.title
Out[9]: <title>Data Viz</title>
```

If you ask for a nonexisting element, you get `None`:

```
In [10]: soup.head.div
```

When there are several elements satisfying the requirements, you get the first one. This is the logic of Beautiful Soup:

```
In [11]: soup.div
Out[11]: <div class="course">Data Visualization</div>
```

HTML elements are called **tags** in Beautiful Soup. The simplest way to extract tags from the soup is based on the methods `find` and `find_all`. The method `find_all` returns a list containing all the tags that satisfy a specification (eventually empty), while `find` returns only the first one (or `None`, if there is no tag satisfying it). Let us see how to use in this method in our example.

## The method find

A first example of `find` follows.
 
```
In [12]: soup.find('div')
Out[12]: <div class="course">Data Visualization</div>
```

Note that there are two `div` tags in this soup, and `find` has extracted the first one. But we can use the attribute values to distinguish among tags with the same name:

```
In [13]: soup.find('div', attrs={'class': 'course'})
Out[13]: <div class="course">Data Visualization</div>
```

For the attribute `class`, this is can be shortened, as in: 

```
In [14]: soup.find('div', 'program')
Out[14]: <div class="program">MBA full-time</div>
```

Since a tag works as a smaller soup, you can iterate the method `find`:

```
In [15]: soup.find('head').find('title')
Out[15]: <title>Data Viz</title>
```

## The method find_all

The method `find_all` uses the same syntax as `find` but, instead of a single tag, it returns a list with all the tags that satisfy the specification:

```
In [16]: soup.find_all('div')
Out[16]: 
[<div class="course">Data Visualization</div>,
 <div class="program">MBA full-time</div>]
```

Note that `find_all` *always* returns a list. The list can be empty (`find` would return `None` in that case) 

```
In [17]: soup.find('head').find_all('div')
Out[17]: []
```

When there is only one tag in the list, that tag is precisely the one returned by `find`:

```
In [18]: soup.find_all('div', 'course')
Out[18]: [<div class="course">Data Visualization</div>]
```

Note that, even when there is exactly one tag in the list returned by `find_all`, you have to extract it from the list:

```
In [19]: soup.find_all('div', 'course')[0]
Out[19]: <div class="course">Data Visualization</div>
```

## Extracting information from the tags

The information we wish to extract from a HTML element can come as the text between the start tag and the end tag, or as the value of an attribute. The method `text` extracts all the text between the tags (including children tags, if there are):

```
In [20]: soup.find('a').text
Out[20]: 'Miguel Ángel Canela'
```

Note that this method cannot be applied directly to a list returned by `find_all`: 

```
In [21]: soup.find_all('div').text
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_54134/3644496290.py in <module>
----> 1 soup.find_all('div').text

/opt/anaconda3/lib/python3.9/site-packages/bs4/element.py in __getattr__(self, key)
   2251     def __getattr__(self, key):
   2252         """Raise a helpful exception to explain a common code fix."""
-> 2253         raise AttributeError(
   2254             "ResultSet object has no attribute '%s'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?" % key
   2255         )

AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
```

But we can use a comprehension list to extract the text from every item of the list and store it in a new list:

```
In [22]: [t.text for t in soup.find_all('div')]
Out[22]: ['Data Visualization', 'MBA full-time']
```

In certain cases, we are interested in the value of an attribute. A frequent example is that of an `a` tag whose
attribute `href` contains a relevant link. The link is then extracted as:

```
In [23]: soup.find('a')['href']
Out[23]: 'faculty-research/faculty/miguel-angel-canela'
```

## Finding the elements containing a string

In `find_all`, the argument `text` allows searching elements by the text enclosed:

```
In [24]: soup.find_all('div', text='Data Visualization')
Out[24]: [<div class="course">Data Visualization</div>]
```

The search string can be a **regular expression** instead of a fixed string, which gives us extra power. Note that the text value must be set as `re.compile(expr)`. For instance, to find the elements whose text contains the substring 'Data', we can use: 

```
In [25]: import re
    ...: soup.find_all('div', text=re.compile('Data'))
Out[25]: [<div class="course">Data Visualization</div>]
```

This approach can also be used to shorten the `class` value:

```
In [26]: soup.find_all('div', re.compile('co'))
Out[26]: [<div class="course">Data Visualization</div>]
```
