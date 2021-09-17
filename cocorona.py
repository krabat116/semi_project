#-*-coding utf-8-*-
import pandas as pd
from pprint import *
import matplotlib.pyplot as plt
import platform
import numpy as np
import csv
import matplotlib
from matplotlib import font_manager, rc
import missingno as msno

plt.rcParams['axes.unicode_minus'] = False

# plt.rcParams['font.size']=12
# plt.reParams['figure.figsize']=(4,3)

if platform.system() == 'Darwin':
    rc('font',family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family = font_name)
else:
    print('Unknown system...sorry~~')

''' 2018 3 분기 2019 4 분기 2020 123 분기 병함 데이터 전처리 '''

df2018_1 = pd.read_csv('test2018_3분기.csv',sep=",")
df2019_1 = pd.read_csv('test2019_4분기.csv',sep=",")
df2020_1 = pd.read_csv('test2020_123분기.csv',sep=",")

beadal = pd.read_csv('주요 배달앱 결제자수 결제금액 추정.csv',sep=",",skiprows=0)
df2018 = pd.DataFrame(df2018_1)
df2019 = pd.DataFrame(df2019_1)
df2020 = pd.DataFrame(df2020_1)
beadal_nop = beadal["결제자수"]
beadal_pay = beadal["결제금액"]
result = pd.concat([df2018,df2019,df2020],ignore_index=True)
result.drop('Unnamed: 0',axis= 1 ,inplace= True)
result['년/월']=['18-07','18-08','18-09','19-10','19-11','19-12','20-01','20-02','20-03','20-04','20-05','20-06','20-07','20-08','20-09']
result['분기']=['18년3분기','18년3분기','18년3분기','19년4분기','19년4분기','19년4분기','20년1분기','20년1분기','20년1분기','20년2분기','20년2분기','20년2분기','20년3분기','20년3분기','20년3분기']
result['배달결제자수']=beadal_nop
result["결제금액"]=beadal_pay
result.set_index('년/월',inplace=True) # 배달데이터랑 뽑을때 18년도 3분기는 제외하고 뽑아야됨
result=result.drop("사업장생활계폐기물(t)",axis=1)
# print(result)

corona = pd.read_csv("covid19_bd.csv")
result1=result.loc[:,['음식물','재활용']]



'''코로나 확진자 수데이터와 기존데이터 병합 우정이 자료 결제금액과 영훈이형 자료 결제금액 다른점은 이유를 알아야함'''
corona_bb = pd.merge(result,corona,on='년/월',how='outer')
# corona_bb.to_csv("종합데이터.csv")
print(corona_bb)
'''종합데이터로 코로나 이후 재활용 쓰레기 음식물 쓰레기 변화  여기에러,...'''
# fig, ax1 = plt.subplots()
# # ax1.set_ylim(1300,2000)# y축 범위
# ax1.set_xlabel('년/월')
# ax1.set_ylabel('확진자수',rotation='vertical')
# ax1.plot(corona_bb.index[3:16],corona_bb.loc[3:15,"확진자수"],color = 'red',label="총계(t)",linewidth=3,marker='o',markersize=5)
# ax2 = ax1.twinx()
# ax2.set_ylabel('쓰레기총계')
# ax2.bar(corona_bb.index[3:15],corona_bb.loc[3:15,"총계(t)"],color = ['g','g','g','g','g','g','b','b','b','b','b','b','b','b','b','b','b'],label="결제금액(십억)",alpha=0.5,width=0.5)
# # ax2 = ax1.twinx()
# # ax2.set_ylabel('결제자수(만명)')
# # ax2.bar(result.index,beadal_nop,color = ['g','g','g','g','g','g','b','b','b','b','b','b','b','b','b','b','b'],label="결제자수(만명)",alpha=0.5,width=0.5)
# # ax2.bar(result.index[:6],beadal_nop[:6],color = 'g',label="결제금액",alpha=0.5,width=0.5)
# # ax3 = ax1.twinx()
# # ax3.bar(result.index[6:],beadal_nop[6:],color = 'b',label="결제금액",alpha=0.5,width=0.5)
# # ax3 = ax1.twinx()
# # ax3.set_ylabel('배달결제자수')
# # ax3.bar(result.index,beadal_pay,color = 'blue',label="결제자수",alpha=0.5,width=0.5)
#
# ax1.set_zorder(ax2.get_zorder()+10)
# ax1.patch.set_visible(False)
# ax1.legend(loc='upper left')
# ax2.legend(loc='upper center')
# # ax3.legend(loc='upper right')
# plt.show()

'''종합데이터의 결손 데이터 그래프로 보기 ex)코로나 전에는 확진자수가 없음'''
# msno.matrix(corona_bb)
# plt.show()

'''생활폐기 마스크 및 sum,mean'''
# sang_mask_18_3 = result['생활폐기'][:3]
# sang_mask_19_4 = result['생활폐기'][3:6]
# sang_mask_20_1 = result['생활폐기'][6:10]
# sang_mask_20_2 = result['생활폐기'][10:14]
# sang_mask_20_3 = result['생활폐기'][:3]
#
# sang_mask_18_3_sum = int(result['생활폐기'][:3].sum())
# sang_mask_19_4_sum = int(result['생활폐기'][3:6].sum())
# sang_mask_20_1_sum = int(result['생활폐기'][6:10].sum())
# sang_mask_20_2_sum = int(result['생활폐기'][10:14].sum())
# sang_mask_20_3_sum = int(result['생활폐기'][:3].sum())
# sang_mask_18_3_mean = int(result['생활폐기'][:3].mean())
# sang_mask_19_4_mean = int(result['생활폐기'][3:6].mean())
# sang_mask_20_1_mean = int(result['생활폐기'][6:10].mean())
# sang_mask_20_2_mean = int(result['생활폐기'][10:14].mean())
# sang_mask_20_3_mean = int(result['생활폐기'][:3].mean())
# beadal_nop = result["배달결제자수"]
# beadal_pay = result["결제금액"]
# print("sang_mask_18_3_sum",sang_mask_18_3_sum)  # 분기별 합을 해서
# print("sang_mask_18_3_mean",sang_mask_18_3_mean)
# sang_mask_sum = result['생활폐기']
# x=result.index
# bungi_sum=[sang_mask_18_3_sum,sang_mask_19_4_sum,sang_mask_20_1_sum,sang_mask_20_2_sum,sang_mask_20_3_sum]
# # print(x)
# # print("sang_mask_18_3",sang_mask_18_3)
# # print("sang_mask_18_4",sang_mask_19_4)
# # print("sang_mask_sum",sang_mask_sum)
#
# per_kg = result['1일발생량(t)']
# per_kg_18_3_sum = int(result['1일발생량(t)'][:3].sum())
# per_kg_19_4_sum = int(result['1일발생량(t)'][3:6].sum())
# per_kg_20_1_sum = int(result['1일발생량(t)'][6:9].sum())
# per_kg_20_2_sum = int(result['1일발생량(t)'][9:12].sum())
# per_kg_20_3_sum = int(result['1일발생량(t)'][12:].sum())
#
# print("per_kg_sum",per_kg_18_3_sum)
# print("per_kg_sum",per_kg_19_4_sum)
# print("per_kg_sum",per_kg_20_1_sum)
# print("per_kg_sum",per_kg_20_2_sum)
# print("per_kg_sum",per_kg_20_3_sum)
# # per_kg_18_3 = int(result['1일발생량(t)'][:3].sum())
# # per_kg_19_4 = int(result['1일발생량(t)'][3:6])
# # per_kg_20_1 = int(result['1일발생량(t)'][6:9])
# # per_kg_20_2 = int(result['1일발생량(t)'][9:12])
# # per_kg_20_3 = int(result['1일발생량(t)'][12:])
#
# # print("per_kg",per_kg_18_3)
# # print("per_kg",per_kg_19_4)
# # print("per_kg",per_kg_20_1)
# # print("per_kg",per_kg_20_2)
# # print("per_kg",per_kg_20_3)
#
# # plt.plot(x,sang_mask_sum,kind='bar') # 애는 안됨 오류 찾기
# # plt.plot(per_kg_19_4,color='r') # 18년도 3분기 1인당
# # per_kg_19_4.plot(color='r')
# # plt.show()


'''생활 폐기물 '''
# sang_mask_19_4.plot(kind='bar',color='b')
# result['생활폐기'][:3].plot(kind='bar') # 18년도 3분기 생활폐기
# plt.xlabel('구분/월')
# plt.title("20183분기")
# result.plot(color='r')
# result.plot(kind = 'bar')
# # result.plot(kind = 'barh')
# plt.show()


# df1 = pd.read_csv("주요 배달앱 결제자수 결제금액 추정.csv")
# print(df1)
# df2 = pd.read_excel("배달앱_및_배달대행_이용현황_20210811121525.xls")
# print(df2)
# # df3 = pd.read_csv("폐기물_발생현황_생활폐기물_20210811141014.csv")
# # print(df3)
# df4 = pd.read_csv("한국환경공단_지자체별 RFID음식물쓰레기 배출량_20200731.csv",encoding='cp949')
# print(df4)
# seoul=df4['광역시도']=='서울특별시'
# year2018 = df4['배출연도']==2018
# year2019 = df4['배출연도']==2019
# year2020 = df4['배출연도']==2020
# ggg=df4[seoul & year2018]
# fff=df4[seoul & year2019]
# hhh=df4[seoul & year2020]
# # ton_2018 = ggg['배출량(톤)'].astype(float).sum()
# print(ggg)
# # print(ton_2018)
#

'''1일 쓰레기 발생량, 결제금액 비교 '''
# fig, ax1 = plt.subplots()
# # ax1.set_ylim(1300,2000)# y축 범위
# ax1.set_xlabel('년/월')
# ax1.set_ylabel('1일발생량',rotation='vertical')
# ax1.plot(result.index,per_kg,color = 'red',label="쓰레기1일발생량(t)",linewidth=3,marker='o',markersize=5)
# ax2 = ax1.twinx()
# ax2.set_ylabel('배달결제금액(십억)')
# ax2.bar(result.index,beadal_pay,color = ['g','g','g','g','g','g','b','b','b','b','b','b','b','b','b','b','b'],label="결제금액(십억)",alpha=0.5,width=0.5)
# # ax2 = ax1.twinx()
# # ax2.set_ylabel('결제자수(만명)')
# # ax2.bar(result.index,beadal_nop,color = ['g','g','g','g','g','g','b','b','b','b','b','b','b','b','b','b','b'],label="결제자수(만명)",alpha=0.5,width=0.5)
# # ax2.bar(result.index[:6],beadal_nop[:6],color = 'g',label="결제금액",alpha=0.5,width=0.5)
# # ax3 = ax1.twinx()
# # ax3.bar(result.index[6:],beadal_nop[6:],color = 'b',label="결제금액",alpha=0.5,width=0.5)
# # ax3 = ax1.twinx()
# # ax3.set_ylabel('배달결제자수')
# # ax3.bar(result.index,beadal_pay,color = 'blue',label="결제자수",alpha=0.5,width=0.5)
#
# ax1.set_zorder(ax2.get_zorder()+10)
# ax1.patch.set_visible(False)
# ax1.legend(loc='upper left')
# ax2.legend(loc='upper center')
# # ax3.legend(loc='upper right')
# plt.show()
# #
