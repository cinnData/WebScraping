# [WEB-01] What is web scraping?

## What is web scraping?

**Web scraping** is concerned with extracting data from websites, in particular data that would be difficult to get on a large scale using traditional data collection methods. There is a whole industry built around web scraping, as it is used to track product price changes or discounts, to gather data from social profiles, to capture real estate listings, in search engine optimization (SEO), etc.

Scraping a web page involves downloading the page and extracting data from it. Both things can be done in many ways, in particular with Python tools. There are also specialized web scraping software applications, such as **Octoparse**. This course uses the Python packages **Requests**, **Beautiful Soup** and **Selenium**.

## What is HTML?

**HTML** (Hypertext Markup Language) is the language in which are written the documents designed to be displayed in a web browser. The web browser receives HTML documents from a web server or from local storage and renders the documents as multimedia web pages.

HTML is assisted by two technologies:

* **CSS** (Cascading Style Sheets) is a language used to describe the style of HTML documents.

* **JavaScript** is a scripting language, that is, one for integrating and communicating with other languages. Scripting languages are used for small jobs. The source code of dynamic web pages contains JavaScript scripts to perform actions such as accepting cookies or asking for more information. 

An extremely simple example of a HTML document follows. It is easy to see, in this example, why HTML is called a **markup language**. The markup, consisting here of the tags `<head>`, `<body>`, `<title>`, `<div>` and `<a>`, is used for creating a structure in the document and for including **links** to web pages, pictures, etc.

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

Unfortunately, in a HTML document captured from Internet, you will not find such a friendly presentation, with one line for each tag, and indentation to help you see the structure of the document. But there are many tools for rendering HTML documents in this form.

## Tags and attributes

The structure of a HTML document is made by the tags. Every part of the document is opened by a **start tag** (`<tag>`) and closed by an **end tag** (`</tag>`). These parts are called **HTML elements**. The HTML document The tags create a tree-like structure in the document, with HTML elements nested within HTML elements. The representation of the HTML document as a logical tree is called the **Document Object Model** (DOM). 

*Note*. Though we may insert white space between consecutive elements, as I have done in the example below, to make the document readable, white space between tag belonging to different elements is ignored by the HTML interpreter.

The tag `<html>` tells the browser that this is a HTML document. The `html` element is the whole document. It has two **child elements**, `head` and `body`. A HTML document is always split in this way. In the example, the `head` element has one **child**, while the `body` element has three children, which are **siblings**.

Then, the `title` element contains the string `'Data Viz'`, enclosed between the start tag and the end tag (this can also be said of the `head` element). This string is referred to as **text**. Also, most of the start tags have **attributes**. In our example, the `div` elements have one `class` attribute, while the `a` element has two attributes, a `class` attribute and a `href` attribute. `class` attributes, which specify one or more `class` names for some elements of the HTML document, are very frequent. The value of a `class` attribute can be used by CSS and JavaScript to perform certain tasks for the elements with that `class` value.

The `a` tags have a special role, marking hyperlinks. A **hyperlink** is used to link a page to another page, or to download a file. The most important attribute of an `a` element is the `href` attribute, which indicates the link's destination. 

Tags with other names, such as `span`, `img`, `button` and `script`, which have their specific roles in a HTML document, will appear in the examples of this course, and will be discussed there.
