import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform

import seaborn
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus']=False
path = ("/C:\Windows\Fonts\malgun.ttf")

if platform.system() == 'Darwin':
    rc('font',family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family = font_name)
else:
    print('Unknown system...sorry~~')


data01 = pd.read_csv('./2021_08_12.csv')
data01.set_index('키워드', inplace=True)
plt.figure()
data01['블로그 총 발행량'].sort_values().plot(kind='barh', figsize=(10,10),)

plt.title('2021.08.12 블로그 총 발행량')
plt.xlabel('검색 횟수')
plt.ylabel('검색 키워드')
plt.show()
