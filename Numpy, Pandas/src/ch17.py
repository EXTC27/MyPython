import pandas as pd
from pandas import *
import numpy as np

def main():
    #유일한 값, 도수 메서드
    s1 = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
    unique = s1.unique() #중복값을 없애는 메서드
    print(unique) #unique()에 의한 결과값은 정렬되지 않은 상태로 반환된다.
    print("-------------------------\n")

    cnt = s1.value_counts() #값의 수를 계산(도수), 반환값은 Series 객체 
    print(cnt) #내림차순으로 정렬된다.
    print("-------------------------\n")

    #isin 메서드는 어떤 값이 Series에 있는지 나타내는 메서드
    #boolean 값(True, False)을 반환한다.
    #DataFrame, Series에서 원하는 값을 골라내고 싶을 떄 유용하게 사용하는 메서드
    print(s1)
    print()
    mask = s1.isin(['b', 'c'])
    print(mask)
    print()
    print(s1[mask])
    print("-------------------------\n")

    data = DataFrame({'Q1':[1,3,4,3,4], 'Q2':[2,3,1,2,3], 'Q3':[1,5,2,4,4]})
    print(data)
    print()
    res = data.apply(pd.value_counts)
    print(res)
    print()
    res = data.apply(pd.value_counts).fillna(0) #NaN 대신 0으로 채운다.
    print(res)
    print("-------------------------\n")

    #누락된 데이터 처리
    #pandas에서는 누락된 데이터를 실수든 아니든 모두 NaN으로 취급한다.
    stringData = Series(['aaa', 'bbbb', np.nan, 'ccccc'])
    print(stringData)
    #NaN의 값은 파이썬의 None값 NA와 같은 값으로 취급된다.
    print()
    print(stringData.isnull())
    print()
    stringData[0] = None
    print(stringData.isnull())




if __name__ == "__main__":
    main()