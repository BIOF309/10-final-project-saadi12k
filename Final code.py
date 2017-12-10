# We will use 4 python libraries. json for parsing the data; pandas for data manipulation; matplotlib for creating charts; and re for regular expressions
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

def word_in_text(word, text):
    if text == None:
        return False
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

    # Reading Tweets
print('Reading Tweets\n')
tweets_data_path = "twitter_data.txt"

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print (len(tweets_data))

# Structuring Tweets
print('Structuring Tweets\n')
tweets = pd.DataFrame()

#tweets['YOUR STRING HERE'] = list(map(lambda tweet: tweet.get('YOUR STRING HERE', None),tweets_data))
tweets['text'] = list(map(lambda tweet: tweet.get('text', None),tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet.get('lang', None),tweets_data))
tweets['country'] = list(map(lambda tweet: tweet.get('place',{}).get('country', None) if tweet.get('place') != None else None,tweets_data))
# Analyzing Tweets by Language
print('Analyzing tweets by language\n')
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:10].plot(ax=ax, kind='bar', color='red')
plt.savefig('tweet_by_lang', format='png')
print(len(tweets_by_lang))
plt.show()

# Analyzing Tweets by Country
print('Analyzing tweets by country\n')
tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:20].plot(ax=ax, kind='bar', color='green')
plt.savefig('tweet_by_country', format='png')
plt.show()

#now we introduce columns for the specific sport
tweets['basketball'] = tweets['text'].apply(lambda tweet: word_in_text('basketball', tweet))
tweets['soccer'] = tweets['text'].apply(lambda tweet: word_in_text('soccer', tweet))
tweets['football'] = tweets['text'].apply(lambda tweet: word_in_text('football', tweet))

 #Here we have the frequency of each keyword used
print('basketball', tweets['basketball'].value_counts()[True])
print("soccer", tweets['soccer'].value_counts()[True])
print("football", tweets['football'].value_counts()[True])

#similar to before, we plot the ranking of each sport
type_sport = ['basketball', 'soccer', 'football']
tweets_by_type_sport = [tweets['basketball'].value_counts()[True], tweets['soccer'].value_counts()[True], tweets['football'].value_counts()[True]]

x_pos = list(range(len(type_sport)))
width = 0.5
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_type_sport, width, alpha=1, color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: basketball vs. soccer vs. football (english + american) (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(type_sport)
plt.grid()
plt.savefig('tweets_by_type_sport_1', format='png')
plt.show()

 #No we do a similar comparison but now with a popular name in each respective sport
#first we define columns such that we can check if the givem name is mentioned in a tweet
tweets['lebron'] = tweets['text'].apply(lambda tweet: word_in_text('lebron', tweet))
tweets['ronaldo'] = tweets['text'].apply(lambda tweet: word_in_text('ronaldo', tweet))
tweets['brady'] = tweets['text'].apply(lambda tweet: word_in_text('brady', tweet))

print('lebron', tweets['lebron'].value_counts()[True])
print("ronaldo", tweets['ronaldo'].value_counts()[True])
print("brady", tweets['brady'].value_counts()[True])

#similar to before, we plot the ranking of each sport
pop_players = ['lebron', 'ronaldo', 'brady']
tweets_by_pop_players = [tweets['lebron'].value_counts()[True], tweets['ronaldo'].value_counts()[True], tweets['brady'].value_counts()[True]]

x_pos = list(range(len(pop_players)))
width = 0.5
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_pop_players, width, alpha=1, color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Lebron vs. Ronaldo vs. Brady (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(pop_players)
plt.grid()
plt.savefig('tweets_by_pop_players', format='png')
plt.show()
