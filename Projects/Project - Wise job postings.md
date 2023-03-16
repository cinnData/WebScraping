# Project - Wise job postings

## Introduction

**Wise** (formerly TransferWise) is a London-based financial technology company founded by Estonian businessmen Kristo Käärmann and Taavet Hinrikus in January 2011. It provides **international money transfers**, claiming to charge as little as possible, with no subscription needed.

Wise job offers are posted at the **Wise Careers** page, which can be read at `transferwise.jobs/search`. When I'm writing this, there is information on 392 positions. To have access to all the positions, you have to make two steps:

* First, you have to **accept cookies**. 

* Once the cookies have been accepted, the page downloaded contains only nine job postings. We find, below the last posting, a *Show more* button. Clicking on the button, a new page is downloaded, showing nine additional postings. If we wish to capture all the postings, we have to click on this button repeatedly, until the *Show more* message disappears.

To manage the process in a Python program, you have an additional problem, that the text document that you obtain with a GET request is not the source code for any web page. It contains the HTML elements of the Wise Careers page that are fixed, and do not change when the information about the jobs is updated. It also contains a link to JavaScript program for the cookie acceptance step (`wise.com/cookie-consent.js`).

With **Selenium**, you create a zombie browser, controlled from the Python kernel. This browser will make the necessary steps so you can get the final source code, for 392 positions, as a string in Python. Once we have this, the scraping job can managed as in the previous examples.

## The target data

The objective of this example is to collect data on the positions offered at `transferwise.jobs/search` and to export them to a tabular file in which every row corresponds to a job. We aim at capturing the following fields:

* `link`, the link to a page specific for that position, which contains a description of the company and the role of the new employee. Example: '`www.wise.jobs/role/2451706-finance-data-analyst`'.

* `title`, the job title. Example: 'Finance Data Analyst'.

* `dept`, the department where the position is offered. Example: 'Finance'.

* `location`, the job location. Example: 'Tallinn'.
