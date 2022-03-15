import requests
from bs4 import BeautifulSoup as bs

url = 'https://datalab.naver.com/'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

findKeywordLank = soup.select('#content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel > div > div > div')

for keyword_rank in findKeywordLank:
    findDate = keyword_rank.select_one('div > strong > span').text
    print('날짜 : ', findDate)
    findItemList = keyword_rank.select(' div > div > ul > li > a')
    for list_area in findItemList:
        findRank = list_area.select_one('em').text
        findItemName = list_area.select_one('span').text
        print(findRank, '위 : ', findItemName)


# #content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel > div > div > div:nth-child(2)

# findTitle = soup.find_all('span', class_='title')
# for title in findTitle:
#    print(title.get_text())