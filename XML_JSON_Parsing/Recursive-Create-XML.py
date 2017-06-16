from lxml import etree
# Create Simple XML
'''
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="web">
    <title lang="en">XQuery Kick Start</title>
    <author>James McGovern</author>
    <author>
		<firstname>Bothner</firstname>
		<lastname>Per</lastname>
		<country>England</country>
	</author>
    <year>2003</year>
    <price>49.99</price>
  </book>

  <book category="web" cover="paperback">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>

</bookstore>

''' 
def create_element(parent_tag):
	print "Enter child tag under parent:",parent_tag.tag
	child_tag = raw_input("Enter Child tag name: ")
	childtag = etree.SubElement(parent_tag,child_tag)
	# Have attribute for childtag
	while True:
		child_tag_attrib = raw_input("Do child tag has any attrib. ? (y/n):")
		if child_tag_attrib in ['Y','y']:
			print "Enter attribute for child tag:",childtag.tag
			attrib_name = raw_input("Enter attrib. name:")
			attrib_val = raw_input("Enter attrib. value:")
			childtag.set(attrib_name,attrib_val)
		elif child_tag_attrib in ['N','n']:
			break
	# Have text for childtag
	child_tag_text = raw_input("Do child tag has any text ? (y/n):")
	if child_tag_text in ['Y','y']:
		print "Enter text for child tag:",childtag.tag
		text_value = raw_input("Enter text:")
		childtag.text = text_value
	else:
		pass
	# Have any sub-element for childtag
	print "Do you want any sub element or tag for ",childtag.tag,
	child_tag_sub_element = raw_input("?(y/n):")
	if child_tag_sub_element in ['Y','y']:
		print "Creating sub element or tag for child tag:",childtag.tag
		create_element(childtag)
	else:
		decision = False
		while not decision:
			parent_tag = childtag.getparent()
			if parent_tag.tag == 'bookstore':
				return
			else:
				print "Will u create sub element for ",parent_tag.tag
				answer = raw_input(" ?(y/n):")
				if answer in ['Y','y']:
					print "Creating sub element or tag for child tag:",parent_tag.tag
					decision = True
				else:
					decision = False
					childtag = parent_tag
		if decision:
			create_element(parent_tag)
			
			
########## Main Namespace ##########	
bookstore = etree.Element('bookstore')
n_book = input("How many books details you enter:")
print type(n_book)
for book in range(n_book):
	create_element(bookstore)
## Show Created XML in file
serializer = etree.tostring(bookstore,pretty_print=True,xml_declaration=True,encoding="UTF-8")
fp = open('rec_xml.xml','w')
fp.write(serializer)
