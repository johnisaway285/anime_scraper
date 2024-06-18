import requests,os
import openpyxl as excel
from bs4 import BeautifulSoup

directory=os.getcwd()
file_name="top_50.xlsx"
file_path=os.path.join(directory,file_name)

def main():
    create_empty()
    book=excel.load_workbook(file_path)
    sheet=book.active
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    raw_page=requests.get("https://myanimelist.net/topanime.php",headers=headers)
    soup=BeautifulSoup(raw_page.text,"html.parser")
    titles=soup.find_all("a",class_="hoverinfo_trigger")
    a={}
    
    for title in titles:
        if title.text == "\n\n":
            titles.pop(titles.index(title))
    for i in range(50):
        a[i+1]=titles[i].text    
    sheet["A1"].value="Ranking"
    sheet["B1"].value="Anime Name"
    for i in range(1,51):
        sheet[f"A{i+1}"].value=i
        sheet[f"B{i+1}"].value=a[i]
    book.save(file_path)

        
    
def create_empty():
    wb = excel.Workbook()
    wb.save(file_path)

if __name__=="__main__":
    main()