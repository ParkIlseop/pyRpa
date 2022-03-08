from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\\Users\\neope\\PycharmProject\\pyRpa\\pyRpa\\chromedriver.exe')  # 웹드라이버 켜기
driver.maximize_window()  # 크롬창 최대화
time.sleep(2)

# 네이버 로그인
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')
id = 'neopenta'
pw = 'neo97013284penta'
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
time.sleep(2)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
time.sleep(2)
login_btn = driver.find_element(By.ID, 'log.login').click()  # Id로 검색
time.sleep(2)

# 카페 메뉴 > 중고장터로 이동 > '16인치' 검색 및 이동
gocafe = driver.find_element(By.XPATH, '//*[@id="HOME_SHORTCUT"]/ul/li[6]/a').click()
time.sleep(2)
gomarket = driver.find_element(By.XPATH, '//*[@id="ct"]/div[2]/div[3]/div[1]/div[2]/a').click()
time.sleep(2)
search = driver.find_element(By.XPATH, '//*[@id="hd"]/div/div[3]/a').click()
time.sleep(2)
key = driver.find_element(By.XPATH, '//*[@id="cafe_search"]')
key.send_keys('16인치', Keys.ENTER)
time.sleep(2)

# 화면 가장 아래까지 스크롤 내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

def click_post(driver, n):
    driver.find_element(By.XPATH, '//*[@id="ct"]/div[2]/div[5]/div/div[2]/ul/li[{0}]/a/div/div[2]/h3'.format(n+1)).click()

for n in range(30):
    if n == 4:
        continue

    # checkClass = driver.find_element(By.CLASS_NAME, 'adtype_infinity')

    click_post(driver, n)
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select_one('title').get_text()
    price = soup.select_one('strong.price').get_text()
    date = soup.select_one('span.board_time').get_text()
    user = soup.select_one('strong.nickname').get_text()
    cond = soup.select_one('p.txt_desc').get_text()
    text = soup.select_one('div.se-component-content').get_text()
    content = "제목 : {0}\n가격 : {1}\n날짜 : {2}\n작성자 : {3}\n상태 : {4}\n본문 : {5}".format(title, price, date, user, cond, text)
    print(content)
    driver.back()

driver.quit()  # 브라우저 닫기