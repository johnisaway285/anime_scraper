# Anime List Scraper
> [!IMPORTANT]
> Program is now functional. For some animes, genres don't come through and therefore some animes' genres will be left empty

This is for you anime fans out there who want to binge-watch animes but don't know which one to go for.

## Description
This program will go onto [MyAnimeList](https://myanimelist.net/topanime.php) and fetch the top 50 Animes that are currently trending.

It'll generate a excel spreadsheet which you can open to see the details of these animes.

## Details will be included:
- Ranking (Completed)
- Name (Completed)
- Score (completed)
- Details/Synoposis (Completed)
- Genre (90% complete)


## How to run this program?
 TL;DR:
 1. Download this repository
 2. Change directory to the repository(i.e the folder you just git cloned / downloaded)
 3. Run this program

 **Longer version**:
 
 you need to **download** this repository (copy this command downbelow and run it in your terminal):
> [!IMPORTANT]
> Make sure you install the modules in the requirements.txt before you execute any of the commands below. Otherwise the program won't work if you lack any of the modules.
> A helpful command would be:
```
pip3 install -r requirements.txt
```
to get all the prerequsite modules all at once.

If you know how to download otherwise, knock yourself out! For the sake of convenience, here is the command:
```
git clone https://github.com/johnisaway285/anime_scraper
```

Then you need to change directory to the repository you just downloaded:
```
cd /path/to/directory
```

Final step! Run this program and have fun!
```
python3 main.py
```

Special thanks goes to Andrej Kesely([kiwwisk](https://github.com/kiwwisk)) for showing me how CSS selectors works!