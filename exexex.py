import pandas as pd
import numpy as np

obj = pd.Series([4,7,-5,3])
print("=====2====")
print(obj)  # dtype 데이터 타입 뜸
'''
0    4
1    7
2   -5
3    3
dtype: int64
'''
#Series 의 값만 확인하기
print("=====3====")
print(obj.values)  # dtype 데이터 타입 안뜸


print("=====4 ====")
print(obj.dtype)

# # int64
# # 인덱스를 바꿀 수 있다.
# print("=====5 ====")
# obj2 = pd.Series([4,7,-5,3], index=['d','b','a','c'])
# print(obj2)
# '''
# d    4
# b    7
# a   -5
# c    3
# dtype: int64
# '''
#
# print("=====6 ====")
# # python 의 dictionary 자료형을 Series data 로 만들 수 있다.
# #dictionary의 key 가 Series의 index 가 된다. key 가 시리즈에 인덱스
# sdata = {"Kim":35000, "Beomwoo":67000, "Joan":12000, "Choi": 4000 }
# obj3 = pd.Series(sdata)
# print(obj3)
# '''
# Kim        35000
# Beomwoo    67000
# Joan       12000
# Choi        4000
# dtype: int64
# '''
#
# print("===== 7 ====")
# obj3.name = "Saiary"
# obj3.index.name = "Names"
# print(obj3)
# '''
# Names  # index.name
# Kim        35000
# Beomwoo    67000
# Joan       12000
# Choi        4000
# Name: Saiary, dtype: int64
# '''
#
# print("===== 8 ====")
# # 인덱스 변경
# obj3.index = ['A', 'B', 'C', 'D']
# print(obj3)
# '''
# A    35000
# B    67000
# C    12000
# D     4000
# Name: Saiary, dtype: int64  # obj 이름은 그대로
# '''
#
#
# print("===== 9 ====")
# # Data Frame 정의하기
# # 이전에 Data Frame 에 들어갈 데이터를 정의해주어야 하는데,
# # 이는 python의 dictionary 또는 numpy의 array로 정의할 수 있다.
# data = {"name" : ["Beomwoo", "Beomwoo", "Beomwoo", "Kim", "Park"],
#         'year':[2013, 2014, 2015, 2016, 2015],
#         'points':[1.5, 1.7, 3.6, 2.4, 2.9]}
# df = pd.DataFrame(data)
# print(df)
# '''
# index     name  year  points  # 키
#     0  Beomwoo  2013     1.5
#     1  Beomwoo  2014     1.7
#     2  Beomwoo  2015     3.6
#     3      Kim  2016     2.4
#     4     Park  2015     2.9
# '''
#
# print("===== 10 ====")
# # 행과 열의 구조를 가진 데이터가 생긴다.
# # 행 방향의 index RangeIndex
#
# print(df.index)
# '''
# RangeIndex(start=0, stop=5, step=1)
# '''
#
# print("===== 11 ====")
# # 열 방향의 index
# print(df.columns)
# '''
# Index(['name', 'year', 'points'], dtype='object')
# '''
# print("===== 12 ====")
# #값 얻기
# print(df.values)  # dtype이 안나옴 자료는 나옴
# '''
# [['Beomwoo' 2013 1.5]
#  ['Beomwoo' 2014 1.7]
#  ['Beomwoo' 2015 3.6]
#  ['Kim' 2016 2.4]
#  ['Park' 2015 2.9]]
# '''
#
# print("===== 13 ====")
# # 각 인덱스에 대한 이름 설정하기
# df.index.name = 'Num'
# df.columns.name = 'info'
# print(df)
# '''
# info     name  year  points
# Num
# 0     Beomwoo  2013     1.5
# 1     Beomwoo  2014     1.7
# 2     Beomwoo  2015     3.6
# 3         Kim  2016     2.4
# 4        Park  2015     2.9
# '''
#
#
#
# print("===== 14 ====")  #######
# # Data Frame을 만들면서 columns 와 index를 설정 할 수 있다.
# df2 = pd.DataFrame(data, columns=['year', 'name', 'points', 'penalty'],
#                    index=['one', 'two', 'three', 'four', 'five'])
# print(df2)
# '''
# Data Frame을 정의하면서, data로 들어가는 python dictionary와 columns의 순서가 달라도
# 알아서 맞춰서 정의된다. 하지만 data에 포함되어 있지 않은 값은 NaN(Not a Number)으로 나타나게 되는데,
# 이는 null과 같은 개념이다.
# NaN값은 추후에 어떠한 방법으로도 처리가 되지 않는 데이터이다.
# 따라서 올바른 데이터 처리를 위해 추가적으로 값을 넣어줘야 한다.
# '''
# '''
#        year     name  points penalty
# one    2013  Beomwoo     1.5     NaN
# two    2014  Beomwoo     1.7     NaN
# three  2015  Beomwoo     3.6     NaN
# four   2016      Kim     2.4     NaN
# five   2015     Park     2.9     NaN
# '''
# print("===== 15 ====")
# # describe () 함수는 DataFrame의 계산 가능한 값들에 대한 다양한 계산 값을 보여준다.
# print(df2.describe())
# '''
#               year    points
# count     5.000000  5.000000
# mean   2014.600000  2.420000
# std       1.140175  0.864292
# min    2013.000000  1.500000
# 25%    2014.000000  1.700000
# 50%    2015.000000  2.400000
# 75%    2015.000000  2.900000
# max    2016.000000  3.600000
# '''
# print("===== 16 ====")
# data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
#         "year" : [2014, 2015, 2016, 2015, 2016],
#         "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
# df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
#                         index=["one", "two", "three", "four", "five"])
# # colums 행 name  index 열 name
# print(df)
# '''
#        year    names  points penalty
# one    2014    Kilho     1.5     NaN
# two    2015    Kilho     1.7     NaN
# three  2016    Kilho     3.6     NaN
# four   2015  Charles     2.4     NaN
# five   2016  Charles     2.9     NaN
# '''
#
# print("===== 17 18 ====")
# # DataFrame 에서 열을 선택하고 조작하기
# # print(df.year) # 동일 방법
# print(df['year'])
# '''
# one      2014
# two      2015
# three    2016
# four     2015
# five     2016
# Name: year, dtype: int64
# '''
# print("===== 19 ====")
# print(df[['year','points']])
# '''
#        year  points
# one    2014     1.5
# two    2015     1.7
# three  2016     3.6
# four   2015     2.4
# five   2016     2.9
# '''
# print("===== 21 ====")
# # 특정 열에 대해 위와 같이 선택하고, 우리가 원하는 값을 대입할 수 있다.
# df['penalty'] = 0.5
# print(df)
# '''
#        year    names  points  penalty
# one    2014    Kilho     1.5      0.5
# two    2015    Kilho     1.7      0.5
# three  2016    Kilho     3.6      0.5
# four   2015  Charles     2.4      0.5
# five   2016  Charles     2.9      0.5
# '''
# print("===== 22 ====")
# df['penalty'] = [0.1, 0.2, 0.3, 0.4, 0.5] # 리스트로?
# print(df)
# '''
#        year    names  points  penalty
# one    2014    Kilho     1.5      0.1
# two    2015    Kilho     1.7      0.2
# three  2016    Kilho     3.6      0.3
# four   2015  Charles     2.4      0.4
# five   2016  Charles     2.9      0.5
# '''
#
# print("===== 23 ====")
# # 새로운 열을 추가하기
# df['zeros'] = np.arange(5) # 넘파이 arange 가능 그럼 인덱스도 이걸로 가능?
# print(df)
# '''
#        year    names  points  penalty  zeros
# one    2014    Kilho     1.5      0.1      0
# two    2015    Kilho     1.7      0.2      1
# three  2016    Kilho     3.6      0.3      2
# four   2015  Charles     2.4      0.4      3
# five   2016  Charles     2.9      0.5      4
# '''
#
# print("===== 25 ====")
# # Series 를 추가할 수도 있다. # 그 인덱스에 맞춰서 넣을때 index 조심심
# val= pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# df['debt'] = val
# print(df)
# '''
#        year    names  points  penalty  zeros  debt
# one    2014    Kilho     1.5      0.1      0   NaN
# two    2015    Kilho     1.7      0.2      1  -1.2
# three  2016    Kilho     3.6      0.3      2   NaN
# four   2015  Charles     2.4      0.4      3  -1.5
# five   2016  Charles     2.9      0.5      4  -1.7
# '''
# '''
# 하지만 Series 로 넣을 때는 val와 같이 넣으려는 data의 index에 맞춰서 데이터가 들어간다.
# 이점이 python list 나 numpy array로 데이터를 넣을떄와 가장 큰 차이점이다.
#
# '''
# print("===== 26 ====")
# df['net_points'] = df['points'] - df['penalty'] # 연산 해서 넣을 때  열 추가 df['net_points'] = 이런식
# df['high_points'] = df['net_points'] > 2.0 # 불리언 값으로도 나옴옴print(df)
# '''
#        year    names  points  penalty  zeros  debt  net_points  high_points
# one    2014    Kilho     1.5      0.1      0   NaN         1.4        False
# two    2015    Kilho     1.7      0.2      1  -1.2         1.5        False
# three  2016    Kilho     3.6      0.3      2   NaN         3.3         True
# four   2015  Charles     2.4      0.4      3  -1.5         2.0        False
# five   2016  Charles     2.9      0.5      4  -1.7         2.4         True
# '''
# print("===== 27 ====")
# #열 삭제 하기  del
# del df['high_points']
# print(df)
# '''
#        year    names  points  penalty  zeros  debt  net_points
# one    2014    Kilho     1.5      0.1      0   NaN         1.4
# two    2015    Kilho     1.7      0.2      1  -1.2         1.5
# three  2016    Kilho     3.6      0.3      2   NaN         3.3
# four   2015  Charles     2.4      0.4      3  -1.5         2.0
# five   2016  Charles     2.9      0.5      4  -1.7         2.4
# '''
# print("===== 28 ====")
# del df['net_points']
# del df['zeros']
# print(df)
# '''
#        year    names  points  penalty  debt
# one    2014    Kilho     1.5      0.1   NaN
# two    2015    Kilho     1.7      0.2  -1.2
# three  2016    Kilho     3.6      0.3   NaN
# four   2015  Charles     2.4      0.4  -1.5
# five   2016  Charles     2.9      0.5  -1.7
# '''
# print("===== 29 ====")
# print(df.columns)
# '''
# Index(['year', 'names', 'points', 'penalty', 'debt'], dtype='object')
# '''
#
# print("===== 30 ====")
# df.index.name = 'Order'
# df.columns.name = 'info'
# print(df)
# '''
# info   year    names  points  penalty  debt
# Order
# one    2014    Kilho     1.5      0.1   NaN
# two    2015    Kilho     1.7      0.2  -1.2
# three  2016    Kilho     3.6      0.3   NaN
# four   2015  Charles     2.4      0.4  -1.5
# five   2016  Charles     2.9      0.5  -1.7
# '''
# ######################################################
# print("===== 32 ====")
# '''
# DataFrame 에서 행을 선택하고 조작하기
# pandas 에서는 DataFramedptj 행을 인덱싱 하는 방법이 무수히 많다.
# 물론 위에서 소개했던 열을 선택하는 방법도 수많은 방법중에 하나에 불과하다.
# '''
# # 0번째 부터 2(3-1)번 쨰까지 가져온다.
# # 뒤에 써준 숫자번째의 행은 뺀다.
# print(df[0:3])
# '''
# info   year  names  points  penalty  debt
# Order
# one    2014  Kilho     1.5      0.1   NaN
# two    2015  Kilho     1.7      0.2  -1.2
# three  2016  Kilho     3.6      0.3   NaN
# '''
#
# print("===== 33 ====")
# # two 라는 행부터 four라는 행까지 가져온다.
# # 뒤에 써준 이름의 행을 뺴지 않는다.
# print(df['two':'four']) # 비추천 와이?
# '''
# info   year    names  points  penalty  debt
# Order
# two    2015    Kilho     1.7      0.2  -1.2
# three  2016    Kilho     3.6      0.3   NaN
# four   2015  Charles     2.4      0.4  -1.5
# '''
#
# print("===== 34 ====")
# # 요 방법을 권장함
# # .loc 또는 .iloc 함수를 사용하는 방법.
# print(df.loc['two']) # 반환 형태는 Series
# '''
# info
# year        2015
# names      Kilho
# points       1.7
# penalty      0.2
# debt        -1.2
# Name: two, dtype: object
# '''
#
#
# print("===== 35 ====")
# print(df.loc['two':'four'])
# '''
# info   year    names  points  penalty  debt
# Order
# two    2015    Kilho     1.7      0.2  -1.2
# three  2016    Kilho     3.6      0.3   NaN
# four   2015  Charles     2.4      0.4  -1.5
# '''
# print("===== 36 ====")
# print(df.loc['two':'four', 'points'])
# '''
# Order
# two      1.7
# three    3.6
# four     2.4
# Name: points, dtype: float64
# '''
#
# print("===== 37 ====")
# print(df.loc[:, 'year']) # == df['year'] year 의 모든 행
# '''
# Order
# one      2014
# two      2015
# three    2016
# four     2015
# five     2016
# Name: year, dtype: int64
# '''
# print("===== 38 ====")
# print(df.loc[:,['year', 'names']]) # == df['year'] 'year', 'names' 열의 모든 행
# '''
# info   year    names
# Order
# one    2014    Kilho
# two    2015    Kilho
# three  2016    Kilho
# four   2015  Charles
# five   2016  Charles
# '''
#
# print("===== 39 ====")
# print(df.loc['three':'five', 'year':'penalty']) # == df['year'] year~penalty
# '''
# info   year    names  points  penalty
# Order
# three  2016    Kilho     3.6      0.3
# four   2015  Charles     2.4      0.4
# five   2016  Charles     2.9      0.5
# '''
#
# print("===== 41 ====")
# # 새로운 행 삽입 하기  각 value 넣어 줘여함
# df.loc['six',:] = [2013, 'Jone', 2.0, 0.1, 2.1]
# print(df)
# '''
# info     year    names  points  penalty  debt
# Order
# one    2014.0    Kilho     1.5      0.1   NaN
# two    2015.0    Kilho     1.7      0.2  -1.2
# three  2016.0    Kilho     3.6      0.3   NaN
# four   2015.0  Charles     2.4      0.4  -1.5
# five   2016.0  Charles     2.9      0.5  -1.7
# six    2013.0     Jone     2.0      0.1   2.1
# '''
# print("===== 42 ====")
# # .iloc 사용 :: index 번호를 사용한다. 행만 가져오기
# print(df.iloc[3]) # 3번째 행을 가져온다.
# '''
# info
# year        2015.0
# names      Charles
# points         2.4
# penalty        0.4
# debt          -1.5
# Name: four, dtype: object
# '''
# print("===== 43 ====")
# print(df.iloc[3:5, 0:2])
# '''
# info     year    names
# Order
# four   2015.0  Charles
# five   2016.0  Charles
# '''
# print("===== 46 ====")
# print(df.iloc[[0,1,3], [1,2]]) # 행 열 지정 가능
# '''
# info     names  points
# Order
# one      Kilho     1.5
# two      Kilho     1.7
# four   Charles     2.4
# '''
# print("===== 47 ====")
# print(df.iloc[:, 1:4])
# '''
# info     names  points  penalty
# Order
# one      Kilho     1.5      0.1
# two      Kilho     1.7      0.2
# three    Kilho     3.6      0.3
# four   Charles     2.4      0.4
# five   Charles     2.9      0.5
# six       Jone     2.0      0.1
# '''
# print("===== 48 ====")
# print(df.iloc[1,1])
# '''
# Kilho
# '''
# print("===== 49 ====")
# '''
# DataFrame boolean indexing
# '''
# print(df)
# '''
# info     year    names  points  penalty  debt
# Order
# one    2014.0    Kilho     1.5      0.1   NaN
# two    2015.0    Kilho     1.7      0.2  -1.2
# three  2016.0    Kilho     3.6      0.3   NaN
# four   2015.0  Charles     2.4      0.4  -1.5
# five   2016.0  Charles     2.9      0.5  -1.7
# six    2013.0     Jone     2.0      0.1   2.1
# '''
# print("===== 50 ====")
# # year가 2014 보다 큰 boolean data
# print(df['year'] > 2014)  # 조건 만 넣을 때 True False
# '''
# Order
# one      False
# two       True
# three     True
# four      True
# five      True
# six      False
# Name: year, dtype: bool
# '''
# print("===== 51 ====")
# print(df.loc[df['names'] == 'Kilho',['names','points']])  # 조건 넣어 줄 떄
# '''
# info   names  points
# Order
# one    Kilho     1.5
# two    Kilho     1.7
# three  Kilho     3.6
# '''
# print("===== 52 ====")
# # numpy 에서와 같이 논리연산을 응용할 수 있다.
# print(df.loc[(df['points']>2)&(df['points']<3),:]) # point 값 2초과 3 미만 모든 행
# '''
# info     year    names  points  penalty  debt
# Order
# four   2015.0  Charles     2.4      0.4  -1.5
# five   2016.0  Charles     2.9      0.5  -1.7
# '''
# print("===== 53,54 ====")
# # 새로운 값을 대입할 수도 있다.
# df.loc[df['points']>3,'penalty'] = 0 # point 3 이상 penalty 0
# print(df)
# '''
# info     year    names  points  penalty  debt
# Order
# one    2014.0    Kilho     1.5      0.1   NaN
# two    2015.0    Kilho     1.7      0.2  -1.2
# three  2016.0    Kilho     3.6      0.0   NaN
# four   2015.0  Charles     2.4      0.4  -1.5
# five   2016.0  Charles     2.9      0.5  -1.7
# six    2013.0     Jone     2.0      0.1   2.1
# '''
#
# print("===== 55 ====")
# #DataFrame을 만들 때 index, column 을 설정하지 않으면 기본값으로 0부터 시작하는 정수형 숫자로 입력된다.
# df = pd.DataFrame(np.random.randn(6,4))
# print(df)
# '''
#           0         1         2         3
# 0  0.573993  0.669843  1.041256 -1.838300
# 1  1.341876 -0.082578 -1.697153  1.074568
# 2  0.075987 -1.035557 -1.323053  1.158527
# 3 -1.169771 -0.413766  0.558117 -0.655227
# 4 -0.071372  0.111246 -1.121536 -0.240719
# 5 -0.186733  0.137920 -0.040878  0.673444
# '''
#
# print("===== 56 ====")
# df.columns = ['A', 'B', 'C', 'D']
# df.index = pd.date_range('20160701', periods=6)
# # pandas에서 제공하는 date_range함수는 datetime 자료형으로 구성된 날짜 시각등을 알 수 있는 자료형을 만드는 함수
# print(df.index)
# '''
# DatetimeIndex(['2016-07-01', '2016-07-02', '2016-07-03', '2016-07-04',
#                '2016-07-05', '2016-07-06'],
#               dtype='datetime64[ns]', freq='D')
# '''
# print("===== 57 ====")
# print(df)
# '''
# 2016-07-01  0.573993  0.669843  1.041256 -1.838300
# 2016-07-02  1.341876 -0.082578 -1.697153  1.074568
# 2016-07-03  0.075987 -1.035557 -1.323053  1.158527
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444
# '''
# print("===== 58 ====")
# # np.nan 은 NaN값을 의미한다.
# df['F'] = [1.0, np.nan, 3.5, 6.1, np.nan, 7.0]  # 열 추가 + NaN 값
# print(df)
# '''                A         B         C         D    F
# 2016-07-01  0.573993  0.669843  1.041256 -1.838300  1.0
# 2016-07-02  1.341876 -0.082578 -1.697153  1.074568  NaN
# 2016-07-03  0.075987 -1.035557 -1.323053  1.158527  3.5
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227  6.1
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719  NaN
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444  7.0
# '''
# print("===== 59 ====")
# # 행의 값중 하나라도 nan값 인 경우 그 행을 없앤다. 결측값
# print(df.dropna(how='any'))  # axis 옵션 디폴트로 행 지정 ,  axis = 0 or row  how 옵션 'any' 결측지가 있는 행이면 전부라는 의미
# '''
#                    A         B         C         D    F
# 2016-07-01  0.573993  0.669843  1.041256 -1.838300  1.0
# 2016-07-03  0.075987 -1.035557 -1.323053  1.158527  3.5
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227  6.1
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444  7.0
# '''
# '''
# 주의 drop함수는 특정 행 또는 열을 drop하고 난 DataFrame을 반환한다.
# 즉, 반환을 받지 않으면 기존의 DataFrame은 그대로이다.
# 아니면, inplace = True라는 인자를 추가하여, 반환을 받지 않고서도
# 기존의 DataFrame이 변경되도록 한다.
# '''
#
# print("===== 61 ====")
# # nan 값에 값 넣기
# print(df.fillna(value=0.5))
# '''
#                    A         B         C         D    F
# 2016-07-01  0.573993  0.669843  1.041256 -1.838300  1.0
# 2016-07-02  1.341876 -0.082578 -1.697153  1.074568  0.5
# 2016-07-03  0.075987 -1.035557 -1.323053  1.158527  3.5
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227  6.1
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719  0.5
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444  7.0
# '''
#
# print("===== 62 ====")
#
# # nan  값인지 확인하기
# print(df.isnull())
# '''
#                 A      B      C      D      F
# 2016-07-01  False  False  False  False  False
# 2016-07-02  False  False  False  False   True
# 2016-07-03  False  False  False  False  False
# 2016-07-04  False  False  False  False  False
# 2016-07-05  False  False  False  False   True
# 2016-07-06  False  False  False  False  False
# '''
#
# print("===== 63 ====")
# # F열에서 nan값을 포함하는 행만 추출하기  F열
# print(df.loc[df.isnull()['F'],:])
# '''
#                    A         B         C         D   F
# 2016-07-02  1.341876 -0.082578 -1.697153  1.074568 NaN
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719 NaN
# '''
#
# print("===== 64 ====")
# print(pd.to_datetime('20160701'))
# # 2016-07-01 00:00:00
#
# print("===== 65 ====")
# # 특정행 drop하기 ??????
# print(df.drop(pd.to_datetime('20160701')))
# '''
#                    A         B         C         D    F
# 2016-07-02  1.341876 -0.082578 -1.697153  1.074568  NaN
# 2016-07-03  0.075987 -1.035557 -1.323053  1.158527  3.5
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227  6.1
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719  NaN
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444  7.0
# '''
# print("===== 66 ====")
# # 2개 이상도 가능
# print(df.drop([pd.to_datetime('20160702'),pd.to_datetime('20160703')]))
# '''
#                    A         B         C         D    F
# 2016-07-01  0.573993  0.669843  1.041256 -1.838300  1.0
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227  6.1
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719  NaN
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444  7.0
# '''
# print("===== 67 ====")
# #특정 열 삭제하기
# print(df.drop('20160701',axis = 0)) #
# print(df.drop('F',axis = 1))
# '''
#                    A         B         C         D    F
# 2016-07-02  1.341876 -0.082578 -1.697153  1.074568  NaN
# 2016-07-03  0.075987 -1.035557 -1.323053  1.158527  3.5
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227  6.1
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719  NaN
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444  7.0
#                    A         B         C         D
# 2016-07-01  0.573993  0.669843  1.041256 -1.838300
# 2016-07-02  1.341876 -0.082578 -1.697153  1.074568
# 2016-07-03  0.075987 -1.035557 -1.323053  1.158527
# 2016-07-04 -1.169771 -0.413766  0.558117 -0.655227
# 2016-07-05 -0.071372  0.111246 -1.121536 -0.240719
# 2016-07-06 -0.186733  0.137920 -0.040878  0.673444
# '''
# print("===== 68 ====")
# #2 개 이상의 열도 가능
# print(df.drop(['B','D'],axis = 1))
# '''
#                    A         C    F
# 2016-07-01  0.573993  1.041256  1.0
# 2016-07-02  1.341876 -1.697153  NaN
# 2016-07-03  0.075987 -1.323053  3.5
# 2016-07-04 -1.169771  0.558117  6.1
# 2016-07-05 -0.071372 -1.121536  NaN
# 2016-07-06 -0.186733 -0.040878  7.0
# '''

print("===== 70 ====")
'''Data 분석용 함수들 '''
data=[
    [1.4, np.nan],
    [7.1, -4.5],
    [np.nan, np.nan],
    [0.75, -1.3]
      ]
df = pd.DataFrame(data, columns=["one", "two"], index=["a", "b", "c", "d"])
print(df)
'''
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3
'''

print("===== 71 ====")
# 행 방향으로의 합 ( 즉, 각 열의 합)
print(df.sum(axis=0))
'''
one    9.25
two   -5.80
dtype: float64
'''
'''
이떄 출력값에서 볼 수 있듯이 NaN값은 배제하고 계산한다.
NaN 값을 배제하지 않고 계산하려면 아래와 같이 skipna에 대해 false로 지정해준다
'''
print("===== 72 ====")
print(df.sum(axis=1,skipna=False))
'''
a     NaN
b    2.60
c     NaN  
d   -0.55
dtype: float64
'''
print("===== 73 ====")
# 특정 행 또는 특정 열에서만 계산하기
print(df['one'].sum())
print(df['two'].sum())
'''
9.25
-5.8
'''
print("===== 74 ====")
print(df.loc['a'].sum())
'''
1.4
'''
print("===== 75 ====")
#  행값 periods 값 같아야지~ 돈두르마돈두르마 잡아야쥐~
df3 = pd.DataFrame(np.random.randn(6,4),
                   columns=['A','B','C','D'],
                   index=pd.date_range("20160701",periods=6))
print(df3)
'''
                   A         B         C         D
2016-07-01 -0.648979 -1.314532  0.377134 -1.472631
2016-07-02 -0.614854  1.309597 -0.518718 -1.399751
2016-07-03 -0.366113  0.606592 -0.189654  0.306462
2016-07-04 -2.851018 -0.566090  0.512436 -1.390729
2016-07-05  2.115544  1.851996  0.257734  0.614287
2016-07-06 -0.484149 -0.059409  1.026257  0.194265
'''

print("===== 76 ====")
# A열과 B열의 상관계수 구하기  #  두 변수 사이의 통계적 관계를 표현하기위해 특정한 상관관계의 정도를 수치적으로 나타낸다
''' corr = correlation
변수와 상관관계 : 변수간 흐름이 얼마나 비슷한가를 나타내는 척도
- a가 증가하면 b도 증가하냐/감소하냐
- 증가의 성향이 얼마나 비슷한가
ㅇ   1에 가까울 수록 두개가 비슷하게 증가
ㅇ   -1에 가까울 수록 하나 증가/ 하나 감소
ㅇ   0에 가까울수록 두개간 관계가 없다
'''
print(df3['A'].corr(df3['B']))
'''
0.6704831290827927  
'''

print("===== 77 ====")
#B열 과 C열의 공분산 구하기 covariance
print(df3['B'].cov(df3['C']))
'''
-0.3220542126743586
'''

print("===== 78 ====")
dates = df3.index
random_dates = np.random.permutation(dates)  # 무작위로 섞인 배열 만듬 배열 모양 그대로 무작위 배열
df3 = df3.reindex(index = random_dates, columns = ["D","B","C","A"])
print(df3)
'''
                   D         B         C         A
2016-07-04 -1.390729 -0.566090  0.512436 -2.851018
2016-07-02 -1.399751  1.309597 -0.518718 -0.614854
2016-07-03  0.306462  0.606592 -0.189654 -0.366113
2016-07-01 -1.472631 -1.314532  0.377134 -0.648979
2016-07-06  0.194265 -0.059409  1.026257 -0.484149
2016-07-05  0.614287  1.851996  0.257734  2.115544
'''
print("===== 79 ====")
# index 와 column 의 순서가 섞여있다.
# 이때 index가 오름차순이 되도록 정렬해보자
print(df3.sort_index(axis=0))  # 위에 랜덤 때리고 인덱스로만 오름차순  날짜 별로 010203040506
'''
                   D         B         C         A
2016-07-01 -1.472631 -1.314532  0.377134 -0.648979
2016-07-02 -1.399751  1.309597 -0.518718 -0.614854
2016-07-03  0.306462  0.606592 -0.189654 -0.366113
2016-07-04 -1.390729 -0.566090  0.512436 -2.851018
2016-07-05  0.614287  1.851996  0.257734  2.115544
2016-07-06  0.194265 -0.059409  1.026257 -0.484149
'''
print("===== 80 ====")
# col을 기준
print(df3.sort_index(axis=1)) # 위의 열 인덱스로만 ABCD
'''
                   A         B         C         D
2016-07-04 -2.851018 -0.566090  0.512436 -1.390729
2016-07-02 -0.614854  1.309597 -0.518718 -1.399751
2016-07-03 -0.366113  0.606592 -0.189654  0.306462
2016-07-01 -0.648979 -1.314532  0.377134 -1.472631
2016-07-06 -0.484149 -0.059409  1.026257  0.194265
2016-07-05  2.115544  1.851996  0.257734  0.614287
'''
print("===== 81 ====")
# 내림차순으로 ㄴ,ㄴ?
print(df3.sort_index(axis=1, ascending=False)) # ascending  기본 정렬방식 오름차순. 내림차순 false
'''
                   D         C         B         A
2016-07-04 -1.390729  0.512436 -0.566090 -2.851018
2016-07-02 -1.399751 -0.518718  1.309597 -0.614854
2016-07-03  0.306462 -0.189654  0.606592 -0.366113
2016-07-01 -1.472631  0.377134 -1.314532 -0.648979
2016-07-06  0.194265  1.026257 -0.059409 -0.484149
2016-07-05  0.614287  0.257734  1.851996  2.115544
'''
print("===== 82 ====")
# 값기준 정렬
# D열의 값이 오름차순이 되도록
print(df3.sort_values(by='D')) # D 기준 오름차순
'''
                   D         B         C         A
2016-07-01 -1.472631 -1.314532  0.377134 -0.648979
2016-07-02 -1.399751  1.309597 -0.518718 -0.614854
2016-07-04 -1.390729 -0.566090  0.512436 -2.851018
2016-07-06  0.194265 -0.059409  1.026257 -0.484149
2016-07-03  0.306462  0.606592 -0.189654 -0.366113
2016-07-05  0.614287  1.851996  0.257734  2.115544
'''
print("===== 83 ====")
# B열의 값이 내림차순이 되도록 정렬하기
print(df3.sort_values(by='B',ascending=False))
'''
                   D         B         C         A
2016-07-05  0.614287  1.851996  0.257734  2.115544
2016-07-02 -1.399751  1.309597 -0.518718 -0.614854
2016-07-03  0.306462  0.606592 -0.189654 -0.366113
2016-07-06  0.194265 -0.059409  1.026257 -0.484149
2016-07-04 -1.390729 -0.566090  0.512436 -2.851018
2016-07-01 -1.472631 -1.314532  0.377134 -0.648979
'''

print("===== 84 ====")

df3["E"] = np.random.randint(0,6,size=6)
df3["F"] = ["alpha", "beta", "gamma", "gamma","alpha", "gamma"]
print(df3)
'''
                   D         B         C         A  E      F
2016-07-04 -1.390729 -0.566090  0.512436 -2.851018  5  alpha
2016-07-02 -1.399751  1.309597 -0.518718 -0.614854  0   beta
2016-07-03  0.306462  0.606592 -0.189654 -0.366113  2  gamma
2016-07-01 -1.472631 -1.314532  0.377134 -0.648979  2  gamma
2016-07-06  0.194265 -0.059409  1.026257 -0.484149  2  alpha
2016-07-05  0.614287  1.851996  0.257734  2.115544  1  gamma
'''
print("===== 85 ====")
#E열과 F열을 동시에 고려하여, 오름차순으로 하려면?
print(df3.sort_values(by=['E','F']))
'''
                   D         B         C         A  E      F
2016-07-02 -1.399751  1.309597 -0.518718 -0.614854  0   beta
2016-07-05  0.614287  1.851996  0.257734  2.115544  1  gamma
2016-07-06  0.194265 -0.059409  1.026257 -0.484149  2  alpha
2016-07-03  0.306462  0.606592 -0.189654 -0.366113  2  gamma
2016-07-01 -1.472631 -1.314532  0.377134 -0.648979  2  gamma
2016-07-04 -1.390729 -0.566090  0.512436 -2.851018  5  alpha
'''

print("===== 86 ====")
# 지정한 행 또는 열에서 중복값을 제외한 유니크한 값만 얻기
print(df3['F'].unique())
'''
['alpha' 'beta' 'gamma']
'''
print("===== 87 ====")
# 지정한 행 또는 열에서 값에 따른 개수 얻기 value_counts
print(df3['F'].value_counts())
'''
gamma    3
alpha    2
beta     1
Name: F, dtype: int64
'''
print("===== 88 ====")
#지정한 행 또는 열에서 입력한 값이 있는지 확인하기 isin !!
print(df3['F'].isin(["alpha", "beta"]))
'''
2016-07-04     True
2016-07-02     True
2016-07-03    False
2016-07-01    False
2016-07-06     True
2016-07-05    False
Name: F, dtype: bool
'''

print("===== 89 ====")
#F열의 값이 알파나 베타인 모든 행 구하기
print(df3.loc[df3['F'].isin(["alpha", "beta"]),:])
'''
                   D         B         C         A  E      F
2016-07-04 -1.390729 -0.566090  0.512436 -2.851018  5  alpha
2016-07-02 -1.399751  1.309597 -0.518718 -0.614854  0   beta
2016-07-06  0.194265 -0.059409  1.026257 -0.484149  2  alpha
'''

print("===== 90 ====")
df4 = pd.DataFrame(np.random.randn(4,3), columns=["b","d","e"],
                   index= ["서울","인천","부산","대구"])
print(df4)
'''
           b         d         e
서울  0.809607  0.201471  0.164400
인천  0.119837 -0.580021  1.166487
부산  2.101493 -1.331205  1.689306
대구 -0.214897 -1.733039  1.646059
'''
print("===== 91 ====")
func = (lambda x: x.max() - x.min())  # 여기 마지막 왜지?
print(func)
'''
<function <lambda> at 0x0000024CFCF50EE0>
'''
print("===== 91 ====")
df4.apply(func, axis=0)
print(df4.apply(func, axis=0))
'''
b    2.316390
d    1.934510
e    1.524906
dtype: float64
'''