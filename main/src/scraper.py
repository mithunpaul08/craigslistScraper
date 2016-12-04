#changes included in this version
#1.1 download and save html files from the first one results---done
#1.2 download and save html files from the first ten results----done
#1.3 download html files from the first ten results---done
#2. convert first 10 html results to text and save them---done
#3. download pdf files from the first ten results--done
#4. convert the pdf files into txt and save them---done
#5. create a folder structure

import requests, bs4, sys, webbrowser, html2text, os , PyPDF2, urllib2, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# encoding=utf8
# the html file written by beautifulsoup4 wasnt getting parsed by html2text.
#So converted it to default utf8 encoding


#uncomment these 2 lines of code if you get the below error. Some unicode encoding stuff
#UnicodeEncodeError: 'ascii' codec can't encode character u'\ufeff' in position 0: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding('utf8')

#print os.getcwd()
os.chdir('../../outputs/')
#print os.getcwd()
#exit()
#various typical requests
#todo: add into a string array and call ?
#res = requests.get('https://www.google.com/search?q=pests+diseases+tamil+nadu+agriculture')

#res = requests.get('https://www.google.com/search?q=soil+degradation+tamil+nadu+agriculture')
#res = requests.get('https://www.google.com/search?q=farm+sizes+tamil+nadu+agriculture')
#res = requests.get('https://www.google.com/search?q=%22farm+size%22+tamil+nadu+agriculture+&start=1&num=10')
#https://www.google.com/search?q=%22farm+size%22+tamil+nadu+agriculture+&start=1&num=10
#ideal query:res = requests.get('https://www.google.com/search?q=%22farm+size%22+tamil+nadu+agriculture+&start=1&num=10')
#				https://www.google.com/search?q=%22pests+diseases%22+tamil+nadu+agriculture+&start=41&num=10

stubFilename='rawOutputs'
queryStringStubForTucson='http://tucson.craigslist.org/search/cto?'
actualQueryString='http://tucson.craigslist.org/search/cto?sort=priceasc&min_price=1&max_price=6000&auto_make_model=honda+%7C+toyota&min_auto_year=2001&max_auto_year=2016&min_auto_miles=300&max_auto_miles=110000&auto_title_status=1'
numberOfGoogleResults=1000
startValue=1
stubUrlForTucsonCLInnerpages='http://tucson.craigslist.org/'
stubUrlForPhxCLInnerpages='http://phoenix.craigslist.org/'
gmailUsername="saf@gmail.com"
gmailPwd="sfasd"
fromaddr="adf@gmail.com"
toaddrs="asdf@gmail.com"
#toaddr="mithunpaul08@gmail.com"
subjectForEmail= "Details of the used cars in tucson/phoenix area you asked for"
carbonCopy = "asfa@gmail.com"
bodyOfEmail="Hi,\n These are the parameters used for this query:\n\n"

class myCar:
    min_price = ""
    max_price =""
    auto_make_model=""
    min_auto_year=""
    max_auto_year=""
    min_auto_miles=''
    max_auto_miles=''
    auto_title_status=''



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

def createQueryObject(queryStringStubToBuild, carObject):
    queryStringToSearch = str(queryStringStubToBuild)+"sort=priceasc&min_price="+carObject.min_price+\
                          "&max_price="+carObject.max_price+\
                          "&auto_make_model="+carObject.auto_make_model+\
                            "&min_auto_year="+carObject.min_auto_year+\
                                             "&max_auto_year="+carObject.max_auto_year+\
                                             "&min_auto_miles="+carObject.min_auto_miles+\
                                             "&max_auto_miles="+carObject.max_auto_miles+\
                                             "&auto_title_status="+carObject.auto_title_status
    return queryStringToSearch

def sendEmail(queryResults,carObject):
    bodyWithQueryDetails=createQueryObject(bodyOfEmail,carObject);
    bodyWithQueryDetailsreplacedAmbersand=bodyWithQueryDetails.replace("&", "\n")
    finalMessageToSend=bodyWithQueryDetailsreplacedAmbersand+"\n \nAnd the results are as follows:\n\n"+queryResults
    print("getting here at 32423")

    msg = "\r\n".join([
        "From: "+fromaddr,
        "To: " + toaddr,
        "Cc: " + carbonCopy,
        "Subject:"+subjectForEmail,
        "",
        finalMessageToSend
    ])

    server = smtplib.SMTP('smtp.gmail.com:587')
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmailUsername, gmailPwd)
    #print(fromaddr)
    #print(toaddr)
    #print(msg)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print("done sending email")

def buildMessageBody(carObjectToBuildQuery):
    bodyOfEmail = "Hi, the details used for this query are as follows:"+carObjectToBuildQuery



def writeToOutputFile(textToWrite):
     # #write the converted text to a txt file
    #target = open(outputDirectory+combinedFileName+'InTxtFormat.txt', 'w')
    target = open(stubFilename+'.txt', 'w')
     #if you get this error: TypeError: expected a character buffer object
    target.write(html2text.html2text(textToWrite).encode('utf-8'))
    #target.write(textToWrite)
    target.close()


def parseGResults(myQS):
    try:

        carObjectToBuildQuery = myCar()
        fillSearchQueryAttributes(carObjectToBuildQuery)
        queryStringToSearch=createQueryObject(queryStringStubForTucson,carObjectToBuildQuery)
        #urrlib2 is a version of beautiful soup that raises a http request for you
        try:
            url = urllib2.urlopen(queryStringToSearch)
        except urllib2.HTTPError, e:
            print('HTTPError = ' + str(e.code))
        except urllib2.URLError, e:
            print('URLError = ' + str(e.reason))
        except httplib.HTTPException, e:
            print('HTTPException')
        except Exception:
            import traceback
            print('generic exception: ' + traceback.format_exc())
        else:
            content = url.read()
            #parse the content into a format that soup understands
            soup = bs4.BeautifulSoup(content,"lxml")
            listOfCars = []
            #for each of the hyperlinks in the page
            for link in soup.find_all('a'):
                # get class of the link. In craigslist result, actual hyperlinks of results are in the :class="result-title hdrlnk"
                classResult = link.get('class')
                if (classResult != None):
                    if ("result-title" in classResult):
                        #print(link.get('class'))
                        #if the class exists, get the link, if its not null
                        linkToNextPage = link.get('href')
                        if (linkToNextPage != None):
                            print("\n")
                            childurl = stubUrlForTucsonCLInnerpages + linkToNextPage
                            #print(linkToNextPage)
                            if("phoenix" in linkToNextPage):
                                childurl = "http:" + linkToNextPage

                            #once you get the link, open and go into that page.
                            try:
                                secondChildurl = urllib2.urlopen(childurl)
                            except urllib2.HTTPError, e:
                                print('HTTPError = ' + str(e.code))
                            except urllib2.URLError, e:
                                print('URLError = ' + str(e.reason))
                            except httplib.HTTPException, e:
                                print('HTTPException')
                            except Exception:
                                import traceback
                                print('generic exception: ' + traceback.format_exc())
                            else:
                                content = secondChildurl.read()
                                if(content != None):
                                # parse the content into a format that soup understands
                                    childSoup = bs4.BeautifulSoup(content, "lxml")
                                    #print childSoup
                                    #print "done child data"

                                    #to find the attributes of the car, which is inside <div class="mapAndAttrs">

                                    #find all div tags

                                    listOfSpanValues = []

                                    individualCarDetails = ""

                                    carTitleSpan = childSoup.find("span", {"id": "titletextonly"})
                                    if(carTitleSpan!=None):
                                        carTitle = "Name:"+carTitleSpan.text+"\n"
                                        individualCarDetails+=carTitle


                                    carPriceSpan = childSoup.find("span", {"class": "price"})
                                    if (carPriceSpan != None):
                                        carPrice= "Price:"+carPriceSpan.text+"\n"
                                        individualCarDetails+=carPrice


                                    myDivTags=childSoup.find_all("div", {"class": "mapAndAttrs"})
                                    for individualDivs in myDivTags:
                                        if(len(individualDivs.find_all('span'))!=0):
                                            for spanElements in individualDivs.find_all('span'):
                                                mySpanElementText=str(spanElements.text)
                                                #print spanElements.text
                                                #carAttributes= carAttributes+mySpanElementText
                                                listOfSpanValues.append(mySpanElementText)
                                            #carAttributes=String.join(listOfSpanValues, '')
                                            #print carAttributes
                                            individualCarDetails=individualCarDetails+str(listOfSpanValues)
                                            print individualCarDetails
                                            print childurl
                                            #print individualCarDetails
                                            #sys.exit(1)
                                            urlToThisCar="Link To This Car:"+childurl
                                            listOfCars.append(individualCarDetails)
                                            listOfCars.append(str(urlToThisCar))

            finalListOfCars = "\n\n".join(listOfCars)
            sendEmail(finalListOfCars,carObjectToBuildQuery)
    except:
        print('generic exception: ')
        #+sys.exc_info()[0])




parseGResults(actualQueryString)
 
