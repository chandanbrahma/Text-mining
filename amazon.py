

##our  assignment is to choose one product from the Ecommerce website and put sentimental analysis based on the reviews it has got.
## i have bought a samsung galaxy M40 about six monthes earlier from Amazon, So lets get the reviews and also lets try to get the performance of the same.


##importing the necessery libraries 
import requests    
from bs4 import BeautifulSoup as bs 
import re 
import nltk
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
from wordcloud import WordCloud


# creating empty reviews list 
galaxy_m40_reviews =[]


for i in range(1,70):
  ip=[]  
  url = "https://www.amazon.in/Test-Exclusive-649/product-reviews/B07HGJFVMZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser") 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})
   
  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)
  # adding the reviews of one page to empty list which in future contains all the reviews  
  galaxy_m40_reviews=galaxy_m40_reviews+ip


    
# Joinining all the reviews into single paragraph 
galaxy_string = " ".join(galaxy_m40_reviews)



# converting each words to lower case and also removing numericals and symbols
galaxy_string = re.sub("[^A-Za-z" "]+"," ",galaxy_string).lower()
galaxy_string = re.sub("[0-9" "]+"," ",galaxy_string)



# words that contained reviews
galaxy_words = galaxy_string.split(" ")

#importing stopwords
with open("E:\\assignment\\text mining\\stop.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")

##applying stopwords on in the dataset
galaxy_words = [w for w in galaxy_words if not w in stopwords]



# Joinining all the reviews into single string to apply on wordcloud 
galaxy_string = " ".join(galaxy_words)


##  visualisation using wordcloud

wordcloud_ip = WordCloud(width=2400,height=1600).generate(galaxy_string)
plt.imshow(wordcloud_ip)

##from the plot we can see the words those are the most are wide angle, gb ram,blue varient, seawaterblue , screen sound etc
##now let us go for the negative as well as positive reviews so that we can know thw pros and cons.




##importing the positive words and applying on the string
with open("E:\\assignment\\text mining\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]


##checking the positive words and joining the positive words in a single string to apply on wordcloud
galaxy_pos= " ".join([w for w in galaxy_words if w in poswords])

wordcloud_pos = WordCloud(width=2400,height=1800).generate(galaxy_pos)
plt.imshow(wordcloud_pos)

## so from the word cloud we found some positive words for the phone like "good,supports,great,fast" etc
##so when we search the same words inside the reviews we found that it is a good budget phone,supports all aplications,
## people had a great experience as well as its processing speed is very fast


##now lets move for the negative words so that we can found out the cons for the same
##importing negative words and applying the same in the dataset
with open("E:\\assignment\\text mining\\negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

negwords = negwords[37:]

# negative word cloud
# Choosing the only words which are present in negwords
galaxy_neg = " ".join ([w for w in galaxy_words if w in negwords])

wordcloud_neg = WordCloud(width=2400,height=1800).generate(galaxy_neg)
                     
plt.imshow(wordcloud_neg)

##from the negative word cloud we have found some words as "punch,noise,dissappointed,dust,struggle" etc
## so based on the words we have searched the reviews and found that,
## people donot like the puchhole display that much they are excited of.
## noise cancellation is not that effective
## people are dissapointed with the battery and they struggling for the backup.

## hence we got an idea about the performance of the samsung galaxy M40 phone based on the reviews from Amazon.

