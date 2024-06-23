import requests,os,re
import openpyxl as excel
from bs4 import BeautifulSoup


directory=os.getcwd()
file_name="top_50.xlsx"
file_path=os.path.join(directory,file_name)

def main():
    #Create an empty excel file
    create_empty()
    #Load the excel file and the active worksheet
    book=excel.load_workbook(file_path)
    sheet=book.active
    #In case the requests get blocked, I used headers to disguise the request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    raw_page_1=requests.get("https://myanimelist.net/topanime.php",headers=headers)
    #Parse the html for the top 50 aninme
    soup=BeautifulSoup(raw_page_1.text,"html.parser")
    #The url for the single anime description
    url_description="https://myanimelist.net/anime/{}"
    #Write the headers of the excel file
    sheet["A1"].value="Ranking"
    sheet["B1"].value="Anime Name"
    sheet["C1"].value="Score"
    sheet["D1"].value="Genres" 
    sheet["E1"].value="Synopsis"
    i=0
    #Special thanks for Andrej Kesely for the css selector tutorial
    #Choose the h3 tags with an id attribute(i.e. the animes)
    for a in soup.select("h3>a[id]"):
        title=a.text
        id_num=a["id"].removeprefix("#area").strip()
        url_fetch=url_description.format(id_num)
        raw_page_2=requests.get(url_fetch,headers=headers)
        soup_2=BeautifulSoup(raw_page_2.text,"html.parser")
        score=soup_2.find("div",class_=re.compile(r"score-label")).text
        synoposis=soup_2.find("p",attrs={"itemprop":"description"}).text
        genre_str=""
        # For some reasons, some animes have the genre tag as "Genre" and some as "Genres", therefore I included both cases
        if soup_2.select("div:-soup-contains('Genres:')>span[itemprop='genre']")==[]:
            for genre in soup_2.select("div:-soup-contains('Genre:')>span[itemprop='genre']"):
                genre_str+=genre.text+","
        else:
            for genre in soup_2.select("div:-soup-contains('Genres:')>span[itemprop='genre']"):
                genre_str+=genre.text+","
        #Remove the last comma
        genre_str=genre_str[:-1]
        sheet[f"A{i+2}"].value=i+1
        sheet[f"B{i+2}"].value=title
        sheet[f"C{i+2}"].value=score
        sheet[f"D{i+2}"].value=genre_str
        sheet[f"E{i+2}"].value=synoposis
        i+=1
    #Save the excel file
    book.save(file_path)
    #Let users know it's done
    print("Top 50 anime saved to top_50.xlsx")
        
def create_empty():
    '''
    Create an empty excel file
    If an existing file is found, it will be overwritten following the code in the main() function
    '''
    wb = excel.Workbook()
    wb.save(file_path)



if __name__=="__main__":
    main()