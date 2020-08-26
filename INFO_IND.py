import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = "http://www.busanit.or.kr/board/list.asp?bcode=notice_e&sword=&search_txt=&ipage="

def extract_busanit(html,num):
    title = html.find("td",{"class":"subject"}).find('a')["title"].strip()
    rate = list(html.find_all("td",recursive = False))[2].string
    view = list(html.find_all("td",recursive = False))[3].string
    link = html.find("td",{"class":"subject"}).find('a')["href"]
    num = num
    return {
        "title":title,
        "rate":rate.replace("-","."),
        "view":view,
        "link":f"http://www.busanit.or.kr/board/{link}",
        "num":num
    }


def extract_busanits():
    busanits = []
    
    for page in range(1):
        
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

#def save_to_file(busanits):
#  file = open("busanit.csv", mode = 'w',encoding = "UTF-8-sig")
#  writer = csv.writer(file)
#  writer.writerow(["title", "rate", "file", "link"])
#  for busanit in busanits:
#    writer.writerow(list(busanit.values()))
#    print(busanit)
    
#  return

#busanits = get_busanits()
#save_to_file(busanits)