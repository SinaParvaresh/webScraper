from ast import operator
from http.client import CREATED
from pydoc_data.topics import topics
from turtle import title
import praw
import pandas as pd
import datetime as dt
from tabulate import tabulate
import csv
import re
import operator

# Get credentials from DEFAULT instance in praw.ini
reddit = praw.Reddit()

#a class that scrapes a particular subreddit and
#will sort by new, and a limit on how many posts to go through
class SubredditSraper:

        

    def __init__(self, lim = 100, sort = 'new', sub = 'wallstreetbets'):
        self.sub = sub
        self.lim = lim
        self.sort = sort
    

    #read the NYSE CSV file for stock names, then get each of the subreddit posts' attributes
    def getPosts(self):
        
        #create dict with stock names
        stockNames = {}
        with open('nasdaq_screener.csv', mode ='r') as infile:
            reader = csv.reader(infile)
            for column in reader:
                stockNames[column[0]] = {}
            stockNames_dict = dict.fromkeys(stockNames,0)
           

       

        topics_dict = { "title":[], 
                "score":[], 
                "url":[],
                "created":[] }

        sortedSubreddit = reddit.subreddit(self.sub).new(limit=self.lim)

        for post in sortedSubreddit:
            topics_dict["title"].append(post.title)
            topics_dict["score"].append(post.score)
            topics_dict["url"].append(post.url)
            topics_dict["created"].append(post.created)

        #put the posts' attributes in a dataframe and then a CSV
        wsb_data = pd.DataFrame(topics_dict)

        #convert unix timestap to readable data
        def get_date(created):
            return dt.datetime.fromtimestamp(created)

        _timestampColumn = wsb_data['created'].apply(get_date)
        wsb_data = wsb_data.assign(timestampColumn = _timestampColumn)
        wsb_data = wsb_data.drop(columns='created')

        wsb_csv = wsb_data.to_csv('wsb.csv', index=False)

        #find stock names in each post
        #we convert our titles from a list to a set, as sets have a much faster lookup time
        titleSet = set(topics_dict['title'])

        for title in titleSet:
            for stock in stockNames.keys():
                if re.search(r'\s+\$?' + stock + r'\$?\s+', title):
                    stockNames_dict[stock] += 1
                    print('Stock name:', stock, "\nTitle is:", title, "\n---------------")
        
        #sorting the list of the most popular stocks, and choosing the top 5
        topStocks = dict(sorted(stockNames_dict.items(), key=operator.itemgetter(1), reverse=True)[:5])
        print(topStocks)
    


if __name__ == '__main__':
    SubredditSraper(lim = 1000).getPosts()