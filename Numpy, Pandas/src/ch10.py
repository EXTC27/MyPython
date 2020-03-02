import numpy as np
import pandas as pd
from pandas import *

def main():
    
    obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
    print(obj)
    print()

    obj2 = obj.drop('c')
    print(obj2)
    print()

    obj3 = obj.drop(['b', 'd', 'c'])
    print(obj3)
    print("-----------------------")

    df = DataFrame(np.arange(16).reshape(4, 4), index=["seoul", "busan", "deagu", "incheon"], columns=["one", "two", "three", "four"])
    print(df)
    print()

    new_df = df.drop(["seoul", "busan"])
    print(new_df)
    print()

    new_df = df.drop('three', axis=1)  #three라는 column을 지움.
    print(new_df)
    print()

    new_df = df.drop(["two", "four"], axis=1)
    print(new_df)
    print("----------------------------")


if __name__ == "__main__":
    main()