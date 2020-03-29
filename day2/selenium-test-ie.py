import time

from selenium import webdriver
 
# 드라이버 파일 위치
path = "C:/programs/webdriver/IEDriverServer.exe"
 
#조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Ie(path)

#webdriver가 google 페이지에 접속하도록 명령
driver.get('https://www.google.com')

time.sleep(5)  # 크롤링 로직을 수행하기 위해 5초정도 쉬어준다.

#webdriver를 종료하여 창이 사라진다
driver.close()
