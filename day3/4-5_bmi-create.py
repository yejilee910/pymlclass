import random

import glob
import os.path
import re
import json
# print('cwd: '+ os.getcwd())
os.chdir('./day3')

# BMI를 계산해서 레이블을 리턴하는 함수


def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5:
        return "thin"
    if bmi < 25:
        return "normal"
    return "fat"


# 출력 파일 준비하기
fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\r\n")

# 무작위로 데이터 생성하기
cnt = {"thin": 0, "normal": 0, "fat": 0}
total = 40000
for i in range(total):
    h = random.randint(140, 190)
    w = random.randint(40, 80)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\n".format(h, w, label))
fp.close()
print("ok,", cnt)
thin_portion = int((cnt["thin"] / total) * 100)
normal_portion = int((cnt["normal"] / total) * 100)
fat_portion = int((cnt["fat"] / total) * 100)
print("저체중 비중 :", thin_portion, "%")
print("정상 비중 :", normal_portion, "%")
print("과체중 비중 :", fat_portion, "%")
