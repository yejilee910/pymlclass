import requests
import json
# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요. --- (※1)
apikey = "2e6891a28eaa6f12cfb5a144ad58cbaf"

# 날씨를 확인할 도시 지정하기 --- (※2)
ids = ["1835848", "1836553", "1836553"]
# API 지정 --- (※3)
api = "http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={key}&lang={lang}"
# 켈빈 온도를 섭씨 온도로 변환하는 함수 --- (※4)


def k2c(k): return k - 273.15


# 각 도시의 정보 추출하기 --- (※5)
for id in ids:
    # API의 URL 구성하기 --- (※6)
    url = api.format(city_id=id, key=apikey, lang="kr")
    # API에 요청을 보내 데이터 추출하기
    r = requests.get(url)
    # 결과를 JSON 형식으로 변환하기 --- (※7)
    data = json.loads(r.text)
    # 결과 출력하기 --- (※8)
    print("| 도시 =", data["name"])
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 최저 기온 =", k2c(data["main"]["temp_min"]))
    print("| 최고 기온 =", k2c(data["main"]["temp_max"]))
    print("| 습도 =", data["main"]["humidity"])
    print("| 기압 =", data["main"]["pressure"])
    print("| 풍향 =", data["wind"]["deg"])
    print("| 풍속 =", data["wind"]["speed"])
    print("")

    print(data)
