import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('https://twitter.com/Gupta96Ayush')
html = response.read()
soup = BeautifulSoup(html, "lxml")

tweets = soup.find_all('li', 'js-stream-item')
tweet_text = soup.find_all('p', 'js-tweet-text')

print tweet_text
