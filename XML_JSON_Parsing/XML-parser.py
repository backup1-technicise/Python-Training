from lxml import etree

tree = etree.parse('complex.XML') # parse() returns an object of ElemntTree class object, s.t lxml.etree.ElementTree()
print type(tree)

## Show the root elemnt 
print "Root tag for XML is :",tree.getroot()

## Copy XML element tree to another .xml file
tree.write('abc.xml', xml_declaration=True, encoding="UTF-8", pretty_print=True)

for element in tree.iter():
	print element, element.tag, element.attrib, element.text
print"---------------------------------------------------------------------------------"

## To know paths for each element
for element in tree.iter():
	print tree.getpath(element)
print "-------------------------------------------------------------------------------"
## Access auther 2 details from XML element tree
for element in tree.iterfind('book/author[2]/'):
	print element.tag
print"-----------------------------------------------------------"

for element in tree.findall('book/author[2]/'):
	print element.tag
print"-----------------------------------------------------------"
		
## Objective : To find a list of books with tile, category and author details
print "## Objective : To find a list of books with tile, category and author details"
for iterator in tree.getiterator():
	if iterator.tag == 'book':
		author_name = ''
		book_category = ''
		book_title = ''
		book_category += str(iterator.attrib)
		for element in iterator:
			## For book category
			if element.tag == 'title':
				book_title += element.text
			if element.tag == 'author':
				if len(element) == 0:
					author_name += element.text
				else:
					author_name += ' ' + element[0].text + ' ' + element[1].text
		print book_title,book_category,author_name

print "\n"
		
## Objective : To find a list of books with tile, category and authors who are from UK		
print "## Objective : To find a list of books with tile, category and authors who are from UK"
for iterator in tree.getiterator():
	if iterator.tag == 'book':
		author_name = ''
		book_category = ''
		book_title = ''
		## For book category
		book_category += str(iterator.attrib)
		for element in iterator:
			## For book title
			if element.tag == 'title':
				book_title += element.text
			## For book author
			if element.tag == 'author':
				if len(element) != 0 and element[2].text == 'UK':
					author_name += ' ' + element[0].text + ' ' + element[1].text
		if author_name:
			print book_title,book_category,author_name

print "\n"
## Objective : To find web technology books with tile, category and authors who are from UK		
print "## Objective : To find web technology books with tile, category and authors who are from UK	"
for iterator in tree.getiterator():
	if iterator.tag == 'book':
		author_name = ''
		book_category = ''
		book_title = ''
		## For book category
		book_category += str(iterator.attrib)
		for element in iterator:
			## For book title
			if element.tag == 'title':
				book_title += element.text
			## For book author
			if element.tag == 'author':
				if len(element) != 0 and element[2].text == 'UK':
					author_name += ' ' + element[0].text + ' ' + element[1].text
		if author_name and book_category == str({'category': 'Web technology'}):
			print book_title,book_category,author_name
