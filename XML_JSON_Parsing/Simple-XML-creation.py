from lxml import etree
# Create Simple XML with XML declaration and encoding
'''
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="web">
    <title lang="en">XQuery Kick Start</title>
    <author>James McGovern</author>
    <year>2003</year>
    <price>49.99</price>
  </book>
</bookstore>
'''

########## Main Namespace ##########

	
bookstore = etree.Element('bookstore')

bookstore.append(etree.Comment('Bookstrore with web technology books'))

book = etree.SubElement(bookstore,'book')
book.set('category','web')

book_title = etree.SubElement(book,'title')
book_title.set('lang','en')
book_title.text='XQuery Kick Start'

book_author = etree.SubElement(book,'author')
book_author.text='James McGovern'

book_year = etree.SubElement(book,'year')
book_year.text='2003'

book_price = etree.SubElement(book,'price')
book_price.text='49.99'


## Show Created XML
serialized_object = etree.tostring(bookstore, xml_declaration=True, encoding="UTF-8", pretty_print=True) 
print serialized_object
fp = open('simple.xml','w')
fp.write(serialized_object)

# XML Element tree iteration
for element in bookstore.iter():
	print "element tag:", element.tag
	print "element type", type(element.tag)
	print "element parent:",element.getparent()
	print "element attribute:", element.attrib
	print "element text:", element.text
	print "-----------------------------------------------------------------------"
	
## print only elements of str type
print "################## Only string type element:"
for element in bookstore.iter():
	if isinstance(element.tag,str):
		print "element tag:", element.tag
		print "element type", type(element.tag)
		print "element parent:",element.getparent()
		print "element attribute:", element.attrib
		print "element text:", element.text
		print "-----------------------------------------------------------------------"
