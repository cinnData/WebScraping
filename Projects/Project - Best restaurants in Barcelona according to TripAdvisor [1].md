# Project - Best restaurants in Barcelona according to TripAdvisor [1]

## Introduction

**TripAdvisor** is a US travel and restaurant website company that shows hotel and restaurant reviews, accommodation bookings and other travel-related content. Headquartered in Needham, Massachusetts, TripAdvisor is the largest 'social travel website' in the world, with about 315 million reviewers (active and inactive) and about 500 million reviews of hotels, restaurants, attractions and other travel-related businesses. TripAdvisor was an early adopter of user-generated content. 

TripAdvisor services are free to users, who provide most of the content, and the website is supported by a hotel booking facility and an advertising business model. TripAdvisor proposals are grouped in different categories, such as *Hotels*, *Things to do*, *Restaurants*, etc. 

This example is focused on the top ranked restaurants in Barcelona. The starting URL is `tripadvisor.com/`  `Restaurants-g187497-Barcelona_Catalonia.html`. With `tripadvisor.es` instead of  `tripadvisor.com`, we get the Spanish version. The information is about the same in both sources, but `tripadvisor.es` show reviews on Spanish (some of them are automatic translations from English), while `tripadvisor.com` shows reviews in English. `tripadvisor.com` provides information on about 9,000 restaurants in Barcelona.

By editing the starting URL in the browser's adress bar, you can discover that the string 'g187497' identifies Barcelona, and that `tripadvisor.com/Restaurants-g187497` leads you to the same page. This page contains information on the 30 top ranked restaurants. Therefore, to get data on more restaurants, we have to scrape additional pages. To get these pages, we have to change accordingly the URL.

## The target data

The objective of this example is to collect data on the 450 top ranked restaurants and to export them to a tabular file in which every row corresponds to a restaurant. We aim at capturing the following fields:

* `rank`, the current rank of the restaurant in TripAdvisor.

* `name`, the name of the restaurant as it appears in the TripAdvisor's URL's. Example: 'BelleBuon'.

* `id`, a unique identifier for the restaurant. This ID is expected to be found as part of the link to the restaurant, in the same way that the ID of Barcelona ('g187497') is found as part of the URL of the restaurants in Barcelona. Example: 'd12207253'.

* `bubble`, the number of bubbles that approximate the average rating of the restaurant. It comes as a multiple of 0.5.

* `reviewCount`, the total number of reviews for that restaurant.

* `priceRange`, with values 'Fine Dining', 'Mid-range' y 'Cheap Eats'. In the webpage, these categories are indicated with dollar symbols ('\$\$\$\$', '\$\$ - \$\$\$' and '\$', respectively).

*Note*. You can easily increase the number of restaurants if you want, but we keep it low in this example, to save time and to prevent interruptions.
