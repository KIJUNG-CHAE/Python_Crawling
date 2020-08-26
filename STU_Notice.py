import requests
from bs4 import BeautifulSoup
import csv

LIMIT = 50
URL1 = "https://e-onestop.pusan.ac.kr/index?home=home"
URL2 = "menuId=20001104&rMenu=12&a"
headers = {'Accept-Language' : "ko-KR"}

def extract_stu_notice(html, num):
    title = html.find('a').string 
    print(title)
    rate = html.find("span").string
    link = html.find('a')["href"]
    num = num
    return {
        "title":title,
        "rate":rate,
        "link":f"https://e-onestop.pusan.ac.kr/{link}",
        "num":num
    }


def extract_stu_notices():
    notices = []

    print(f"Scrapping Notice : Page:1")
    result = requests.get(f"{URL1}", verify =False, headers = headers)
    # print(result)
    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup)
    results = soup.find_all("td",{"class":"table_m"})
    print(results)
    i = 1
    for result in results:
        notice = extract_stu_notice(result, i)
        notices.append(notice)
        i+=1
    
    return notices


def get_stu_notices():
  notices = extract_stu_notices()
  return notices

#def save_to_file(notices):
#  file = open("notice.csv", mode = 'w',encoding = "CP949")
#  writer = csv.writer(file)
#  writer.writerow(["title", "rate", "file", "link"])
#  for notice in notices:
#    writer.writerow(list(notice.values()))
#    print(notice)
    
#  return

#notices = get_notices()
#save_to_file(notices)