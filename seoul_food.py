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


# df = pd.read_csv("한국환경공단_지자체별 RFID음식물쓰레기 배출량_20200731.csv",encoding="cp949")
# seo_1= df['광역시도']=='서울특별시'
#
#
# # pprint(df)
# pprint(df[seo_1])
# pprint(df[seo_1].dtypes)
# seo_11=df[seo_1]
# # print(seo_11)
# pd.options.mode.chained_assignment = None
# seo_12=seo_11['배출량(톤)']
# # print(seo_12)
# for i in seo_12.index:
#     seo_11['배출량(톤)'][i]=seo_11['배출량(톤)'][i].replace(',','')
# print(seo_11)
# seo_11.to_csv("한국환경공단_음식물쓰레기_서울시배출량.csv")

# plt.show()

# gg=df[seo_1]
# qq = gg['배출연도']=2017
# pprint(qq)

# seoul_foodb=pd.read_csv("한국환경공단_음식물쓰레기_서울시배출량.csv")
# seoul_foodb.set_index('Unnamed: 0',inplace=True)
#
# seoul_foodb_19=seoul_foodb['배출연도']==2019
#
# # print(seoul_foodb.dtypes)
# print(seoul_foodb[seoul_foodb_19])

