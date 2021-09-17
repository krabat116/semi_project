#-*-coding utf-8-*-
import pandas as pd
import json
from pprint import *
from pandas import json_normalize
import matplotlib.pyplot as plt
import platform
import numpy as np
import csv
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font',family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family = font_name)
else:
    print('Unknown system...sorry~~')

# with open("2019 (시도) 지정폐기물 발생량(의료 제외).json",'r',encoding='utf-8') as f:
#     contents = f.read()# string 타입
#     json_data = json.loads(contents)
# print(json_data)
# print(json_data['AREA':'서울'])
#
# json_file_path = "./2019 (시도) 지정폐기물 발생량(의료 제외).json" # ㅍ일 로드
# with open(json_file_path,'r',encoding='utf-8') as j:
#     contents = json.loads(j.read())

# pprint(contents)

# df = pd.read_json('2019 (시도) 지정폐기물 발생량(의료 제외).json')
# print(df.info())
# citizen_per_person = pd.read_csv('주민_1인당_생활폐기물배출량_시도_시_군_구__20210811163628.csv',encoding="cp949")
# pprint(citizen_per_person.head())
#
# citizen_per_person = pd.read_csv('(사전정보공개)_2018._3분기_생활폐기물_월별_발생량,_1인당_발생량.csv',sep=",",encoding="cp949")
# # pprint(citizen_per_person)
# # pprint(citizen_per_person.drop('Unnamed: 0',axis=1))
# # pprint(citizen_per_person.drop(['Unnamed: 0','Unnamed: 1'],axis=1))
# citizen_per_person_2018_3=citizen_per_person.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 3','Unnamed: 4','Unnamed: 6','Unnamed: 8','Unnamed: 3'],axis=1 )
# # # citizen_per_person_2018_3=citizen_per_person.dropna()
# pprint(citizen_per_person_2018_3)
# # # df = pd.DataFrame[]
# citizen_per_person_2018_3.to_csv("test2018.csv",sep=",",index=False)
#
# data = pd.read_csv("test2018.csv")
# print('data')
# pprint(data)
# # ,columns=["구분/월","생활폐기물","음식물류폐기물","재활용","총계(톤)","1일발생량(톤)","1인1일발생량(kg)","사업장생활계폐기물(통)"]
#                   # ,index=['0','1','2','3','4','5','6','7','8']
# df = pd.DataFrame(data)
# # df.columns.name = "2018_생활폐기물_월별_1인당_발생량"
# df.columns =["구분/월","생활폐기","음식물","재활용","총계(t)","1일발생량(t)","1인1일발생량(kg)","사업장생활계폐기물(t)"]
# df.index=['0','0','0','1','2','3','0']
# df.drop(['0'],axis=0, inplace=True)
# # df.drop('구분/월',axis=1,inplace=True)
#
# # df.rename()
# # print("dfdfdsf")
# pprint(df)
# # df.to_csv("test2018_3분기.csv")
# # df.to_csv("test2018_3분기.csv",sep=",")
# # df.to_csv("test2018_3분기.csv",sep=",",index=True)
# # 0.1 2 지울려 data.reset index set . index
#
# # op =open("test2018_3분기.csv",'r',encoding='utf-8')
# # opp = csv.reader(op)
#
# data1 = pd.read_csv("test2018_3분기.csv")
# # data1.style.hide_index() 숨긴대 ~
# print("data1")
# pprint(data1)


# citizen_per_person1 = pd.read_csv('(사전정보공표)2019.4분기_생활폐기물_월별_발생량_1인당_발생량.csv',sep=",",encoding="cp949")
# citizen_per_person_2019_4=citizen_per_person1.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 3','Unnamed: 4','Unnamed: 6','Unnamed: 8','Unnamed: 3'],axis=1 )
# pprint(citizen_per_person_2019_4)
# citizen_per_person_2019_4.to_csv("test2019.csv",sep=",",index=False)
#
# data2 = pd.read_csv("test2019.csv")
# print('data2')
# pprint(data2)
# df2 = pd.DataFrame(data2)
# # df.columns.name = "2018_생활폐기물_월별_1인당_발생량"
# df2.columns =["구분/월","생활폐기","음식물","재활용","총계(t)","1일발생량(t)","1인1일발생량(kg)"]
# df2.index=['0','0','0','1','2','3','0','0','0']
# df2.drop(['0'],axis=0, inplace=True)
#
# # print("dfdfdsf")
# # pprint(df2)
# # df.to_csv("test2018_3분기.csv")
# # df.to_csv("test2018_3분기.csv",sep=",")
# df2.to_csv("test2019_4분기.csv",sep=",",index=False)
# data3= pd.read_csv("test2019_4분기.csv")
# print("data3")
# pprint(data3)
#
# '''동한이형꺼 자료 너무 방대해 '''
# # gabe_2019 = pd.read_csv("2019(시도)지정폐기물발생량(의료제외).csv",sep=",",skipfooter=40)
# # pprint(gabe_2019)
#
# citizen_per_person2 = pd.read_csv('2020_3분기_생활폐기물_월별_발생량_1인당_발생량).csv',sep=",",encoding="cp949")
# citizen_per_person_2020_3=citizen_per_person2.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 3','Unnamed: 4','Unnamed: 6','Unnamed: 8','Unnamed: 13'],axis=1 )
# print("citizen_per_person_2020_3")
# pprint(citizen_per_person_2020_3)
# citizen_per_person_2020_3.to_csv("test2020.csv",sep=",",index=False)
#
# data4 = pd.read_csv("test2020.csv")
# print('data4')
# pprint(data4)
# df3 = pd.DataFrame(data4)
# # df.columns.name = "2018_생활폐기물_월별_1인당_발생량"
# df3.columns =["구분/월","생활폐기","음식물","재활용","총계(t)","1일발생량(t)","1인1일발생량(kg)"]
# df3.index=['0','0','0','1','2','3','4','5','6','7','8','9']
# df3.drop(['0'],axis=0, inplace=True)
#
# # print("dfdfdsf")
# # pprint(df3)
# # df.to_csv("test2018_3분기.csv")
# # df.to_csv("test2018_3분기.csv",sep=",")
# df3.to_csv("test2020_123분기.csv",sep=",",index=False)
# data3= pd.read_csv("test2020_123분기.csv")
# print("2020_123")
# pprint(data3)
#
#
#
# ac18=pd.read_csv("주민_1인당_생활폐기물배출량_시도_시_군_구__20210811163628.csv",encoding="cp949")
# print("ac18")
# pprint(ac18)
#
# ac19 = pd.read_csv("한국환경공단_지자체별 RFID음식물쓰레기 배출량_20200731.csv",encoding="cp949")
# ac19=ac19[ac19.배출연도>2017]
# ac19=ac19[ac19.광역시도=='서울특별시']
# ac19=ac19[ac19.기초지자체=='강남구']
# ac19=ac19[((ac19.배출월>3)&(ac19.배출월<7))]
#
# pprint(ac19)
# # # dq1 = pd.DataFrame(ac19)
# # # # pprint(dq1)
# # # mask = dq1['배출연도'] == '2018',
# # # print(mask)
# #
# # # ac = ac19["배출연도"]=='2018'
# # # qq = df[ac]
# # # pprint(qq)
''' 주민 1인당 생활폐기물 배출량 시도 시 군 구 20210811.csv '''
# df = pd.read_csv("주민_1인당_생활폐기물배출량_시도_시_군_구__20210811163628.csv",encoding='cp949')
# # df = df[df.행정구역별=='서울특별시']
# pprint(df)

''' 2018 3 분기 2019 4 분기 2020 123 분기 병함 '''
df2018_1 = pd.read_csv('test2018_3분기.csv',sep=",")
df2019_1 = pd.read_csv('test2019_4분기.csv',sep=",")
df2020_1 = pd.read_csv('test2020_123분기.csv',sep=",")

df2018 = pd.DataFrame(df2018_1)
# df2018.drop()
# df2018.drop(['Unnamed: 0','구분/월'],axis= 1 ,inplace= True)
df2019 = pd.DataFrame(df2019_1)
df2020 = pd.DataFrame(df2020_1)

result = pd.concat([df2018,df2019,df2020],ignore_index=True)
result.drop('Unnamed: 0',axis= 1 ,inplace= True)
result['구분/월']=['18-07','18-08','18-09',
                 '19-10','19-11','19-12',
                 '20-01','20-02','20-03',
                 '20-04','20-05','20-06',
                 '20-07','20-08','20-09']
pprint(result)

# result.to_csv("2018_2019_2020_종합.csv",index=False)
# qwer= pd.read_csv("2018_2019_2020_종합.csv")
# result1=result.drop('사업장생활폐기물(t)',axis=1)
result1 = result.dropna(how='any')
ba_2018_3 = result1['생활폐기'][:3]
# ba_2018_3_1per = result['1인비일발생량(kg)'][0:3]
# ba_2019_4_1per = result['1인비일발생량(kg)'][3:6]
# ba_2020_1_1per = result['1인비일발생량(kg)'][6:9]
# ba_2020_2_1per = result['1인비일발생량(kg)'][9:12]
# ba_2020_3_1per = result['1인비일발생량(kg)'][12:15]

# pprint(ba_2018_3)
# ba_2018_3.plot()

result1['생활폐기'][:3].plot.bar(rot=0)
plt.xlabel('구분/월')
plt.title("20183분기_20194분기_20201~3분기")
# result1.transpose().plot(kind = 'bar')
result1.plot()
result1.plot(kind = 'bar')
# result.plot(kind = 'barh')
plt.show()