import pandas as pd
from pandas import *
import numpy as np

def main():
    data = {
        "city":["서울", "부산", "광주", "대구"],
        "year":[2000, 2001, 2002, 2003],
        "pop":[4000, 2000, 1000, 1000]
    }

    df2 = DataFrame(data, columns=['year', 'city', "pop", "debt"], index=["one","two","three","four"]) #index는 row의 인덱스를 바꿀수 있다.
    print(df2)
    print("--------------------------------")
    print(df2["city"]) #city에 해당하는 column과 data type도 출력됨
    print("--------------------------------")
    print(df2["year"])
    print("--------------------------------")
    print(df2.columns) #df2의 column의 인덱스를 출력한다.
    print("--------------------------------")
    print(df2.index) #df2이 지정한 인덱스를 출력한다.
    print("--------------------------------")
    
    print(df2.loc["three"])
    print("--------------------------------")
    print(df2.iloc[0])
    print("--------------------------------")

    df2['debt'] = 1000
    print(df2)
    print("--------------------------------")
    df2['debt'] = np.arange(4)
    print(df2)
    print("--------------------------------")

    val = Series([1000, 2000, 3000, 4000], index=["one", "two", "three", "four"])
    df2['debt'] = val
    print(df2)
    print("--------------------------------")

    val1 = Series([1000, 3000, 5000], index=["one", "three", "four"])
    df2['debt'] = val1
    print(df2)
    print("--------------------------------")

    df2["aaa"] = df2.city == "서울"
    print(df2)
    print("--------------------------------")

    del df2["aaa"] #del 명령어로 aaa에 해당하는 column을 지울 수 있다.
    print(df2.columns)
    print(df2)
    print("--------------------------------")

    data2 = {
        "seoul" : {2001: 20, 2002: 30},
        "busan" : {2000: 10, 2001: 200, 2002: 300}
    }

    df3 = DataFrame(data2)
    print(df3)

if __name__ == "__main__":
    main()