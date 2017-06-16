import json
import xmltodict

fp = open('complex.XML','r')
## fp.read() read the XML file content as string
xml_str = fp.read()
print xml_str
print type(xml_str)

## xmltodict.parse converts the string content to python dictionary
xml_dict = xmltodict.parse(xml_str)
print xml_dict
print type(xml_dict)
print "----------------------------------------------------------------------"

## json.dumps() creates json string from python dictionary
json_str = json.dumps(xml_dict)
print json_str
print type(json_str)
print "----------------------------------------------------------------------"

## json.loads() creates json string from python dictionary
json_dict = json.loads(json_str)
print json_dict
print type(json_dict)
print "----------------------------------------------------------------------"

						## try to achieve same objectives as XML parsing
## Objective : To find a list of books with tile, category and author details
print "\n"
print "## Objective : To find a list of books with tile, category and author details"
print "\n",
for book_entry in json_dict[u'bookstore'][u'book']:
	author_name = ''
	book_category = ''
	book_title = ''
	#print book_entry

	book_category += book_entry[u'@category']
	book_title += book_entry[u'title'][u'#text']
	if isinstance(book_entry[u'author'],list):
		author_name += book_entry[u'author'][0] + ' and ' + book_entry[u'author'][1][u'firstname'] + ' ' + book_entry[u'author'][1][u'lastname']
	elif isinstance(book_entry[u'author'],dict):
		author_name += book_entry[u'author'][u'firstname'] + ' ' + book_entry[u'author'][u'lastname']
	print book_category,book_title,author_name

## Objective : To find a list of books with tile, category and authors who are from UK	
print "\n"	
print "## Objective : To find a list of books with tile, category and authors who are from UK"
print "\n"
for book_entry in json_dict[u'bookstore'][u'book']:
	author_name = ''
	book_category = ''
	book_title = ''
	#print book_entry

	book_category += book_entry[u'@category']
	book_title += book_entry[u'title'][u'#text']
	if isinstance(book_entry[u'author'],list):
		if book_entry[u'author'][1][u'country'] == 'UK':
			author_name += book_entry[u'author'][0] + ' and ' + book_entry[u'author'][1][u'firstname'] + ' ' + book_entry[u'author'][1][u'lastname']
	elif isinstance(book_entry[u'author'],dict):
		if book_entry[u'author'][u'country'] == 'UK':
			author_name += book_entry[u'author'][u'firstname'] + ' ' + book_entry[u'author'][u'lastname']
	if author_name:
		print book_category,book_title,author_name
		
## Objective : To find web technology books with tile, category and authors who are from UK		
print "\n"
print "## Objective : To find web technology books with tile, category and authors who are from UK	"
print "\n"
for book_entry in json_dict[u'bookstore'][u'book']:
	author_name = ''
	book_category = ''
	book_title = ''
	#print book_entry

	book_category += book_entry[u'@category']
	book_title += book_entry[u'title'][u'#text']
	if isinstance(book_entry[u'author'],list):
		if book_entry[u'author'][1][u'country'] == 'UK':
			author_name += book_entry[u'author'][0] + ' and ' + book_entry[u'author'][1][u'firstname'] + ' ' + book_entry[u'author'][1][u'lastname']
	elif isinstance(book_entry[u'author'],dict):
		if book_entry[u'author'][u'country'] == 'UK':
			author_name += book_entry[u'author'][u'firstname'] + ' ' + book_entry[u'author'][u'lastname']
	if author_name and book_category == 'Web technology':
		print book_category,book_title,author_name
