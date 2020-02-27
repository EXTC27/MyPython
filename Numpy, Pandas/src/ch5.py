#numpy 브로드 캐스트
import numpy as np

def main():
    a = np.array([[1,2], [3,4]])
    b = 10

    c = a*b
    print(c)
    print("-------------------------")

    x = np.array([[1,2],[3,4]])
    y = np.array([10,20])

    z = x*y
    print(z)
    print("-------------------------")

    #배열 요소 접근
    x = np.array([[11,21],[43,43],[0,9]])
    print(x)
    print()
    for row in x:
        print(row)
    print("-------------------------")

    #2차원 배열을 1차원 배열로 변환(평탄화) : flatten()
    x = x.flatten()
    print(x)
    print("-------------------------")

    print(x[np.array([1, 3, 5])]) #인덱스가 1, 3, 5인 요소들을 꺼낸다.

    print(x[x > 25]) # x > 25 조건이 참인 요소만 꺼낸다.

    print(x > 25) #numpy 배열에 부등호 연산자를 사용한 결과는 bool 배열이다.
    


if __name__ == "__main__":
    main()