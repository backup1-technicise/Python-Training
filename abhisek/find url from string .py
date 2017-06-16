import re
text = '<p>Contents :</p><a href="http://w3resource.com">Python Examples</a><a href="https://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://[\w]+\.[a-z]+', text)
print("original string:", text)
print("Urls: ", urls)
