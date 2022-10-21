import snscrape.modules.twitter as sntwitter
import pandas as pd

# using snscrape for scrapping our tweets.

query = "amazon"
tweets = []
limit = 1000 # as mentioned in problem statement.

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    #print(vars(tweet))
    #break

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        # selecting our features based on which we will analyze the tweets

#creating a dataframe

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

