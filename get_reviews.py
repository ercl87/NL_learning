
from bs4 import BeautifulSoup
import requests


import sentiment


url = "https://itunes.apple.com/us/rss/customerreviews/id=954338382/sortBy=mostRecent/xml"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data,"html.parser")

for block in soup.find_all('title'):

    text = block.find_next_sibling()
    if text.name != 'content':
        continue

    text = text.text
    print(text)
    

    sentiment.get_sentiment(text)
    import pdb;pdb.set_trace()



