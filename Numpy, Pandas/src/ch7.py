import pandas as pd
from pandas import *

def main():
    data = {"Seoul":4000, "Busan":2000, "Incheon":1500, "Kwangju":1000}

    obj = Series(data)
    print(obj)
    print()

    cities = ["Seoul", "Daegu", "Incheon", "Kwangju"]
    obj2 = Series(data, index=cities)
    print(obj2)
    print()

    print(obj + obj2) #연산할 때 인덱스가 다른 부분은 NaN이 뜸
    print()

    #Series 객체와 Series의 인덱스는 모두 name이라는 속성이 있다.
    obj2.name = "인구 수"
    print(obj2)
    print()

    obj2.index.name = "도시"
    print(obj2)
    print()

    obj2.index = ["Daejeon", "Busan", "Jaeju", "Jeonju"]
    print(obj2)
    print()
    print("--------------------------")

    #DataFrame
    a = pd.DataFrame([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    print(a)
    print("--------------------------")

    data = {
        "city":["서울", "부산", "광주", "대구"],
        "year":[2000, 2001, 2002, 2003],
        "pop":[4000, 2000, 1000, 1000]
    }

    df = pd.DataFrame(data)
    print(df)
    print()
    #다음과 같이 인덱스의 순서도 바꿔줄 수 있다.
    df = DataFrame(data, columns=["year", "city", "pop"])
    print(df)


if __name__ == "__main__":
    main()