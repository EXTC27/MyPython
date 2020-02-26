import numpy as np

def main():
    list1 = [1, 2, 3, 4]
    a = np.array(list1)
    print(a)
    print(a.shape) #1차원 배열, 즉 rank가 1이라 열의 개수만 나옴    
    print()

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b)
    print(b.shape) #rank가 2이기 때문에 (2,3)이 출력됨.
    print()

    aa = np.zeros((2, 2)) #2x2인 0행렬 생성
    print(aa)
    print(type(aa))
    print()

    aa = np.ones((2, 3)) #2x3인 1행렬 생성
    print(aa)
    print()

    aa = np.full((2, 3), 10) #2x3이고 요소값이 10인 행렬생성
    print(aa)
    print()

    aa = np.eye(4) #4x4 단위행렬 생성
    print(aa)
    print()

    aa = np.array(range(20)).reshape((5, 4)) #range()로 [0, n-1] 숫자열 생성, array()로 배열 생성, reshape()로 다차원 배열로 변환
    print(aa)
    print()

    aa = np.array(range(15)).reshape((3, 5))
    print(aa)
    print()


if __name__ == "__main__":
    main()
