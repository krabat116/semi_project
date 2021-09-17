import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
import matplotlib.lines as mlines
from matplotlib import font_manager, rc

'''코로나19 월별 확진자수와 배달앱 결제 금액의 상관관계 '''
# plt.rcParams['axes.unicode_minus']=False
# # path = ("/System/Library/Fonts/Supplemental/AppleGothic.ttf")
# path = 'C:/Windows/Fonts/HMKMRHD.TTF'
#
#
# if platform.system() =='Darwin':
#     rc('font', family='NanumSquareRoundR')
# elif platform.system()=='Windows':
#     font_name = font_manager .FontProperties(fname=path).get_name()
#     rc('font', family=font_name)
# else:
#     print('Unknown system...')
#
# data01 = pd.read_csv('covid19_bd.csv', encoding='utf-8')
# data01.set_index('A', inplace=True)
#
# plt.figure()
# dfdfdfdf=[0,1,2,3,4,5,6,7,8,9,10,11]
# label=['2020.1', '2020.2', '2020.3', '2020.4', '2020.5', '2020.6', '2020.7', '2020.8', '2020.9', '2020.10', '2020.11', '2020.12']
#
# data01['B'].plot(color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=7, figsize=(20,10), label="확진자수")
#
#
# plt.xticks(dfdfdfdf, label, fontsize=15)
# plt.xlabel('날짜', fontsize=20)
# plt.ylabel('확진자수', fontsize=20)
# plt.title("코로나19 월별 확진자 수와 배달앱 결제금액의 상관관계", fontsize=25)
#
#
# plt.twinx()
# plt.ylabel('결제금액(억)', fontsize=20)
# data01['C'].plot(color='red', linestyle='-', marker='s', markerfacecolor='cyan', markersize=7, figsize=(20,10), label="결제금액")
# # data01['C'].plot(kind='bar',alpha=0.3, color='cyan',width=0.5)
# plt.ylim(6000, 15000)
#
#
# ABC = mlines.Line2D([], [], color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=7, label='확진자수')
# DEF = mlines.Line2D([], [], color='red', linestyle='-', marker='s', markerfacecolor='cyan', markersize=7, label='결제금액(억)')
# plt.legend(handles=[ABC, DEF], loc="upper left", fontsize=25, frameon=True, shadow=True)
#
# plt.show()

'''코로나19 월별 확진자수와 배달앱 결제 금액의 상관관계2'''

plt.rcParams['axes.unicode_minus']=False
# path = ("/System/Library/Fonts/Supplemental/AppleGothic.ttf")
path = 'C:/Windows/Fonts/HMKMRHD.TTF'

if platform.system() =='Darwin':
    rc('font', family='NanumSquareRoundR')
elif platform.system()=='Windows':
    font_name = font_manager .FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...')

data01 = pd.read_csv('covid19_bd.csv', encoding='utf-8')
data01.set_index('A', inplace=True)

plt.figure()
dfdfdfdf=[0,1,2,3,4,5,6,7,8,9,10,11]
label=['2020.1', '2020.2', '2020.3', '2020.4', '2020.5', '2020.6', '2020.7', '2020.8', '2020.9', '2020.10', '2020.11', '2020.12']

data01['B'].plot(color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=7, figsize=(20,10), label="확진자수")

plt.xticks(dfdfdfdf, label, fontsize=15)
plt.xlabel('날짜', fontsize=20)
plt.ylabel('확진자수', fontsize=20)
plt.title("코로나19 월별 확진자 수와 배달앱 결제금액의 상관관계", fontsize=25)

plt.twinx()
plt.ylabel('결제금액(억)', fontsize=20)
N = 6
colors = np.random.rand(N * 3).reshape(N, -1)
data01['C'].plot(color='red', linestyle='-', marker='s', markerfacecolor='cyan', markersize=7, figsize=(20,10), label="결제금액")
data01['C'].plot(kind='bar', alpha=0.3, color=colors, width=0.5)
plt.ylim(6000, 15000)

ABC = mlines.Line2D([], [], color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=7, label='확진자수')
DEF = mlines.Line2D([], [], color='red', linestyle='-', marker='s', markerfacecolor='cyan', markersize=7, label='결제금액(억)')
plt.legend(handles=[ABC, DEF], loc="upper left", fontsize=25, frameon=True, shadow=True)

plt.show()