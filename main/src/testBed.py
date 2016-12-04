import html2text

with open(waterResults0mytext, 'wb') as f:
    myhhtml = html2text.HTML2Text()
    f.write(myhhtml.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>!")"
