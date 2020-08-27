from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
import re

def extract_smarts():
    url = "https://e-onestop.pusan.ac.kr/menu/bbs/notice/list?menuId=20001104&rMenu=12"
    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome(
        r"C:\Users\CHAE GI JUNG\Desktop\Python_Crawling_Gitconnect\Python_Crawling\chromedriver_win32\chromedriver", options=options)
    browser.get(url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    results = soup.find('table', attrs={'id': 'bbs'}).find(
        'tbody').find_all('tr')

    smarts = []
    for result in results:
        datas = result.find_all('td')
        index = datas[0].get_text().strip()
        title = datas[1].a.get_text().strip()
        rate = datas[2].get_text().strip().replace('-', '.')
        link_index = re.findall("\\d+",datas[1].a['onclick'])[0]
        link = f"https://e-onestop.pusan.ac.kr/menu/bbs/notice/view?bbsConfNo=1&articleNo={link_index}&menuId=20001104&rMenu=12"
        print
        smarts.append(
            {'index': index, 'title': title, 'rate': rate, 'link': link}
        )

    browser.quit()
    return smarts


def get_smarts():
    smarts = extract_smarts()
    print(smarts)
    return smarts

def save_smt_db():
    connection = MongoClient('localhost', 27017)
    db = connection.crawling_db
    collection = db.smt_collection
    for smt in get_smarts():
        x = collection.update(smt, smt, upsert = True)
        print(x)


