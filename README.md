# CraigsList scraper for used cars

Code that gets the used car results of a given craigslist query, and converts it to text

# Description
So this is some code I wrote for a friend recently. Just sharing , just in case its useful for someone. This will automatically "keep an eye out" for anything on craigslist. That way if you want something, you dont have to consistently keep checking craigslist day in day out. As and when it shows up, this code with send you an email. Eg: used cars of a particular model/year/miles etc

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
 python scraper.py frompwd toaddr

 Eg:  python scraper.py password123 mithunpaul@gmail.com
 
 
 

#to change the parameters:
Go to scraper.py and update the variables.


#"Search Query attributes used to build the query string"
def fillSearchQueryAttributes(queryCar):
    queryCar.min_price = "1"
    queryCar.max_price ="6000"
    queryCar.auto_make_model="honda+%7C+toyota"
    queryCar.min_auto_year="2008"
    queryCar.max_auto_year="2016"
    queryCar.min_auto_miles='300'
    queryCar.max_auto_miles='150000'
    queryCar.auto_title_status='1'

#changing email parameters
Go to scraper.py and change the following

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
3. wrap it around a GUI to make noob friendly
4. make an app out of it

