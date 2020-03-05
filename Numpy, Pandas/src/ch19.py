import pandas as pd
from pandas import *
import numpy as np

def main():
    #다중 색인(multi index)
    #색인의 계층 : pandas의 중요 기능 중의 하나로 다중 색인 단계를 지정할 수 있다.
    data = Series(np.random.randn(11), 
                    index=[['a','a','a','b','b','b','c','c','c','d','d'],
                            [1,2,3,1,2,3,5,1,2,1,2]])

    print(data)
    print()
    print(data.index)
    print()
    print(data['b'])
    print()
    print(data['a':'b'])
    print()
    print(data.loc[['a','d']])
    print()
    print(data[:, 2])
    print()
    print(data[:, 5])
    print("------------------------------------\n")

    df = DataFrame(np.arange(12).reshape(4,3),
    index=[['a','a','b','b'], [1,2,1,2]],
    columns=[['seoul','busan','kwangju'], ['red','green','blue']])
    print(df)
    print()

    #column 인덱스의 이름 정하기
    df.columns.names=['city', 'color']
    print(df)
    print()

    df.index.names = ['key1', 'key2']
    print(df)
    print()
    print(df['seoul'])
    print("------------------------------------\n")

    #인덱스 계층의 순서를 바꾸기
    #swaplevel() 메서드를 이용해서 바꾼다.
    print(df.swaplevel('key1', 'key2')) #key1과 key2를 바꾸겠다.
    print("------------------------------------\n")

    #사전식으로 계층을 바꾸어서 정렬하기
    #sortlevel() 메서드를 이용해서 정렬한다.
    #sortlevel() 메서드는 0.20.0 버전부터 sort_index()로 대체한다.
    df2 = df.swaplevel('key1', 'key2')
    print(df2.sort_index(0))
    print()
    
    df3 = df.sort_index(1)
    print(df3.swaplevel(0, 1))
    print()
    print(df.swaplevel(0, 1).sort_index(0))
    print()
    print(df.sort_index(1).swaplevel(0, 1))
    print()
    print(df)
    print()
    print(df.sum(level='key2'))
    print("------------------------------------\n")

    df = DataFrame(np.arange(12).reshape(4,3),
    index=[['a','a','b','b'], [1,2,1,2]],
    columns=[['seoul','busan','kwangju'], ['red','green','red']])
    df.columns.names=['city', 'color']
    df.index.names = ['key1', 'key2']

    print(df.sum(level='color', axis=1))
    


if __name__ == "__main__":
    main()