# Project - Finding a job at Netflix

## Introduction

Like some other companies, Netflix posts its job offers at a platform called Lever. **Netflix job postings** can be found at `jobs.lever.co/netflix`. Let us call this page the main page. It will display, the day you visit it, a few hundred postings. These postings can be filtered by location, team and work type. Most of the postings on display are for teams in the Streaming division.

The main page contains, for each available position, basic information about the job, such as the job title, the location and the team, and a link to a page specific for that position, such as `jobs.lever.co/netflix/2d11d912-bfb3-4d9d-bfa1-0ce036214284`. This individual page presents a description of the company and the role of the new employee.

## The target data

The objective of this project is to collect data on the positions offered at `jobs.lever.co/netflix` and to export them to a tabular file in which every row corresponds to a job. The tools used are taken from the Python packages **Requests** and **Beautiful Soup**.

We aim at capturing the following fields:

* `link`, the link to a page specific for that position, which contains a description of the company and the role of the new employee. Example: `jobs.lever.co/netflix/620dd1ad-0345-42dc-a3b1-d94e1a08056b`.

* `title`, the job title. Example: 'Post Production Supervisor (Animation)'.

* `location`, the job location. Example: 'Los Angeles, California'.

* `division`, the first part of the job team. The two parts are separated by an n-dash. Example: 'Animation'.

* `dept`, the second part of the job team. Example: 'Editorial + Post'.
