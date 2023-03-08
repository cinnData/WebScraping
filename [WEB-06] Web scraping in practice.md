# [WEB-06] Web scraping in practice

## HTML and the browser

Suppose that your browser (let us assume that you use Google Chrome) is displaying a web page on the screen. Right-clicking anywhere on the page opens a contextual menu. Select the *View Page Source* option. A new tab will open, displaying a HTML document. In most pages, this HTML document corresponds to the page that the browser was displaying. These pages are the ones covered in this chapter.

But not all pages are that simple. Some use a technology called **AJAX** (Asynchronous JavaScript And XML) in two-step process as follows:

1. The page corresponding to the URL that you enter is loaded.

2. A JavaScript program creates a `XMLHttpRequest` object.

3. The `XMLHttpRequest` object sends a request to a web server.

4. The server sends a new HTML document back to the browser, which the browser displays on the screen. This second document corresponds to the page that you are actually seeing.

The tools provided by the Python package **Requests** can only capture the first page, which is not always the one from which you wish to scrape the information. To get the second one, web scrapers use a tool called **Selenium**, whose discussion we postpone to the next lecture.

Also in the contextual menu of the browser, the *Inspect* option can help you to identify an element of a web page. Right-clicking on a part of the page currently displayed by the browser and selecting this option, the screen is split, leaving the web page on one side and displaying on the other side the *Developer Tools* panel, which provides many choices: *Elements*, *Console*, *Network*, etc. The first one contains the page's DOM tree and gives you full access to the source code of the page currently displayed, which may be different from the one you called, as explained above. The element of the page on which you have clicked appears highlighted.

## The package Requests

In Python, files can be downloaded from Internet sources in multiple ways. Old tutorials suggest using the package `urllib`, which is part of the Python Standard Library. Nowadays, Requests, included in the Anaconda distribution, is the favorite choice of the practitioners.

Let us refresh the context. Through the browser, you can access to resources, specifying a **Uniform Resource Locator** (URL). At the beginning of the URL, we find the the protocol used to access the resource, followed by a colon and two forward slashes. This is usually HTTPS, a secure version of HTTP. 

The **Hypertext Transfer Protocol** (HTTP) was designed to enable communications between clients and servers. For instance, a client (such as your browser) sends a **HTTP request** to the server. Then, the server returns the response to the client. The response contains status information about the request and, if the request is accepted, the requested content.

**GET** is one of the most common HTTP methods. It is used to request data from a specified resource. The function `requests.get` is a Python implementation. You can manage this as follows:

```
import requests
html_str = requests.get(url).text
```

`requests.get` returns a `requests` object (type `requests.models.Response`), containing data about the request. The attribute `text` of this object is a string which, for an ordinary web page, is the HTML source code. Now you can parse this string with the function `BeautifulSoup` from the package `bs4`, and then extract the information you are interested by means of the methods `find` and `find_all`. This information, after cleaning, can be exported to your preferred data format. Let us see below how to export the data to a CSV file.

## Exporting to a CSV file

There are many ways to export the data scraped to a CSV file in Python. The classic approach is based on the package `csv`, included in the standard library. To use this package, write your data set as a list in which every item is a list which contains the data from a row of the data set. Put the column names as the first row. Let us call this list `data`.

First, you import the package:

```
import csv
```

The built-in function `open` creates a connection to an empty text file, assuming that the path makes sense in your computer. The mode can be `'r'` (read), `'w'`(write) or others. The argument `newline=''` is needed in Windows but not in Macintosh. If you omit it, a Windows computer will put extra blank lines between rows. If not specified, the encoding used by the new file is platform-dependent (meaning UTF-8 in Mac and various things in Windows, depending on your region). Assuming that you want to read again the data in Python, let us specify here `encoding='utf-8'`.

```
conn = open('fname.csv', mode='w', newline='', encoding='utf-8')
```

Next, we create a **CSV writer**. The default delimiter is the comma, but you can use `delimiter=';'` if you plan to open the CSV file with Excel and your Excel uses the semicolon as the column separator.  

```
writer = csv.writer(conn, delimiter=',')
```

The method `writerows` writes the rows in the file:

```
writer.writerows(data)
```

Finally, we close the connection:

```
conn.close()
```

Practitioners pack this as:

```
with open('fname.csv', mode='w', newline='', encoding='utf-8') as conn:
    writer = csv.writer(conn, delimiter=',')
    writer.writerows(data)
```

