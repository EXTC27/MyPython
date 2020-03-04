import pandas as pd
from pandas import *
import numpy as np

def main():
    #중복색인
    obj = Series(range(5), index=['a','a','b','b','c'])

    print(obj)
    print()
    print(obj['a']) #중복되는 인덱스가 있을 경우 인덱스를 이용한 결과로 Series 객체를 리턴한다.
    print()
    print(obj['c'])
    print()
    print(obj['b'])
    print("---------------------------\n")
    
    df =DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
    print(df)
    print()
    print(df.loc['b']) #pandas는 중복색인을 허용한다.
    print("---------------------------\n")

    #기술 통계 계산
    #pandas는 일반적인 수학/통계 메서드를 가지고 있다.
    #pandas의 메서드는 처음부터 누락된 데이터를 제외하도록 설계되어 있다.
    df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
    print(df)
    print()

    #sum() 메서드는 각 컬럼의 합을 더해서 Series 객체를 반환한다.
    print(df.sum())
    print()
    print(df.sum(axis=1)) #각 row의 합을 반환한다.
    print("---------------------------\n")

    #전체 행이나 칼럼의 값이 NA가 아니라면 NA값은 제외시키고 계산을 한다.
    #skipna옵션은 전체 row나 column의 값이 NA가 아니라도 제외시키지 않을 수 있다.
    #skipna의 기본값은 True이다.
    print(df.sum(axis=1, skipna=False)) #NA값을 제외시키지 않으면 NA가 나온다.
    print("---------------------------\n")

    #idxmin, idxmax와 같은 메서드는 최소, 최대값을 가지고 있는 인덱스 값 같은 간접 통계를 리턴한다.
    print(df.idxmax())
    print("---------------------------\n")

    #누산 메서드 : cumsum()
    print(df.cumsum())


if __name__ == "__main__":
    main()