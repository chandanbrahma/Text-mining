import tweepy
import pandas as pd

Consumer_key='yJZb4kF71rS2XWIBhQKaFYl46'
Consumer_secret='SPa19LmfSIgo9Oa83Qu3XdlNeQwZW4OuCPeiDw9XW00WtxaVde'
Access_key='713260485236301824-6XPP17iv2claLjVmL0LnlrcJ6K24Wlj'
Access_secret='i9IXA6RnrcCqCJXQ64XJOrUWPyFbnUs52GYbfjlWiOpQm'
alltweets = []	
def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(Consumer_key,Consumer_secret)
    auth.set_access_token(Access_key,Access_secret)
    api = tweepy.API(auth)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    while len(new_tweets)>0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest) #save most recent tweets
        alltweets.extend(new_tweets) #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        print ("...%s tweets downloaded so far" % (len(alltweets)))
        
    outtweets = [[tweet.created_at,tweet.entities["hashtags"],tweet.entities["user_mentions"],tweet.favorite_count,
                  tweet.geo,tweet.id_str,tweet.lang,tweet.place,tweet.retweet_count,tweet.retweeted,tweet.source,tweet.text,
                  tweet._json["user"]["location"],tweet._json["user"]["name"],tweet._json["user"]["time_zone"],
                  tweet._json["user"]["utc_offset"]] for tweet in alltweets]
    
    
    tweets_df = pd.DataFrame(columns = ['text'])
   
    tweets_df["text"] = pd.Series([str(i[11]) for i in outtweets])
   
    return tweets_df

tweet = get_all_tweets("imVkohli")

# Joinining all the reviews into single paragraph 
tweet_string = " ".join(tweet['text'])

# Removing unwanted symbols incase if exists
import re
tweet_string = re.sub("[^A-Za-z" "]+"," ",tweet_string).lower()
tweet_string = re.sub("[0-9" "]+"," ",tweet_string)


## segrigating the words
tweet_words = tweet_string.split(" ")


##importing the stopwords and and applying on the dataset

with open("E:\\assignment\\text mining\\stop.txt","r") as sw:
    stopwords = sw.read().split('\n')

tweet_words =[ w for w in tweet_words if not w in stopwords]

tweet_string= " ".join(tweet_words)
##visualization
from wordcloud import WordCloud
import matplotlib.pyplot as plt

tweet_wordcloud = WordCloud(width=2000,height=1800).generate(tweet_string)
                     
plt.imshow(tweet_wordcloud)
## from the wordcloud we can visualize the words which are repeated the most

## now lets go for positive and negative words that are being used in the tweets

##importing positive words and applying on the tweet dataset
with open("E:\\assignment\\text mining\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]

tweet_pos= " ".join([w for w in tweet_words if w in poswords])

wordcloud_pos = WordCloud(width=2000,height=1800).generate(tweet_pos)
plt.imshow(wordcloud_pos)

##from the word cloud we can visualize the positive words those are usd in the tweet.

##importing negative words and applying onn the tweeet dataset

with open("E:\\assignment\\text mining\\negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

negwords = negwords[37:]

# negative word cloud
# Choosing the only words which are present in negwords
tweet_neg = " ".join ([w for w in tweet_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(width=2000,height=1800).generate(tweet_neg)
plt.imshow(wordcloud_neg_in_neg)
##from the word cloud we can visualize the negative words those are usd in the tweet