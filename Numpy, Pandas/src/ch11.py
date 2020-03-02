import numpy as np
import pandas as pd
from pandas import *

def main():
    #슬라이싱
    obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
    print(obj['b':'c'])
    print()
    obj['b', 'c'] = 10 #기본적인 슬라이싱
    print(obj)
    print("--------------------------")

    data = DataFrame(np.arange(16).reshape(4, 4), index=['seoul', 'busan', 'kwangju', 'daegu'], columns=['one', 'two', 'three', 'four'])
    print(data)
    print()
    print(data['two'])
    print()
    print(data[['one', 'two']])
    print()
    print(data[:2])
    print()
    print(data[data["three"] > 7])
    print()
    print(data < 5)
    print()
    data[data < 5] = 0
    print(data)
    print("--------------------------")

    #ix 속성: DataFrame의 특수한 색인 필드(속성)
    #근데 최신버전은 지원이 안되는거 같다. 따라서 코드 생략

if __name__ == "__main__":
    main()