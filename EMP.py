import requests 
from bs4 import BeautifulSoup 
pageChar = 100


URL = f"https://cse.pusan.ac.kr/cse/14667/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYxNiUyRmFydGNsTGlzdC5kbyUzRmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZzcmNoQ29sdW1uJTNEJTI2cGFnZSUzRD{chr(pageChar)}lMjZzcmNoV3JkJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZiYnNDbFNlcSUzRCUyNnJn"

#def get_last_pages():
#  result = requests.get(URL)
#  soup = BeautifulSoup(result.text, "html.parser")
#  pagination = soup.find("div", {"class":"s-pagination"})
#  links = pagination.find_all('a')

#  last_page = links[-2].get_text(strip=True)
#  return int(last_page)

def extract(html, html2, html3, num):
    
    title = html.find("strong").string
    link = html.find("a")["href"]
    date = html2.string
    index = html3.string
    return {"index": index,"title": title,"date": date, "link": f"http://cse.pusan.ac.kr{link}", "num": num}

def extracts():
  emps = []
  pageChar = 65
  
  for page in range(1):
   pageChar += 4
   print(f"Scrapping emp {page+1} page")
   result = requests.get(f"https://cse.pusan.ac.kr/cse/14667/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYxNiUyRmFydGNsTGlzdC5kbyUzRmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZzcmNoQ29sdW1uJTNEJTI2cGFnZSUzRD{chr(pageChar)}lMjZzcmNoV3JkJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZiYnNDbFNlcSUzRCUyNnJn")
  
   soup = BeautifulSoup(result.text, "html.parser")
   results = soup.find_all("td", {"class":"_artclTdTitle"})
   results2 = soup.find_all("td", {"class":"_artclTdRdate"})
   results3 = soup.find_all("td", {"class":"_artclTdNum"})
   num = 1
   i = 0
   for result3 in results3:
      if result3.string != None:
        emp = extract(results[i], results2[i], result3, num)
        print(emp)
        emps.append(emp)
        num += 1
 
        
      i+=1
  return emps

def get_emps():
  #last_page = get_last_pages()
  emps = extracts()
  return emps

# emps = get_emps()