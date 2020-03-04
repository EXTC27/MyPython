import pandas as pd
import numpy as np
from numpy import nan as NA
from pandas import Series, DataFrame

def main():
    #누락된 데이터 골라내기
    #dropna 함수를 이용하는 방법 등 여러방법이 있다.
    #dropna를 사용하는 것이 유용한 방법이며, Series 객체를 리턴한다.

    data = Series([1, NA, 3.4, NA, 8])
    print(data.dropna())
    print("-------------------------\n")

    #boolean 색인을 이용해서 직접 계산한 후에 가져오기
    print(data.notnull())
    print()
    print(data[data.notnull()])
    print("-------------------------\n")

    #DataFrame에서 누락된 데이터를 골라 내기
    #dropna는 기본적으로 NA값이 하나라도 있는 row는 제외시킨다.
    data = DataFrame([[1, 5.5, 3], [1, NA, NA], [NA, NA, NA], [NA, 3.3, 3]])
    print(data)
    print()
    print(data.dropna()) #하나라도 NA가 있는 row는 제외된다.
    print("-------------------------\n")

    #how='all' 옵션을 주면 모든 값이 NA인 row만 제외된다.
    print(data.dropna(how='all'))
    print()
    data[4] = NA
    print(data)
    print()
    print(data.dropna(how='all', axis=1)) #모든 값이 NA인 column만 제외된다.
    print("-------------------------\n")

    data2 = DataFrame([[1,2,3,NA], [NA,33,11,NA], [11,NA,NA,NA], [43,NA,NA,NA]])
    print(data2)
    print()
    #몇 개의 value가 들어있는 행을 가져오고 싶을 경우 사용되는 인자는 thresh
    print(data2.dropna(thresh=2))
    print("-------------------------\n")

    #누락된 값을 채우기
    #데이터 프레임에서는 누락된 데이터를 완벽하게 골라낼 수 가 없으므로 다른 데이터도 함께 버려지게 된다. 이런 경우에는 fillna 메서드를 활용해서 비어있는 구멍을 채워주면 데이터의 손실을 막을 수 있다.
    print(data2.fillna(0))
    print()
    #fillna의 활용에 따라 각 column마다 다른 값을 채워넣을 수 있다.
    print(data2.fillna({1:10, 3:30}))
    print()
    #보간을 활용
    print(data2.fillna(method='ffill')) #앞의 값으로 보간
    print()
    print(data2.fillna(method='ffill', limit=1))
    print("-------------------------\n")

    data3 = Series([1, NA, 4, NA, 7])
    print(data3)
    print()
    print(data3.fillna(data3.mean())) #NA를 평균값으로 채운다.

if __name__ == "__main__":
    main()
