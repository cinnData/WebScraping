# Project - Best restaurants in Barcelona according to TripAdvisor [2]

## Introduction

This example is the second part of the TripAdvisor project. Now, we extract data from the restaurant pages. In the first part of the project, we collected data from 15 pages, each page reporting 30 restaurants. Now, we will scrape the 450 pages of these restaurants, collecting extra data.

To get the page of a restaurant, we use the id of the restaurant. So, BelleBuon, the first-ranked restaurant (when I'm writing this), will be found at `https://www.tripadvisor.com/Restaurant_Review-g187497-d4049034`.

## The target data

In this second part, we aim at capturing the following fields:

* `claimed`, a True/False column indicating whether the restaurant's page displays the message 'Claimed' on the right side of the restaurant's name. This message tells us that somebody from the business manages the listing.

* `travelers`, a True/False column indicating whether the restaurant has a Traveler's Choice Award.

* `photos`, the number of photos of that restaurant available at its website. It is shown in a link 'See all (# photos)'.

* `thefork`, a True/False column indicating whether the restaurant has an option for reserving a table through TheFork.

* `justeat`, a True/False column indicating whether the restaurant has an option for ordering online to get food delivered by Just Eat.

* `cuisines`, a collection of culinary options placed in the *Details* section of the page, under the heading *CUISINES*. It may be missing. Example: 'Italian, Mediterranean, European, Northern-Italian, Southern-Italian'.

* `diets`, a collection of dietary options placed in the *Details* section, under the heading *SPECIAL DIETS*. It may be missing. Example: 'Vegetarian Friendly, Vegan Options, Gluten Free Options'.

* `meals`, a collection of meal's options placed in the *Details* section, under the heading *MEALS*. It may be missing. Example: 'Lunch, Dinner, Drinks'.

* `features`, a collection of features placed in the *Details* section, under the heading *FEATURES*. It may be missing. Example: 'Reservations, Outdoor Seating, Seating, Serves Alcohol, Full Bar, Free Wifi, Accepts Credit Cards, Table Service, Wine and Beer, Dog Friendly, Gift Cards Available'.

* `neigh`: the neighborhood where the restaurant is. It is placed in the *Location and contact* section. Example: 'El Baix Guinardo'.

* `excellent`: the number of reviews in English with rating 5.

* `verygood`: the number of reviews in English with rating 4.

* `average`: the number of reviews in English with rating 3.

* `poor`: the number of reviews in English with rating 2.

* `terrible`: the number of reviews in English with rating 1.

* `revEnglish`: the number of reviews in English.

* `revSpanish`: the number of reviews in Spanish.

## Homework

1. Some restaurants include a link to a website in the *Location and contacts* section. Add a True/False column indicating whether the restaurant's page contains such link. 

2. Some restaurants include a mailto link  in the *Location and contacts* section. Add a True/False column indicating whether the restaurant's page contains such link. 