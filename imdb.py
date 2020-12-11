

## our  assignment is to extract movie reviews for any movie from IMDB and perform sentimental analysis
##I am extracting one of my all time favorite movie The dark night(2008) which is the second part of the batman series
## it has a IMDB rating of 9/10 and also famous for the iconic character of Joker.
## So let Scarp the reviews for the movie from IMDB and try to find some sentimental analysis.


 
##importing the necessery libraries
import requests   
from bs4 import BeautifulSoup as bs 
import re 
import nltk
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
from wordcloud import WordCloud


# creating empty reviews list  
darknight_reviews =[]


for i in range(1,50):
  ip=[]  
  url = "https://www.imdb.com/title/tt0468569/reviews?ref_=tt_ov_rt"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser") 
  reviews = soup.findAll("div",attrs={"class","text show-more__control"})
   
  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)
  # adding the reviews of one page to empty list which in future contains all the reviews  
  darknight_reviews=darknight_reviews+ip


    
# Joinining all the reviews into single paragraph 
darknight_string = " ".join(darknight_reviews)



# converting each words to lower case and also removing numericals and symbols
darknight_string = re.sub("[^A-Za-z" "]+"," ",darknight_string).lower()
darknight_string = re.sub("[0-9" "]+"," ",darknight_string)



# words that contained in reviews
darknight_words = darknight_string.split(" ")

#importing stopwords
with open("E:\\assignment\\text mining\\stop.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")

##applying stopwords on in the dataset
darknight_words = [w for w in darknight_words if not w in stopwords]



# Joinining all the reviews into single string to apply on wordcloud 
darknight_string = " ".join(darknight_words)


##  visualisation using wordcloud

wordcloud_ip = WordCloud(width=2400,height=1600).generate(darknight_string)
plt.imshow(wordcloud_ip)

##from the plot we can see the words like "Heath ledger,christopher nolan, bruce wayne, dark night, gotham city" etc
##now lets move forward to get more details for the same and for the negative as well as positive reviews.


##importing the positive words and applying on the string
with open("E:\\assignment\\text mining\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]


##checking the positive words and joining the positive words in a single string to apply on wordcloud
darknight_pos= " ".join([w for w in darknight_words if w in poswords])

wordcloud_pos = WordCloud(width=2400,height=1800).generate(darknight_pos)
plt.imshow(wordcloud_pos)

## so from the word cloud we found some positive words for the movie like "brilient,entertaining,great work,perfect, humor, thril,powerful" etc
## So from the thos words if we checkk in the reviews we can find that all are appriciating the brilient performance,also there great and powerful work
## the audience have enjoyed the humour, thrill between batman and the joker


##now lets move for the negative words so that we can found out the cons for the same
##importing negative words and applying the same in the dataset
with open("E:\\assignment\\text mining\\negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

negwords = negwords[37:]

# negative word cloud
# Choosing the only words which are present in negwords
darknight_neg = " ".join ([w for w in darknight_words if w in negwords])

wordcloud_neg = WordCloud(width=2400,height=1800).generate(darknight_neg)
                     
plt.imshow(wordcloud_neg)

## from the negative words we will mostly finf one word i.e joker. If we go for the word in the coment we will find that the centre of attraction of the movie is the Joker
##and his negativity, He has nailed it with his negative role.
## other words we can see like dark , complex crazy etc which are describing the complexicity of the movie and the crazyness of joker.

##so finally we got the review of the Dark Night movie and also an idea of their performance.
