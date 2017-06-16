import json

fp = open('outfile.json','r')
json_str = fp.read()
json_dict = json.loads(json_str)
print json_dict
for key,value in json_dict.iteritems():
	#print key,value
	if isinstance(key,unicode):
		key1 = str(key)
		json_dict[key1] = json_dict.pop(key)
	if isinstance(json_dict[key], list):
		for element in json_dict[key]:
			if isinstance(element,dict):
				for key,value in element.iteritems():
					if isinstance(key,unicode):
						key1 = str(key)
						element[key1] = element.pop(key)
					if isinstance(value,unicode):
						value1 = str(value)
						element[key] = value1
						
print json_dict
