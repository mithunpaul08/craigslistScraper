# CraigsList scraper for used cars

Code that gets the used car results of a given craigslist query, and converts it to text

# Below are the prerequisites
1. sudo pip install requests
2. sudo pip install beautifulsoup4
3. sudo pip install PyPDF2
4. sudo pip install html2text
5. sudo pip install pyinstaller
5. Also recursively do a chmod777 from basefolder. ie. main/src/ and outputs/ must be chmod777 so that the code can write into it.

#To run

1.git clone git@github.com:mithunpaul08/craigslistScraper.git

2. Go to src folder and type :python scraper.py
Eg: mithunpaul@chung:~/Desktop/fall2016NLPResearch/googleScraper/googleScraping/main/src$ python scraper.py

#to change the parameters:
Update the value of the variable numberOfGoogleResults in scraper.py in this function


#"Search Query attributes used to build the query string"
def fillSearchQueryAttributes(queryCar):
    queryCar.min_price = "1"
    queryCar.max_price ="6000"
    queryCar.auto_make_model="honda+%7C+toyota"
    queryCar.min_auto_year="2005"
    queryCar.max_auto_year="2016"
    queryCar.min_auto_miles='300'
    queryCar.max_auto_miles='110000'
    queryCar.auto_title_status='1'

#changing email parameters
gmailUsername=“2324@gmail.com"
gmailPwd=""
fromaddr=“234234@gmail.com"
toaddrs=“2342@gmail.com"
#toaddr=“23423@gmail.com"
subjectForEmail= "Details of the used cars in tucson/phoenix area you asked for"
carbonCopy = “2342@gmail.com"
bodyOfEmail="Hi,\n These are the parameters used for this query:\n\n"


#Todo:
1. attach SSH or PKI instead of typing in the pwd in raw text
2. convert to excel sheet format
3. send out alerts only if this posting hasnt been seen before.
