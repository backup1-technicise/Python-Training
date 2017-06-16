import json
import sys
import xml.etree.cElementTree as ET

json1_file = open(str(argv_list[1]), 'r')
json1_str = json1_file.read()
print json1_str
json1_data = json.loads(json1_str)


json1_fp = open('json1.json', 'r')
json1_key_order = list()
json_key_value_dict = dict()
while True:
    line = json1_fp.readline()
    if line != '}\n' and line != '{\n':
        line = line.strip(' \t\n\r,')
        split_list = line.split(':')
        #print split_list
        if len(split_list) > 1:
            key = split_list[0][1:len(split_list[0]) - 1]
            value = split_list[1][2:len(split_list[1]) - 1]
            print key, value
            json1_key_order.append(key)
            json_key_value_dict[key] = value
        del split_list
    if "" == line:
        print "file finished"
        break
print json1_key_order
print json_key_value_dict

out_XML_file = raw_input("Enter the output XML file=")
output_file = out_XML_file + ".xml"
print output_file
XML1_file = open(str(output_file), 'w')

					# Creation of user defined schema for user given XML file from given json data

Models = ET.Element("Models", xmlns="http://indivo.org/vocab/xml/documents#")
Model = 0
for i in range(len(json1_key_order)):
    if i == 0:
        Model = ET.SubElement(Models, "Model", name=json_key_value_dict[json1_key_order[i]])
    else:
        ET.SubElement(Model, "Field", name=json1_key_order[i]).text = json_key_value_dict[json1_key_order[i]]
tree = ET.ElementTree(Models)
tree.write(output_file)
