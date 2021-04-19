import bs4
import urllib.request as req
from urllib.parse import quote
import csv

def getdata(): #把程式包裝成函式
  url=input("請輸入抓取PTT網址：")
  pages=int(input("請輸入抓取頁數："))
  kw=input("請輸入關鍵字：")
  n=0
 
  while n<pages:
    print("------【正在抓取第"+str(n+1)+"頁資料】------")
 
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"
      })
 
    with req.urlopen(request) as response:
      data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    #titles=root.find_all("div",class_="title")
    titles=root.select("div.title")

 
    for title in titles:
      if title.a!=None and kw in title.a.get_text(): 
        #使用title.a.get_text()指抓取文字，就不會有符號問題了!感謝Python社團大大相救
  
        print(title.a.string)
        print("https://www.ptt.cc"+title.a["href"])
        with open('output.csv', 'a', newline='',encoding="utf-8-sig") as csvfile:
          writer = csv.writer(csvfile, delimiter=' ')
          writer.writerow(title.a.string)
          writer.writerow("https://www.ptt.cc"+title.a["href"])
    nextlink=root.find("a",string="‹ 上頁")
    url=str("https://www.ptt.cc"+nextlink["href"]) 
    #print(nextlink)
    
    n+=1

getdata()
