import csv, codecs
# CSV 파일 열기
filename = "/Users/yejilee/Desktop/GitHub/pymlclass/day3/mushroom.csv"
fp = codecs.open(filename, "r", "euc_kr")
# 한 줄씩 읽어 들이기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])