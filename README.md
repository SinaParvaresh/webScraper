# SubReddit-StockScraper
 

## A subReddit stock title scraper

This program will scrape any subreddit set by the user, and return the top 5 most frequently mentioned stocks.

## Installation

Check if Python is installed (version 3 is required)

```
python --version
```
or

```bash
python3 --version
```

If not installed and on Windows, download from the Microsoft Store.

## After Installation

You **MUST** create your own separate praw.ini file, where you will assign and store your reddit credentials such as the client ID, Client secret and your Reddit username/password.

Set the paramters of your SubReddit scraper such as the number of posts to go through, or the particular subreddit (possibly another stock subreddit such as r/Investing or r/StockMarket).

A CSV which contains the information of each topic in the sub Reddit such as the title, date/time posted, and score is automatically created when running the program.
