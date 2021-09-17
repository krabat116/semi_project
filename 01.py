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

data01 = pd.read_csv('/Users/HOON/Desktop/데이터분석/목적DB/주요 배달앱 결제자수 결제금액 추정.csv')
data01.set_index('년월', inplace=True)
print(data01.head(13))

#plt.figure()



data01['결제자수'].plot(kind='bar', grid=True, figsize=(8,9))  #sort_values(): 수치 적은 것부터 차례대로
#plt.scatter(data01['결제자수'], data01['년월'], s=50)
plt.xlabel('결제자수(만단위)')
plt.ylabel('년월')
plt.show()