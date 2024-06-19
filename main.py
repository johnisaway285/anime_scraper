import requests,os,re
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
    scores=soup.find_all("td",class_="score ac fs14")
    genres=soup.find_all("div",class_="detail")
    print(genres[0].text)
    
    '''
    for score in scores:
        if score.text == "\n\n":
            scores.pop(scores.index(score))
    for title in titles:
        if title.text == "\n\n":
            titles.pop(titles.index(title))
    sheet["A1"].value="Ranking"
    sheet["B1"].value="Anime Name"
    sheet["C1"].value="Score"
    for i in range(0,50):
        sheet[f"A{i+2}"].value=i+1
        sheet[f"B{i+2}"].value=titles[i].text
        sheet[f"C{i+2}"].value=scores[i].text
    book.save(file_path)
    print("Top 50 anime saved to top_50.xlsx")
        
   ''' 
def create_empty():
    wb = excel.Workbook()
    wb.save(file_path)



if __name__=="__main__":
    main()