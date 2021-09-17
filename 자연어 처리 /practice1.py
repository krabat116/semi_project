import numpy as np
import platform
import nltk
from konlpy.tag import Okt

import matplotlib

import matplotlib.pyplot as plt

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

# #그래프에서 마이너스 기호가 표시되도록 하는 설정

from bs4 import BeautifulSoup #BeautifulSoup 라이브러리 임포트
from urllib.request import urlopen #urllib.request에서 urlopen 임포트
import urllib
import time #time 임포트


tmp1 = 'https://search.naver.com/search.naver?where=news'  #검색엔진
html = tmp1 + '&sm=tab_jum&ie=utf8&query={key_word}&start={num}' #검색 키워드와 넘버

response = urlopen(html.format(num=1, key_word=urllib.parse.quote('코로나 이후 배민'))) #키워드 코테이션은 배민

soup = BeautifulSoup(response, 'html.parser') #response 에 대해 html 파서 소환

tmp = soup.find_all('ul') #ul에 해당하는 정보 전부 찾기

tmp_list = [] #tmp_list를 리스트화
for line in tmp:
    tmp_list.append(line.text) #반복문 형태로 append를 통해 text 추가

print(tmp_list) #리스트 프린트

from tqdm import tqdm #tqdm_notebook은 쥬피터 노트북에서만 사용하는 기능
present_candi_text = [] #후보군들을 리스트화

for n in tqdm(range(1, 2000, 10)): #범위 설정 1000개
    response = urlopen(html.format(num=n, key_word=urllib.parse.quote('코로나 이후 배민')))  #배민만 파싱
    soup = BeautifulSoup(response, "html.parser") #html parser 소환
    tmp = soup.find_all('ul') #ul에 해당하는 내용 전부 찾기
    for line in tmp:
        present_candi_text.append(line.text) #후보군들을 append함수로 text 추가
    time.sleep(0.5) #0.5초의 텀
t = Okt()
'''
자연어처리 라이브러리 임포트
'''
present_text = ''
for each_line in present_candi_text[:len(present_candi_text)]:
    present_text = present_text + each_line + '\n'

tokens_ko = t.morphs(present_text)  #형태소를 분석

ko = nltk.Text(tokens_ko, name='배민') #형태소
print(len(ko.tokens)) #전체 토큰 수 : 38594
print(len(set(ko.tokens))) #실제 토큰 수 : 1651

ko = nltk.Text(tokens_ko, name='배민')
a = ko.vocab().most_common(100) #제일 자주쓴 100개 찾기
print(a)
'''
제외 단어 처리
'''
stop_words = ['.', '...', '에', '@', '순', '이', '(', ')', ',',
              '3', '@txt', '펼치기', '접기', "'", '는', '문서', '을',
              '·', '1', 'data@.', '“', '…' ,'‘', '[', ']', '2020.04',
              '2021.05', '"', '’', '10', '의', '19', '하기', '은', '들'
              '를', '가', '으로', '로', '과', '한']
tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]
ko = nltk.Text(tokens_ko, name = '코로나 이후 배민')
ko.vocab().most_common(50)

plt.figure(figsize=(18, 9))
ko.plot(30)
plt.show()
'''
그래프 사이즈 18, 9
50개의 x축 값
그래프 출력
'''

'''
wordcloud 그리기
'''

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

mask = np.array(Image.open('./baemin.jpg')) #배민 이미지를 마스크로 로드

from wordcloud import ImageColorGenerator

image_colors = ImageColorGenerator(mask)

data = ko.vocab().most_common(100)
wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',
                      relative_scaling = 0.1, mask=mask,
                      background_color = 'white',
                      min_font_size=1, max_font_size=100).generate_from_frequencies(dict(data))
default_colors = wordcloud.to_array()


'''
제외 단어 처리
'''
stop_words = ['.', '...', '에', '@', '순', '이', '(', ')', ',',
              '3', '@txt', '펼치기', '접기', "'", '는', '문서', '을',
              '·', '1', 'data@.', '“', '…' ,'‘', '[', ']', '2020.04',
              '2021.05', '"', '’', '10', '의', '19', '하기', '은', '들'
              '를', '가', '으로', '로', '과', '한']
tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]
ko = nltk.Text(tokens_ko, name = '코로나 이후 배민')
ko.vocab().most_common(30)

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='bilinear') #이중선형보간법
plt.axis('off')
plt.show()


