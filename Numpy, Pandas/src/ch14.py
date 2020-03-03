import pandas as pd
from pandas import *
import numpy as np

def main():

    #함수적용과 매핑
    #numpy.random 모듈에 있는 randn함수는 임의의 정규분표 데이터를 생성한다.
    df = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['seoul', 'busan', 'daegu', 'incheon'])
    print(df)
    print()
    print(np.abs(df))
    print("----------------------------\n")

    f = lambda x : x.max()-x.min()
    print(df.apply(f))
    print()
    print(df.apply(f, axis=1))
    print("----------------------------\n")
    
    def f(x):
        return Series([x.min(), x.max()], index=['min', 'max'])

    print(df.apply(f))
    print()

    #DataFrame 객체에서 실수 값을 문자열 포맷으로 변환 할 경우 applymap 함수를 사용한다.
    format = lambda x : '%.2f' % x
    print(df.applymap(format))
    print()
    #Series 객체에서 실수 값을 문자열 포맷으로 변환 할 경우 map 함수를 사용한다.
    print(df['e'].map(format))
    print("----------------------------\n")

    #정렬
    #row나 column의 인덱스 순으로 정렬하는 등의 기준이 필요하다.
    s1 = df['e'].map(format)
    print(s1)
    print()
    print(s1.sort_index()) #인덱스 순으로 정렬된다.
    print("----------------------------\n")

    df2 = DataFrame(np.arange(8).reshape(2, 4), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
    print(df2)
    print()
    print(df2.sort_index()) #row를 기준으로 정렬
    print()
    print(df2.sort_index(axis=1)) #column을 기준으로 정렬
    print("----------------------------\n")

    #데이터(인덱스, 값)는 기본적으로 오름차순으로 정렬이 된다.
    #내림차순으로 정렬할 경우 ascending=False 해준다.
    print(df2.sort_index(axis=1, ascending=False))
    print("----------------------------\n")

    #객체를 값에 따라 정렬할 경우에는 sort_values메서드를 사용한다.
    obj = Series([4,7,-3,1])
    print(obj.sort_values())
    print("----------------------------\n")
    
    obj2 = Series([4, np.nan, 8, np.nan, -10, 2])
    print(obj2.sort_values()) #NaN의 경우 가장 마지막에 정렬된다.
    print("----------------------------\n")

    frame = DataFrame({
        'b':[4,7,-5,2],
        'a':[0,1,0,1]
        })

    print(frame)
    print()
    print(frame.sort_values(by='b')) #by옵션에 정렬하고자하는 column명을 넣어준다.
    print()
    print(frame.sort_values(by='a')) #a column의 값을 기준으로 정렬
    print()
    print(frame.sort_values(by=['a', 'b'])) #a 다음 b columns의 값을 기준으로 정렬
    print("----------------------------\n")


if __name__ == "__main__":
    main()