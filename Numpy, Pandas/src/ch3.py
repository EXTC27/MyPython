import numpy as np

def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    print(c)
    print("---------------")

    d = np.add(a, b)
    print(d)
    print("---------------")

    #나머지 연산은 생략


    #product 구하는 연산
    list1 = [
        [1, 2],
        [3, 4]
    ]

    list2 = [
        [5, 6],
        [7, 8]
    ]

    a = np.array(list1)
    b = np.array(list2)

    product = np.dot(a, b)
    print(product)
    print("---------------")

    #sum(), prod()

    a = np.array([[1, 2], [3, 4]])
    s = np.sum(a)
    print(s)
    print("---------------")

    s = np.sum(a, axis=0) #axis=0 이면 같은 column끼리 더한다. 
    print(s)
    print("---------------")

    s = np.sum(a, axis=1) #axis=1 이면 같은 row끼리 더한다. 
    print(s)
    print("---------------")

    s = np.prod(a, axis=0) #axis=0 이면 같은 column끼리 곱한다. 
    print(s)
    print("---------------") 

    s = np.prod(a, axis=1) #axis=1 이면 같은 row끼리 곱한다. 
    print(s)
    print("---------------")


if __name__ == "__main__":
    main()