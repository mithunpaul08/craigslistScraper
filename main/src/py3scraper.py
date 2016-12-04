#changes included in this version
#1.1 download and save html files from the first one results---done
#1.2 download and save html files from the first ten results----done
#1.3 download html files from the first ten results---done
#2. convert first 10 html results to text and save them---done
#3. download pdf files from the first ten results--done
#4. convert the pdf files into txt and save them---done
#5. create a folder structure

import requests, bs4, sys, webbrowser, html2text, os , PyPDF2

# encoding=utf8
# the html file written by beautifulsoup4 wasnt getting parsed by html2text.
#So converted it to default utf8 encoding

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#print os.getcwd()
os.chdir('../../outputs/')
#print os.getcwd()
#exit()
#various typical requests
#todo: add into a string array and call ?
#res = requests.get('https://www.google.com/search?q=pests+diseases+tamil+nadu+agriculture')
stubFilename='farmSize'
#res = requests.get('https://www.google.com/search?q=soil+degradation+tamil+nadu+agriculture')
#res = requests.get('https://www.google.com/search?q=farm+sizes+tamil+nadu+agriculture')
res = requests.get('https://www.google.com/search?q=%22farm+size%22+tamil+nadu+agriculture+&start=1&num=10')
#https://www.google.com/search?q=%22farm+size%22+tamil+nadu+agriculture+&start=1&num=10

numberOfGoogleResults=1000
startValue=205

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


def parseGResults(myQS,startValue):

    print("value of query string is"+ myQS)
    try:
        res = requests.get(myQS)
        res.raise_for_status()

    except requests.HTTPError as e:
        print("exception occured"+ e.response.status_code)
    else:
        soup = bs4.BeautifulSoup(res.text,"lxml")
        linkElems = soup.select('.r a')
        numOpen = min(numberOfGoogleResults, len(linkElems))
        print('value of  numOpen is ' + numOpen)

        for i in range(numOpen):
            try:
                #find if href has .pdf in it
                filenameCounter=i+startValue
                try:
                    res = requests.get('http://google.com' + linkElems[i].get('href'))
                    res.raise_for_status()
                except requests.HTTPError as e:
                    print ("exception occured"+ e.response.status_code)


                else:
                    #create a unique file name to store each of the results
                    combinedFileName=stubFilename +filenameCounter
                    waterResultFile = open(combinedFileName, 'wb+')
                    for chunk in res.iter_content(100000):
                        waterResultFile.write(chunk)
                    waterResultFile.close()
                    hrefValue=linkElems[i].get('href')

                    if(hrefValue.find('.pdf')>0):
                        print('file number ' + filenameCounter+  ' is a pdf file')
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
                        print('file number ' + filenameCounter+  ' is not a pdf file')

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
                print("Exception occured in the entire function")
                continue



#see if you can raise more than 10 google results
for gCounter in my_range (startValue,numberOfGoogleResults,10):
    start =gCounter
    print(start)
    queryString="https://www.google.com/search?q=%22farm+size%22+tamil+nadu+agriculture+"+"&start="+start+"&num=10"
    parseGResults(queryString,start)
 
