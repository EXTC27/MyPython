
import numpy as np

#numpy 슬라이싱
def numpy_slicing():
    list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    arr = np.array(list)
    a = arr[0:2, 0:2] #0번부터 2개의 행, 0번부터 2개의 열
    print(a)
    print("------------")

    b = arr[1:, 1:] #1번부터 끝까지의 행, 1번부터 끝까지의 열
    print(b)
    print("------------")


#numpy 정수 인덱싱
#numpy 배열 a에 대해서 a[[row1, row2], [col1, col2]]는 
#a[row1, col1]과 a[row2, col2]라는 두개의 배열 요소 집합을 의미
def numpy_integer_indexing():
    list = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    a = np.array(list)

    #정수 인덱싱
    res = a[[0,2], [1,3]] #a[0,1]과 a[2,3]에 해당하는 요소값의 집합

    print(res)
    print("------------")

    #부울 인덱싱
    list1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    aa = np.array(list1)

    b_arr = np.array([
        [False, True, False],
        [True, False, True],
        [False, True, False]
    ])

    n = aa[b_arr]

    print(n)
    print("------------")


    #표현식을 이용하여 부울 인덱싱 배열 생성
    b_arr=(aa % 2 == 0) #배열 aa에서 짝수면 True, 홀수면 False

    print(b_arr)
    print("------------")
    print(aa[b_arr])
    print("------------")
    print(aa[aa % 2 == 0])
    print("------------")

if __name__ == "__main__":
    numpy_slicing()
    numpy_integer_indexing()