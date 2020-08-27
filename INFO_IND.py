import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

URL = "http://www.busanit.or.kr/board/list.asp?bcode=notice_e&sword=&search_txt=&ipage="

def extract_busanit(html,num):
    index = list(html.find_all("td",recursive = False))[0].string
    title = html.find("td",{"class":"subject"}).find('a')["title"].strip()
    rate = list(html.find_all("td",recursive = False))[2].string
    link = html.find("td",{"class":"subject"}).find('a')["href"]
    num = num
    return {
        "index":index,
        "title":title,
        "rate":rate.replace("-","."),
        "link":f"http://www.busanit.or.kr/board/{link}",
        "num":num
    }


def extract_busanits():
    busanits = []
    
    for page in range(5):
        
        print(f"Scrapping busanit : Page:{page+1}")
        result = requests.get(f"{URL}{page + 1}")
        soup = BeautifulSoup(result.content.decode('UTF-8','replace'), 'html.parser')
        results = soup.find("div",{"class":"content_sub"}).find("table", {"class":"bbs_ltype"}).find("tbody").find_all("tr")
        i = 1
        for result in results:
            busanit = extract_busanit(result,i)
            busanits.append(busanit)
            i+=1
    return busanits
   

def get_busanits():
  busanits = extract_busanits()
  return busanits

def save_ind_db():
    connection = MongoClient('localhost', 27017)
    db = connection.crawling_db
    collection = db.ind_collection
    for ind in get_busanits():
        x = collection.update(ind, ind, upsert = True)
        print(x)

#def save_to_file(busanits):
#  file = open("busanit.csv", mode = 'w',encoding = "UTF-8-sig")
#  writer = csv.writer(file)
#  writer.writerow(["title", "rate", "file", "link"])
#  for busanit in busanits:
#    writer.writerow(list(busanit.values()))
#    print(busanit)
    
#  return

# busanits = get_busanits()
#save_to_file(busanits)