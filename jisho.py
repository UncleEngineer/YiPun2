import requests
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import time
import MeCab

def Jisho(vocab='昨日'):
    url = 'https://jisho.org/search/'+vocab
    page_html = requests.get(url)
    data = soup(page_html.text,'html.parser')
    meaning = data.find_all('span',{'class':'meaning-meaning'})
    trans = meaning[0].text
    return trans

wakati = MeCab.Tagger("-Owakati")
text = '私はタイ人です'
result = wakati.parse(text).split()
t1 = time.time()
for r in result:
    res = Jisho(r)
    print(r,res)

t2 = time.time()
print(t2-t1)
