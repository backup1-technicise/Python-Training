import json
import sys
import xml.etree.cElementTree as ET

								# Main namespace
print 'Number of arguments:', len(sys.argv), 'arguments.'
argv_list = sys.argv
print 'Argument List:', argv_list

json1_fp = open(str(argv_list[1]), 'r')		# Open json file in read mode.
					# Creation of name value pair from given JSON string
json1_key_order = list()	# Holds the ordering of name of fields as per given JSON file
json_key_value_dict = dict()	# Creation of name value pair as per given ordeing of fields with name in JSON file.
while True:
    line = json1_fp.readline()
    if line != '}\n' and line != '{\n':
        line = line.strip(' \t\n\r,')  # Removal of special charecters from JSON file data
        split_list = line.split(':')
        #print split_list
        if len(split_list) > 1:	       # Splilting of each JSON object in name and value
            key = split_list[0][1:len(split_list[0]) - 1] # Storing of name or KEY
            value = split_list[1][2:len(split_list[1]) - 1] # Value for name or KEY
            print key, ":", value
            json1_key_order.append(key)
            json_key_value_dict[key] = value
        del split_list
    if "" == line:
        print "file finished"
        break
print json1_key_order
print json_key_value_dict

out_XML_file = raw_input("Enter the output XML file=")  # Get the name of output XML file from user.
output_file = out_XML_file + ".xml"			# String concatenation for .xml extension
print output_file
XML1_file = open(str(output_file), 'w')

# Creation of customized schema to create XML file from user given json file data
Models = ET.Element("Models", xmlns="http://indivo.org/vocab/xml/documents#")
Model = 0
for i in range(len(json1_key_order)):
    if i == 0:
        Model = ET.SubElement(Models, "Model", name=json_key_value_dict[json1_key_order[i]])
    else:
        ET.SubElement(Model, "Field", name=json1_key_order[i]).text = json_key_value_dict[json1_key_order[i]]
tree = ET.ElementTree(Models)
tree.write(output_file)
