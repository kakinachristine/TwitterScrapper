import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter

scraper = sntwitter.TwitterSearchScraper("#python")

for tweet in scraper.get_items():
  break

tweet
#scraper = sntwitter.TwitterSearchScraper("#gbv OR #violence OR #DomesticViolence #SexualAbuse OR #DomesticAbuse OR #ViolenceAgainstWomen OR #harassment OR #femicide OR #women OR #rape OR #domesticviolence OR #sexualassault")
scraper = sntwitter.TwitterSearchScraper("#GenderBiasSports OR #AUSOPEN OR #AUSTRALIANOPEN OR #AUS2023 OR #SIBALENKA OR #DiscriminationAgainstWomen OR #tennispricemoney OR #NaomiOsaka OR #WTA OR #AUS2023Finals OR #Tennis OR #ATPTour OR #WTA OR #GrandSlam# OR #TennisNews OR #TennisUpdates OR #TennisLive OR #TennisMatches OR #TennisTournament")
n_tweets = 12000
tweets = []

for i, tweet in tqdm(enumerate(scraper.get_items()), total=n_tweets):
  # data = [
  #     tweet.date,
  #     tweet.id,
  #     tweet.rawContent,
  #     tweet.username,
  #     tweet.likeCount,
  #     tweet.retweetCount,
  #     tweet.user.location,
  #     tweet.hashtags,
  #     tweet.source
  #     #tweet.geocode
  # ]
  # tweets.append(data)
  # if i > n_tweets:
  #   break

    if i >= n_tweets:
        break
    tweets.append([
        tweet.date,
        tweet.id,
        tweet.rawContent,
        tweet.user.username,
        tweet.likeCount,
        tweet.retweetCount,
        # tweets.user.location,
        # tweets.hashtags,
        tweet.source])

tweet_df = pd.DataFrame(
    tweets, columns=['date', 'id', 'content', 'username', 'likeCount', 'retweetCount','location','hashtag','source']
    )
tweet_df.to_csv("Twitter_Data1.csv", index=False)

tweet_df

len(tweets)

# Data Cleaning and Eploratory Analysis

tweet_df.head()

tweet_df = pd.DataFrame(
    tweets, columns=['date', 'id', 'content', 'username', 'likeCount', 'retweetCount','location','hashtag','source']
    )
tweet_df.to_csv("gbv-tweets_2.csv", index=False)

tweet_df.shape

