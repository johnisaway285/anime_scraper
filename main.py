import requests
from bs4 import BeautifulSoup

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    raw_page=requests.get("https://myanimelist.net/topanime.php",headers=headers)
    soup=BeautifulSoup(raw_page.text,"html.parser")

    titles=soup.find_all("a",class_="hoverinfo_trigger")
    a=[]
    for title in titles:
        if title.text != "\n\n":
            a.append(title.text)
    print(a)

if __name__=="__main__":
    main()