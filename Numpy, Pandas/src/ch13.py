import pandas as pd
from pandas import *
import numpy as np

def main():

    #DataFrame과 Series간의 연산 (numpy의 브로드캐스팅과 유사하다)

    arr = np.arange(12.).reshape(3, 4)
    print(arr)
    print()
    print(arr[0])
    print()
    print(arr - arr[0])
    print("----------------------------\n")

    df = DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'), index=['seoul', 'kwangju', 'daegu', 'incheon'])
    print(df)
    print()
    s1 = df.iloc[0]
    print(s1)
    print()
    print(df - s1) #브로드캐스팅 연산이 됨
    print("----------------------------\n")
    s2 = Series(range(3), index=list('bef'))
    print(s2)
    print()
    print(df + s2) #마찬가지로 공통되지 않은 인덱스는 값이 NaN이 된다.
    print("----------------------------\n")

    s3 = df['d']
    print(s3)
    print()
    print(df + s3) #인덱스 이름이 같아도 row와 column이 다르면 공통된 인덱스가 아니다.
    print()
    
    #row에 대한 연산을 수행할 경우에는 함수를 이용한다.
    print(df)
    print()
    print(df.add(s3, axis=0))
    print()
    print(df.sub(s3, axis=0))
    print("----------------------------\n")

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
    






if __name__ == "__main__":
    main()