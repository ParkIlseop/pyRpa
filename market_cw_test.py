from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/ilseoppark/pythonProject/pyRpa/chromedriver')  # 웹드라이버 켜기
time.sleep(2)

# 네이버 로그인
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')
ID = 'neopenta'
PW = 'neo97013284penta'
driver.execute_script("document.getElementsByName('id')[0].value=\'" + ID + "\'")
time.sleep(2)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + PW + "\'")
time.sleep(2)
login_btn = driver.find_element(By.ID, 'log.login').click()  # Id로 검색
time.sleep(2)

# 카페 메뉴 > 중고장터로 이동 > '16인치' 검색 및 이동
gocafe = driver.find_element(By.XPATH, '//*[@id="HOME_SHORTCUT"]/ul/li[6]/a').click()
time.sleep(2)
gomarket = driver.find_element(By.XPATH, '//*[@id="ct"]/div[2]/div[3]/div[1]/div[2]/a').click()
time.sleep(2)
search = driver.find_element(By.XPATH, '//*[@id="hd"]/div/div[3]/a').click() # //*[@id="hd"]/div/div[3]/a
time.sleep(3)
key = driver.find_element(By.XPATH, '//*[@id="ct"]/div/div/div[1]/div[1]/div/input')
key.send_keys('16인치', Keys.ENTER)
time.sleep(3)

# 16인치 검색 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

findList_area = soup.select('#ct > div > div > div.search_results_list > div.search_list > div > div > ul > div')  # 상품 list 영역 불러오기

# 매물 제목 먼저 가져오기
for findItemTitle in findList_area:
    itemTitle = findItemTitle.select_one('a > div > strong.title').text
    print(itemTitle)

driver.quit()

# def click_post(driver, n):
#     driver.find_element(By.XPATH, '//*[@id="ct"]/div[2]/div[5]/div/div[2]/ul/li[{0}]/a/div/div[2]/h3'.format(n+1)).click()
#
# for n in range(30):
#     if n == 4:
#         continue
#
#     # checkClass = driver.find_element(By.CLASS_NAME, 'adtype_infinity')
#
#     click_post(driver, n)
#     time.sleep(2)
#
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#
#     title = soup.select_one('title').get_text()
#     price = soup.select_one('strong.price').get_text()
#     date = soup.select_one('span.board_time').get_text()
#     user = soup.select_one('strong.nickname').get_text()
#     cond = soup.select_one('p.txt_desc').get_text()
#     text = soup.select_one('div.se-component-content').get_text()
#     content = "제목 : {0}\n가격 : {1}\n날짜 : {2}\n작성자 : {3}\n상태 : {4}\n본문 : {5}".format(title, price, date, user, cond, text)
#     print(content)
#     driver.back()
#
# driver.quit()