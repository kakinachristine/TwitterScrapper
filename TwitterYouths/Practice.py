from pandas.io import api

import snscrape.modules.twitter as sntwitter
import pandas as pd
from time import sleep

# tweet = api.get_status('tweet_id')
# print(dir(tweet))
# Creating list to append tweet data to
tweets_list1 = []

user_name = input("Enter your keywords; ")
numbers = int(input("Enter number of tweets to be scrapped: "))
since_date = "2022-01-01"
query = f"from:{user_name} since:{since_date} -filter:retweets"
# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(query)).get_items()):
    if i > numbers:
        break
    tweets_list1.append([
      tweets.date,
      tweets.id,
      tweets.rawContent,
      tweets.user.username,
      tweets.likeCount,
      tweets.retweetCount,
      # tweets.user.location,
      # tweets.hashtags,
      tweets.source])

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Date', 'Tweet Id', 'Content', 'Username','LikeCount','retweetCount','source'])
tweets_df1.to_csv(f'{user_name}.csv', encoding='utf-8')
