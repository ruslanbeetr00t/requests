import requests
city = input('pleas write here you are city name')
city_name = city.title()
print(type(city_name))
leng_city = input("pleas use code you are languiges")
leng = f"&lang={leng_city}"
print(type(leng))
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
API_key = "31fead8e632bd3aa65668d5c9af84f3d"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}{leng}"


def main():
    responce = requests.get(url, headers=headers)
    print(responce.status_code)
    print(responce.json())


if __name__ == "__main__":
    main()
