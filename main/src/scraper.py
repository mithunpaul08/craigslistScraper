#changes included in this version
#1.1 download and save html files from the first one results---done
#1.2 download and save html files from the first ten results----done
#1.3 download html files from the first ten results---done
#2. convert first 10 html results to text and save them---done
#3. download pdf files from the first ten results--done
#4. convert the pdf files into txt and save them---done
#5. create a folder structure

import requests, bs4, sys, webbrowser, html2text, os , PyPDF2, urllib2

# encoding=utf8
# the html file written by beautifulsoup4 wasnt getting parsed by html2text.
#So converted it to default utf8 encoding

import sys

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
queryStringStub='http://tucson.craigslist.org/search/cto?sort=priceasc&min_price=1&max_price=6000&auto_make_model=honda+%7C+toyota&min_auto_year=2001&max_auto_year=2016&min_auto_miles=300&max_auto_miles=110000&auto_title_status=1'
numberOfGoogleResults=1000
startValue=1
stubUrlForTucsonCLInnerpages='http://tucson.craigslist.org/'
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


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
        #urrlib2 is a version of beautiful soup that raises a http request for you
        url = urllib2.urlopen(myQS)
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
                        #print(linkToNextPage)
                        childurl=stubUrlForTucsonCLInnerpages+linkToNextPage
                        #once you get the link, open and go into that page.
                        try:
                            url = urllib2.urlopen(childurl)
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
                            if(content != None):
                            # parse the content into a format that soup understands
                                childSoup = bs4.BeautifulSoup(content, "lxml")
                                #print childSoup
                                #print "done child data"

                                #to find the attributes of the car, which is inside <div class="mapAndAttrs">

                                #find all div tags

                                listOfSpanValues = []
                                carAttributes="";

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
                                        individualCarDetails=str(listOfSpanValues)
                                        print individualCarDetails
                                        listOfCars.append(individualCarDetails)

        print str(listOfCars)
                         # Extract the details you want. add it to a global buffer or something
                        #get
       # else:
         #       print "no class"
            #print "found a title and its hyperlink value is" + res;


        # get all the hyperlinks in the given page.
        #linkElems = soup.findAll("a")


    except:
        print "exception occured"+ sys.exc_info()[0]

    else:
        print "finished"
        sys.exit(1)
       # soup = bs4.BeautifulSoup(res.text,"lxml")
        #linkElems = soup.select('.r a')
        #writeToOutputFile(linkElems)
        #get the length of the total number of links
        numOpen = len(linkElems)
        print 'value of  numOpen is ' + `numOpen`
        #sys.exit(1)
        for i in range(numOpen):
            try:
                #find if href has .pdf in it
                #filenameCounter=i+startValue
                print linkElems[i]
                sys.exit(1)
                classResult = linkElems[i].get('class')
                if ("result-title" in classResult):
                    #res = requests.get(linkElems[i].get('href'))
                    print "found a title and its hyperlink value is" + res;
                else:
                    continue;
                try:
                    res = requests.get(linkElems[i].get('href'))
                    res.raise_for_status()
                except:
                    print "exception occured"
                          #+ `e.response.status_code`


                else:
                    #create a unique file name to store each of the results
                    combinedFileName=stubFilename +`filenameCounter`
                    waterResultFile = open(combinedFileName, 'wb+')
                    for chunk in res.iter_content(100000):
                        waterResultFile.write(chunk)
                    waterResultFile.close()
                    hrefValue=linkElems[i].get('href')

                    if(hrefValue.find('.pdf')>0):
                        print 'file number ' + `filenameCounter`+  ' is a pdf file'
                        os.rename(combinedFileName,combinedFileName+'.pdf')
                        pdfFileObj = open(combinedFileName+'.pdf', 'rb')
                        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                        pageObj = pdfReader.getPage(0)
                        extractedText=pageObj.extractText()

                        for i in xrange(pdfReader.getNumPages()):
                            pageObj = pdfReader.getPage(i)
                            extractedText=extractedText+pageObj.extractText()

                        #remove the file if it already exists
                        try:
                            os.remove(combinedFileName+'InTxtFormat.txt')
                        except OSError:
                            pass

                        #write the extracted text from pdf document to a txt file
                        target = open(combinedFileName+'InTxtFormat.txt', 'w')
                        target.write(extractedText)
                        target.close()
                    else:
                        #if file is html or txt
                        print'file number ' + `filenameCounter`+  ' is not a pdf file'

                        #get the unicode converted file and rename it as html
                        os.rename(combinedFileName,combinedFileName+'.html')

                        #read into an html handle
                        #myhtml = open(outputDirectory+combinedFileName+".html").read()
                        myhtml = open(combinedFileName+".html").read()

                        #remove the file if it already exists
                        try:
                            #os.remove(outputDirectory+combinedFileName+'InTxtFormat.txt')
                            os.remove(combinedFileName+'InTxtFormat.txt')
                        except OSError:
                            pass

                        #ignore links
                        h = html2text.HTML2Text()
                        h.ignore_links = True

                        convertedText=h.handle(myhtml.encode('utf-8').strip())

                        # #write the converted text to a txt file
                        #target = open(outputDirectory+combinedFileName+'InTxtFormat.txt', 'w')
                        target = open(combinedFileName+'InTxtFormat.txt', 'w')
                        target.write(html2text.html2text(convertedText).encode('utf-8'))
                        target.close()
            except:
                print "Exception occured in the entire function"
                continue


            #see if you can raise more than 10 google results
#for gCounter in my_range (startValue,numberOfGoogleResults,10):
#start =gCounter

queryString=queryStringStub
parseGResults(queryString)
 
