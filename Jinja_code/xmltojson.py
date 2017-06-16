import xmltodict, json

fp_xml = open('Output.xml', 'r')
fp_json = open('Output.json', 'w')
d = xmltodict.parse(fp_xml)
print json.dumps(d)
fp_json.write(json.dumps(d))
