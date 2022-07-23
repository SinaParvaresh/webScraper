# Subreddit-StockScraper
 

## A Subreddit stock title scraper

This program will scrape any subreddit set by the user, and return the top 5 most frequently mentioned stocks. The stocks are then stored in a JSON file, where the user can view when each group of stocks were added.

A CSV which contains the information of each topic in the subreddit such as the title, date/time posted, and score is automatically created for you when running the program.


## Installation

Check if Python is installed (version 3.7+ is required)

```
python --version
```
or

```
python3 --version
```

If not installed and on Windows, download from the Microsoft Store.

## After Installation

You **MUST** create your own separate praw.ini file, where you will assign and store your reddit credentials such as the client ID, Client secret and your Reddit username/password.
These credentials can be obtained by applying for a [Reddit API Key](https://www.reddit.com/wiki/api/#wiki_reddit_api_access).

##### Set the paramters of your subreddit scraper such as: 

Number of posts to go through (Default set to 100) 

Particular subreddit (possibly another stock subreddit such as r/Investing or r/StockMarket).


