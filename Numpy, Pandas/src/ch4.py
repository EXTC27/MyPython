import numpy as np

def main():
    x = np.float32(1.0)

    print(x)
    print(type(x))
    print(x.dtype) #데이터의 type을 알아보기 위한 dtype 속성
    print("--------------------------------")

    z = np.arange(5, dtype='f')
    print(z)
    print("--------------------------------")

    aa = np.array([1,2,3], dtype='f')
    print(aa)
    print(aa.dtype)
    print("--------------------------------")

    xx = np.int8(aa)
    print(xx)
    print(xx.dtype)

    bb = np.arange(10)
    print(bb)
    print("--------------------------------")

    cc = np.arange(3, 10, dtype=np.float)
    print(cc)
    print(cc.dtype)
    print("--------------------------------")

    dd = np.arange(2, 3, 0.1)
    print(dd)


if __name__ == "__main__":
    main()