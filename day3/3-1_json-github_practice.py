import urllib.request as req
import os.path
import random
import json

url = "https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

s = open(savename, "r", encoding="utf-8").read()
items = json.loads(s)
print(items)
exit()


# items = json.load(open(savename, "r", encoding='utf-8'))

# for item in items:
#     print(item["name"] + " - " + item["owner"]["login"])
#     if item["owner"]["site_admin"] == False:
#         print("non_admin")
#     else:
#         print("Admin user")
