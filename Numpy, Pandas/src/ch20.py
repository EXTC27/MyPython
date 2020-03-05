import pandas as pd
from pandas import *
import numpy as np

def main():
    df = DataFrame({
        'a':range(7), 
        'b':range(7,0,-1), 
        'c':['one', 'one', 'one', 'two', 'two', 'two', 'two'], 
        'd':[0,1,2,0,1,2,3]
        })

    print(df)
    print()

    #set_index() 메서드는 하나 이상의 column을 인덱스로 하는 새로운 DataFrame을 생성
    print(df.set_index(['c', 'd'])) 
    print()
    print(df.set_index(['c', 'd'], drop=False))
    print("-----------------------------\n")

    #reset_index() 메서드는 set_index()와 반대되는 개념의 메서드
    #인덱스를 column으로 하는 새로운 DataFrame을 생성한다.
    df2 = df.set_index(['c', 'd'])
    print(df2)
    print()
    print(df2.reset_index())


if __name__ == "__main__":
    main()