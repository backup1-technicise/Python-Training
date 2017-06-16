'''
Assignment 12 : Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
on the New York Times homepage (http://www.nytimes.com/).
This will just print out a list of all the article titles to the screen. It will not make it easy to read,
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
    for heading in soup.find_all("h2", {"class": "story-heading"}):   #heading in class ("story-heading") holds the
                                                                      # website article heading or title content
        print type(heading)
        yield heading.text  # "Shake-Up in Federal Inquiry of Eric Garner Chokehold Case" as object due to yield

    ''' For Example :            # <h2 class="story-heading">
                                    # <a href="http://www.nytimes.com/2016/10/25/nyregion/justice-dept-replaces-
                                                # investigators-on-eric-garner-case.html">
                                                # Shake-Up in Federal Inquiry of Eric Garner Chokehold Case
                                    # </a>
                                # </h2> '''''


def read_article_titles(address):
    # the syntax (according to the documentation) for how to
    # "load" a web page through Python
    page = requests.get(address)
    # how to decode the text of the HTML of the vanity fair homepage
    # website. page comes from the requests request above
    soup = BeautifulSoup(page.text, "html.parser")
    output_text = ''
    for s in getportions(soup):
        print type(s)               # Print the type of HTML Tag content
        #print "\n%s" % s.encode("utf-8")
        ''' Why to encode?
            >>> data = u'\u00c3'            # Unicode data
            >>> data = data.encode('utf8')  # encoded to UTF-8
            >>> data
            '\xc3\x83'
        '''
        output_text += s.encode("utf-8")
        output_text += "\n"
    print output_text
    print "End of article"
    fp = open("Article_title_content.txt", "w")
    fp.write(output_text)

if __name__ == "__main__":
    # the URL of the NY Times website we want to parse
    read_article_titles("http://www.nytimes.com/")
