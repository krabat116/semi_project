import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus']=False
path = ("/System/Library/Fonts/Supplemental/AppleGothic.ttf")

if platform.system() =='Darwin':
    rc('font', family='AppleGothic')
elif platform.system()=='Windows':
    font_name = font_manager .FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...')

data01 = pd.read_csv('/Users/HOON/Desktop/데이터분석/목적DB/우아한 형제들 매출, 영업이익, 연간거래액.csv')
data01.set_index('연도',inplace=True )#
print(data01.head())

#plt.figure()

#data01 = pd.DataFrame(np.)


data01['매출'].plot(kind='bar', grid=True, figsize=(8,9))  #sort_values(): 수치 적은 것부터 차례대로
#plt.scatter(data01['결제자수'], data01['년월'], s=50)
plt.xlabel('연도')
plt.ylabel('매출[억단위]')
plt.show()