import json
import sys

final_result_list = list()


def json2xml(json_obj, line_padding=""):
    json_obj_type = type(json_obj)      # Testing of JSON object, which is collection of JSON data (name/ value pair).
    if json_obj_type is dict:           # If JSON object is dictionary.
        for tag_name in json_obj:       # name part of each JSON data.
            result_list = list()
            tag_value = json_obj[tag_name]  # Value of each name.
            if tag_name == "__modelname__":
                result_list.append("<Model name = %s>" %tag_value)
                result_list.append(json2xml('</Model>', line_padding))
            else:
                result_list.append("<Field name = %s>" %tag_name)
                result_list.append(json2xml(tag_value, line_padding))
                result_list.append(json2xml('</Field>', line_padding))
            print result_list
            tag_str = " ".join(result_list)
            print tag_str
            final_result_list.append(str(tag_str))
            print final_result_list
            print "----------------------------------------------------------------------------"
            del result_list
        return "\n".join(final_result_list)

    else:
        return "%s%s" % (line_padding, json_obj)

                                            # Main namespace
print 'Number of arguments:', len(sys.argv), 'arguments.'
argv_list = sys.argv
print 'Argument List:', argv_list
print argv_list[1]
json1_file = open(str(argv_list[1]))
json1_str = json1_file.read()
print json1_str
json1_data = json.loads(json1_str)
print json1_data
XML_for_JSON = json2xml(json1_data)
print(XML_for_JSON)
out_XML_file = raw_input("Enter the output file name=")
print out_XML_file
XML1_file = open(str(out_XML_file), 'w')
XML1_file.write(XML_for_JSON)
