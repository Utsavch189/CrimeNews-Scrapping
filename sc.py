#itdvH _3v379
import requests
from bs4 import BeautifulSoup
import requests
import selenium

#Terrorist data scrapping
url="https://timesofindia.indiatimes.com/topic/Terrorist-Attack"
r=requests.get(url)
c=r.content
s=BeautifulSoup(c,'html.parser')
#p=s.find_all("div",class_="Mc7GB").text
con={
    'heading':"",
    'date & time':"",
    'news':"",
}

for my_tag in s.find_all(class_="Mc7GB"):

    con={
    'heading': my_tag.span.text,
    
    'news': my_tag.p.text,
}
    
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(str(con))
    print("\n")   