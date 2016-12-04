# googleScraping

Code that gets the first 10 pdf results of a given google query, and converts it to text

# Below are the prerequisites
1. sudo pip install requests
2. sudo pip install beautifulsoup4
3. sudo pip install PyPDF2
4. sudo pip install html2text
5. Also recursively do a chmod777 from basefolder. ie. main/src/ and outputs/ must be chmod777 so that the code can write into it.

#To run

1.git clone git@github.com:mithunpaul08/googleScraping.git

2. Go to src folder and type :python scraper.py
Eg: mithunpaul@chung:~/Desktop/fall2016NLPResearch/googleScraper/googleScraping/main/src$ python scraper.py

#to change the number of query results:
Update the value of the variable numberOfGoogleResults in scraper.py

#A basic set of results can be found in the /archive and /output folder.
