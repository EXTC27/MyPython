import pandas as pd
from pandas import *
import numpy as np

#색인(index) 객체
def main():
    obj = Series(range(3), index=['a', 'b', 'c'])

    print(obj)
    print("-----------------------")

    idx = obj.index
    print(idx)
    print()
    print(idx[1])
    print()
    print(idx[1:])
    print("-----------------------")

    #idx[1] = 'd' #색인 객체는 변경할 수 없다. 이거 에러뜬다.
    index2 = pd.Index(np.arange(3))
    print(index2)
    print("-----------------------")

    #재색인(reindex) : 새로운 색인에 맞도록 객체를 새로 생성하는 기능
    obj = Series([2.3, 4.3, -4.1, 3.5], index=['d', 'b', 'a', 'c'])
    print(obj)
    print()
    
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    print(obj2)
    print()

    obj3 = obj.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value=0.0) #fill_value를 속성을 통해 새로 들어가는 인덱스의 값을 지정할 수 있다.
    print(obj3)
    print("-----------------------")

    obj4 = Series(['blue', 'red', 'yellow'], index=[0,2,4])
    print(obj4)
    print()

    obj5 = obj4.reindex(range(6), method='ffill') #보간
    print(obj5)
    print("-----------------------")

    df = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['x', 'y', 'z'])
    print(df)
    print("-----------------------")

    df2 = df.reindex(['a', 'b', 'c', 'd'])
    print(df2)
    print("-----------------------")

    col = ['w', 'm', 'n']
    print(df2.reindex(columns=col))
    print()

    col = ['x', 'y', 'w', 'z']
    print(df.reindex(columns=col))
    print("-----------------------")

    df = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'd'], columns=['x', 'y', 'z'])
    print(df)
    print()
    df3 = df.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=col)
    print(df3) #DataFrame에서 보간은 row에 대해서만 이루어진다.
    print("-----------------------")

    


if __name__ == "__main__":
    main()