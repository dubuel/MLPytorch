import requests
import re
from bs4 import BeautifulSoup
# 위의 두 모듈이 없는 경우에는 pip install requests bs4 실행

def get_news_content(url):
    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html5lib')

    div = soup.find('div', attrs = {'id' : 'harmonyContainer'})
    
    content = ''
    for paragraph in div.find_all('p'):
        content += paragraph.get_text()
        
    return content

news1 = get_news_content('https://news.v.daum.net/v/20190617073049838')

re.search(r'[\w-]+@[a-zA-Z.]+',news1)