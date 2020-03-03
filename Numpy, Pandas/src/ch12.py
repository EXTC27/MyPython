import pandas as pd
from pandas import *
import numpy as np

def main():
    # 인덱스가 다른 객체를 더하는 산술연산
    s1 = Series([5,6,-1,2], index=['a','c','d','e'])
    s2 = Series([3,4,-1,2,7], index=['a','c','e','f','g'])
    print(s1 + s2)
    print("--------------------------")

    df1 = DataFrame(np.arange(9).reshape(3, 3), columns=list('bcd'), index=['seoul', 'busan', 'kwangju'])
    df2 = DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'), index=['incheon', 'seoul', 'busan', 'suwon'])
    print(df1)
    print()
    print(df2)
    print()
    print(df1 + df2) #인덱스가 존재하는 값만 더해짐 둘중에 하나라도 없으면 NaN
    print("--------------------------")

    df3 = DataFrame(np.arange(12).reshape(3, 4), columns=list('abcd'))
    df4 = DataFrame(np.arange(20).reshape(4, 5), columns=list('abcde'))
    print(df3)
    print()
    print(df4)
    print()
    print(df3 + df4)
    print()
    print(df3.add(df4, fill_value=0)) #df3와 df4가 더해질 때 없는 부분은 0으로 채우고 더한다.
    print()
    print(df3.reindex(columns=df4.columns, fill_value=0)) #df3를 재색인할 때 비어있는 부분은 0으로 채운다.
    print("--------------------------")


if __name__ == "__main__":
    main()