
# coding: utf-8

# In[1]:



# 定义字典

weather_dic = {}
history_dic = {}

# 读取文件，内容存入字典
with open('C:\\Users\\admin\\test\\weather_info.txt','r', encoding='utf-8') as file:
    for info in file.readlines():
        city = info.split(',')[0]
        weather = info.split(',')[1].rstrip('\n')
        weather_dic[city] = weather


while True:
    order = input('请输入指令或您要查明的城市名：')
    # 查询城市天气，并将查询结果存入字典
    if order in weather_dic.keys():
        weather = weather_dic[order]
        history_dic[order] = weather # 保存查询结果
        print('{}天气的状况为:{}'.format(order, weather))

    # 查询帮助信息
    elif order in ['h', 'help']:
        print(
            '''
            输入城市名，查询该城市的天气；
            输入help，查获帮助文档；
            输入history，获取查询历史；
            输入quit，退出天气查询系统。
          '''
        )

    # 查询历史纪录
    elif order in ['history']:
        for order in history_dic:
          print(order,history_dic[order])

     # 返回历史纪录，退出程序
    elif order in ['quit', 'q']:
        print("显示查询结果，退出程序！")
        for order in history_dic:
            print(order, history_dic[order])
        break

    else:
        print('没有该城市信息！请输入help查看帮助文档。')


# In[ ]:



