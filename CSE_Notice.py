import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# import csv

URL1 = f"https://cse.pusan.ac.kr/cse/14651/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYwNSUyRmFydGNsTGlzdC5kbyUzRmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZzcmNoQ29sdW1uJTNEJTI2cGFnZSUzRD"
URL2 = f"lMjZzcmNoV3JkJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZiYnNDbFNlcSUzRCUyNnJnc0VuZGRlU3RyJTNEJTI2"

def extract_notice(html, num):
    index = html.find("td",{"class":"_artclTdNum"}).string
    title = html.find("td",{"class":"_artclTdTitle"}).find('a').find("strong").string 
    rate = html.find("td",{"class":"_artclTdRdate"}).string.strip()
    file = html.find("td",{"class":"_artclTdAtchFile"}).string.strip()
    link = html.find("td",{"class":"_artclTdTitle"}).find('a')["href"]
    # num = num
    
    return {
        "index":index,
        "title":title,
        "rate":rate,
        "file":file,
        "link":f"https://cse.pusan.ac.kr{link}",
        "num":num
    }


def extract_notices():
    notices = []
    
    for page in range(5):
        page_alphabet = chr(69 + page*4)
        print(f"Scrapping Notice : Page:{page+1}")
        result = requests.get(f"{URL1}{page_alphabet}{URL2}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find("table",{"class":"artclTable artclHorNum1"}).find("tbody").find_all("tr")
        i = 1
        for result in results:
            if result.find("td",{"class":"_artclTdNum"}).string != None:
                notice = extract_notice(result, i)
                notices.append(notice)
                i+=1
    
    return notices


def get_notices():
  notices = extract_notices()
  return notices

def save_cse_db():
    connection = MongoClient('localhost', 27017)
    db = connection.crawling_db
    collection = db.cse_collection
    for notice in get_notices():
        x = collection.update(notice, notice, upsert = True)
        print(x)

#def save_to_file(notices):
#  file = open("notice.csv", mode = 'w',encoding = "CP949")
#  writer = csv.writer(file)
#  writer.writerow(["title", "rate", "file", "link"])
#  for notice in notices:
#    writer.writerow(list(notice.values()))
#    print(notice)
    
#  return




#save_to_file(notices)