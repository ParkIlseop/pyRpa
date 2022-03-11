from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/Users/ilseoppark/pythonProject/pyRpa/chromedriver')  # 웹드라이버 켜기
driver.maximize_window()  # 크롬창 최대화
time.sleep(2)

driver.get('https://datalab.naver.com/shoppingInsight/sCategory.naver')
clickCategory = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/span').click()
time.sleep(2)
selectCategory =driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/ul/li[4]/a').click()
time.sleep(2)
clickInquire = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/a').click()
time.sleep(2)

def findItem():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('ul', 'rank_top1000_list')
    print(item.text)

def clickNextFindItem():
    clickNextPage = driver.find_element(By.XPATH,
                                        '//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
    time.sleep(2)
    findItem()


findItem()

for i in range(1, 25):
    clickNextFindItem()