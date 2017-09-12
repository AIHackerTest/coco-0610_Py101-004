# -*- coding:utf-8 -*-
import requests
import sys

history_dict = []

# 调用天气信息
def fetchweather(city):
    url =" http://v.juhe.cn/weather/index?format=2&cityname=%s&key=0fa0e566c7b5ddf62bc711ffc42f4b54" % city
    #print(url)
    f = requests.get(url)
    weather_dict = f.json()
    return weather_dict

# 天气信息输出给用户

def show_weather(weather_dict):
    result = weather_dict['result']
    #print(result.keys())
    #print(result)
    shishi = result['sk']
    time = shishi['time']
    today = result['today']
    city = today['city']
    date = today['date_y']
    week = today['week']
    wind = shishi['wind_direction']
    temp = shishi['temp']
    weather = today['weather']
    user_wather = city + "的天气：" + weather + "风力：" + wind + "温度：" + temp + "摄氏度" + time + week + date
    print(user_wather)
    #print()
    #history_dict.append(user_wather)


def play():
    while True:
        try:
            users_city = str(input("请输入您要查询的城市名："))
            result = fetchweather(users_city)
            show_weather(result)
        except:
            if users_city in ['h', 'help']:
                print(
                    """
                    输入正确的城市名，查询所需城市天气状况；
                    输入help，获得帮助文档；
                    输入history,获得历史查询记录；
                    输入quit，退出程序。
                    """
                )
            elif users_city == 'history':
                for users_city in history_dict:
                    print(history_dict)
            elif users_city in ['quit', 'exit']:
                print('已退出！')
                exit()
            else:
                print("请输入正确的查询信息！或输入help获得帮助文档。")

play()

