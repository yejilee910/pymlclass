import requests

#GET요청
r = requests.get("http://www.google.com")

#POST요청
formdata = {  "key1" : "value1" , "key2" : "value2" }
r = requests.post("http://example.com" , data = formdata)

# r = requests.get("http://api.aoikujira.com/time/get.php")
# text = r.text
# print(text)

# bin = r.content
# print(bin)