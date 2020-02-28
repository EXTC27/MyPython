import pandas as pd
from pandas import Series, DataFrame

def main():
    obj = Series([3, 22, 34, 11])
    print(obj)
    print()
    print(obj.values)
    print()
    print(obj.index) #시작, 종료, 간격이 출력된다.
    print("----------------------------")
    

    #인덱스를 직접 지정할 수도 있다.
    obj2 = Series([4,5,6,2], index=['d','c','e','f'])
    print(obj2)
    print()
    print(obj2['c'])
    print()
    print(obj2[['d','f','c']]) #여러개의 인덱스에 접근할 경우 list로 묶어줘야 한다.
    print()
    print(obj2*2)
    print()
    print('b' in obj2) #조건식을 활용해서 참, 거짓을 뽑아 낼 수 있다.
    print("----------------------------")

    #dictionary 형식을 그대로 사용할 수 있다.
    data = {'kim':3400, 'hong':2000, 'kang':1000, 'lee':2400}
    obj3 = Series(data)
    print(obj3)
    print("----------------------------")

    name = {'woo', 'hong', 'kang', 'lee'}
    obj4 = Series(data, index=name)
    print(obj4)
    print("----------------------------")

    #누락된 데이터를 찾을 때 사용하는 함수 isnull, notnull
    print(pd.isnull(obj4))
    print()
    print(pd.notnull(obj4))

if __name__ == "__main__":
    main()