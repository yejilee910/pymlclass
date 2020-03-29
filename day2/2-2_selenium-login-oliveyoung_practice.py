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

time.sleep(3)
form = browser.find_element_by_class_name("btnArea")
# form.submit()

# browser = webdriver.Chrome()
form.click()
print("로그인 버튼을 클릭합니다.")
time.sleep(3)
print("올리브영 주문배송 조회페이지 가기")
mypage = "https://www.oliveyoung.co.kr/store/mypage/getOrderList.do"
browser.get(mypage)
print("올리브영 주문배송조회 내역 가져오기")
time.sleep(3)

file = open("oliveyoung_order_list.txt", 'w')
print("writing - oliveyoung_order_list.txt..... ")
orders = browser.find_elements_by_class_name("textus")
print(orders)
for order in orders:
    print("-", order.text)
    file.write('{0}\n'.format(order.text))
file.close()

print("reading....")
with open("oliveyoung_order_list.txt", "r") as file:
    for line in file:
        print(line.strip('\n'))

browser.quit()
