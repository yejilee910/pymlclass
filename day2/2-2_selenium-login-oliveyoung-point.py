import time
from selenium import webdriver
from bs4 import BeautifulSoup


path = "./chromedriver"
driver = webdriver.Chrome(path)

options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome('./chromedriver', chrome_options=options)

browser = webdriver.Chrome("./chromedriver")

USER = "<아이디>"
PASS = "<비밀번호>"

url_login = "https://www.oliveyoung.co.kr/store/login/loginForm.do"
browser.get(url_login)
print("올리브영 로그인 페이지에 접근합니다.")

USER = "sapienche"
PASS = "choco1004"

e = browser.find_element_by_id("loginId")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("password")
e.clear()
e.send_keys(PASS)

time.sleep(1)
form = browser.find_element_by_class_name("btnArea")
# form.submit()

# browser = webdriver.Chrome()
form.click()
print("로그인 버튼을 클릭합니다.")
time.sleep(1)

point_url = "https://www.oliveyoung.co.kr/store/mypage/myPageMain.do"
browser.get(point_url)
print("마이페이지에 접근합니다.")
# p = browser.find_element_by_css_selector("point-cjone")
# point = browser.value_of_css_property("cjOnePointInfo")
# point = browser.find_element_by_name("#text")
# point = browser.find_element_by_class_name(point-cjone)

try:
    points = browser.find_element_by_css_selector("a.num")
except AttributeError as error:
    browser.quit()

points_data = points.text
print(points_data)

file = open("olive_point.txt", "w")
print("writing....")
file.write(points_data)
file.close()

time.sleep(3)
print("브라우저를 종료합니다")
browser.quit()
