import urllib.request as req
import os.path
os.chdir("./day3")
local = "mushroom.csv"
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)
print("ok")
