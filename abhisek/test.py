'''
Assignment 11 : Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article
on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you
can read the full article without having to click any buttons.

This will just print the full text of the article to the screen. It will not make it easy to read,
so next exercise we will learn how to write this text to a .txt file.
'''

# import the requests Python library for programmatically making HTTP requests
# after installing it according to these instructions:
# http://docs.python-requests.org/en/latest/user/install/#install
import requests
# import the BeautifulSoup Python library according to these instructions:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
# use this syntax as described on the documentation page:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
from bs4 import BeautifulSoup

def getportions(soup):
    title = soup.find("h1", {"class": "hed"})  # Content under class = "hed" and header <h1> tag .
    heading = soup.find("div", {"class": "dek"})  # # Content under class = "dek" and header <div> tag .
    if title:
        print type(title)
        yield title.text
    if heading:
        print type(heading)
        yield heading.text
    for p in soup.find_all("p", {"class": ""}):   # p is a paragraph. p in any class ("") holds the website content
        print type(p)
        yield p.text


def readpage(address):
    # the syntax (according to the documentation) for how to
    # "load" a webpage through Python
    page = requests.get(address)
    # how to decode the text of the HTML of the vanity fair homepage
    # website. page comes from the requests request above
    soup = BeautifulSoup(page.text, "html.parser")
    output_text = ''
    for s in getportions(soup):
        print type(s)
        #print "\n%s" % s.encode("utf-8")
        output_text += s.encode("utf-8")
        output_text += "\n"
    print output_text
    print "End of article"
    fp = open("Output_web_content", "w")
    fp.write(output_text)

if __name__ == "__main__":
    # the URL of the NY Times website we want to parse
    readpage("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
