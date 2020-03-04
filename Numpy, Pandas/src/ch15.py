import pandas as pd
from pandas import *
import numpy as np

def main():
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

    #순위를 정하는 함수 rank()
    obj3 = Series([7,-2,7,4,2,0,4])
    print(obj3)
    print()
    print(obj3.rank())
    print()
    print(obj3.rank(method='first')) #method='first'는 데이터의 순서에 따라 순위를 매긴다.
    print()
    print(obj3.rank(ascending=False)) #내림차순으로 순위 정하기
    print()
    print(obj3.rank(ascending=False, method='first')) #내림차순 순서에 따라 순위 정하기
    print()
    print(obj3.rank(ascending=False, method='max')) #내림차순 그룹지어서 순위를 매김

if __name__ == "__main__":
    main()