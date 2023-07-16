# [WEB-07] Selenium

## Selenium 

**Selenium** is an open source project for a range of tools for browser automation. It has several components, each taking on a specific role in aiding the development of web application test automation. At the core of Selenium is **Selenium WebDriver**, an interface to write instructions that work interchangeably across browsers. Selenium WebDriver accepts commands and sends them to a browser. This is implemented through a browser-specific **browser driver**, which sends commands to a browser and retrieves results. Most browser drivers actually launch and access a browser application such as Google Chrome or Firefox.

The browser driver provides an interface to the chosen browser. It has to be installed in your computer for the Python package Selenium to work. This lecture only covers Chrome, whose driver is **chromedriver** (`chromedriver.chromium.org/downloads`). Firefox has a similar driver called **geckodriver**. 

You will have to check a few things in your computer to get everything ready:

* The versions of Google Chrome and chromedriver have to match. If you update the browser before downloading the chromedriver binary, you can select the last version most recent version of the driver. Use *Settings >> About Chrome* to see which is your current browser version.

* The driver has to be in the shell path. This, in practice, means different things for Mac and Windows computers. In Mac, it is typically ensured by copying the file `chromedriver.exe` to the folder `/usr/local/bin`. In Windows, by copying it to the Anaconda folder, which is probably in `C:\Users\username`. Anyway, if you have doubts about this point, check the path in the shell itself by entering `ECHO $PATH` if in Mac, or `ECHO %PATH%` if in Windows (remember to use Anaconda Prompt). Mind that this may change across versions of Anaconda.

* In a Mac computer, you will probably need to tell Mac OS to trust chromedriver. A simple way to that is to right click on the chromedriver icon, and select *Open* in the contextual menu. Help on this can be easily found in `support.apple.com`.

## The Python package selenium

The package `selenium` is a Python implementation of Selenium WebDriver. You can install this package with the shell command `pip install selenium`. Web scraping applications of Selenium use the module `selenium.webdriver`. The recommended import style is

```
from selenium import webdriver
```

This subpackage provides methods for different connections. Using `webdriver.Chrome` to connect to Chrome, your code could be as follows. First, you instantiate a Chrome browser with  

```
browser = webdriver.Chrome()
```

If Chrome was already running in your computer previous to this, don't worry. You can have several Chrome browsers working independently. You will notice that a Chrome instance starts when `browser` gets ready. You can then send a GET request with

```
browser.get(url)
```

If accepted, the GET request obtains a text file containing the source code of the page that the browser is currently displaying. The source code comes to your Python kernel as a string, which you can extract with the method `browser.page_source`. To get this, the browser (controlled by Selenium) may have executed some scripts without any human action. For the web scraper, this solves the problem of those pages that use AJAX to call other source files.

You can now apply the Beautiful Soup toolkit to the string returned by `browser.page_source`, as usual. Alternatively, you can continue with `selenium`. But, in any case, you may need additional steps to get the target page, before starting to scrape information. For instance, you may need to **click on a button** to accept cookies, or to **scroll down** to get a bigger page. Let us see how these jobs can be done.

## Button clicking

**Accepting cookies** is an example which illustrates how to operate when, in order to get the target page, you have to click on a button. This button will be one of the HTML elements contained in `browser.page_source`. You can find elements in the source code by using different different approaches, such as the `id` attribute of the element, or a CSS selector. To be able to do this, you have to import first the method `By`:

```
from selenium.webdriver.common.by import By
```

Now, if the button to be clicked has an `id` attribute with value, say `btn_id`, you can find it with

```
button = browser.find_element(By.ID, 'btn-id')
```

If there is an `id` attribute, `By.ID` may be the safest approach, since that attribute only can occur once in a HTML document. The search can also be based on a **CSS selector**, which is built joining the tag name and the class name. For instance if the tag name of the button is `button` (it typically is) and the class name is `class='classname'`, the CSS selector is `button.classname`. CSS selectors are displayed by the browser inspector when you are mouse hovering on the *Elements* panel.  

```
button = browser.find_element(By.CSS_SELECTOR, 'button.classname')
```

Instead of `By.CSS_SELECTOR`, you may prefer to use `By.XPATH`. **XPATH** is a language for searching in XML and HTML documents, which has the advantage that the specification of an attribute value is exact. The same system works for all types of attributes. 

```
button = browser.find_element(By.XPATH, '//button[@class="classname"]')
```

`find_element` has a logic similar to the Beautiful Soup method `find`. With `find_element`, you get a single element, the first one satisfying the request. With `find_elements`, you get a list with all the elements satisfying the request.

*Note*. A difference between `find` (Beautiful Soup) and `find_element` (Selenium) is that the first one returns `None` when the element searched does not exist, but the second one sends an error message.

Once you have captured the button, you click on it with

```
button.click()
```

Buttons for accepting may not appear in certain countries, in which regulation is more relaxed. So, it may be safer to search the button with `find_elements`, making the click conditional to the list returned not being empty:

```
button = browser.find_elements(By.ID, 'btn-id')
if len(button) == 1: button[0].click()
```

Sometimes you need to iterate the button clicking. An example is provided by the *Show more* buttons. In this case, it is useful to create a loop which keeps clicking the button until the *Show more* message disappears.   

## Scrolling down

Selenium uses the JavaScript methods `scrollTo` and `scrollBy` to scroll on a page. To scroll to a point of the page with coordinates `(x, y)`, you can use

```
browser.execute_script('window.scrollTo(x, y)')
```

The origin of this coordinate system, `(0, 0)`, is the top left corner of the page. Scrolling to the bottom of a page is typical. For that, you can use

```
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
```

Typically, the browser has to scroll to the bottom many times, until you get the complete information. You would use a loop for that. It is, in general, a good idea to maximize the browser window before starting the process, since scrolling is easily controlled in a manual way, but remote automatic control may fails by various reasons, and making room for the browser to display the page may help. To maximize the window, use:

```
browser.maximize_window()
```
