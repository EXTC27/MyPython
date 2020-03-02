# Python을 이용한 머신러닝/딥러닝



### Numpy/Pandas

- 보통 둘이 같이 사용한다. 둘다 C로 만들어져서 처리속도가 빠르다.



---

#### *Numpy 

- 과학 계산을 위한 라이브러리로 다차원 배열을 처리하는데 필요한 기능을 제공.



##### 1. 설치

- `pip3 install numpy`



##### 2. numpy 배열

- numpy에서 배열은 동일한 타입의 값들을 갖는다.
- 배열의 차원을 **rank**라고 한다.
- **shape** : 각차원의 크기를 tuple로 표시한 것.
  - ex) 2x3인 2차원 배열 => rank는 2, shape(2, 3) 로 표기가 된다.



##### 3. numpy 배열을 생성하는 방법

1. 파이썬의 list를 사용

   - `array()` 함수의 인자로 list를 넣어 사용한다.

     > ex) `numpy.array([1, 2, 3])`

   

2. numpy에서 제공하는 함수 사용

   1. `zeros()` : 0으로 초기화된 배열 생성

   2. `ones()` : 1로 초기화된 배열 생성

   3. `full()` : 사용자가 지정한 값으로 초기화된 배열 생성

   4. `eye()` : 단위행렬 생성 (2차원 배열)

   5. `reshape()` : 다차원으로 변형하는 함수, 주의할 점은 배열의 개수를 지켜줘야 한다.

      > ex) `numpy.array(range(20)).reshape(5, 4)`, 5*4 = 20



##### 4. numpy 배열 슬라이싱, 인덱싱

1. 슬라이싱

   - 범위식을 이용한다.

     > ex)
     >
     > `numpy.array(list)[0:2, 0:2]` => 2차원 배열 list의 0번부터 2개의 행, 0번부터 2개의 열에 해당하는 배열 리턴
     >
     > `numpy.array(list)[1:, 1:]` => 2차원 배열 list의 1번부터 끝까지의 행, 1번부터 끝까지의 열에 해당하는 배열 리턴

   

2.  인덱싱

   - 정수 인덱싱

     > ex)
     >
     > `numpy.array(list)[[0, 2], [1, 3]]` => 2차원 배열 list의 [0,1]과 [2,3]에 해당하는 요소값의 집합을 리턴

   - 부울 인덱싱

     > ex)
     >
     > 1. 단순한 방법
     >
     > ```python
     > import numpy as np
     > 
     > list1 = [
     >     [1,2,3],
     >     [4,5,6],
     >     [7,8,9]
     > ]
     > 
     > aa = np.array(list1)
     > 
     > #단순한 방법
     > b_arr = np.array([
     >     [False, True, False],
     >     [True, False, True],
     >     [False, True, False]
     > ])
     > 
     > n = aa[b_arr]
     > 
     > print(n) # [2, 4, 6, 8]
     > 
     > 
     > #표현식을 이용한 방법
     > b_arr=(aa % 2 == 0)
     > 
     > n = aa[b_arr]
     > 
     > print(n) # [2, 4, 6, 8]
     > 
     > #이렇게해도 됨
     > n = aa[aa % 2 == 0]
     > 
     > print(n) # [2, 4, 6, 8]
     > ```



##### 5.numpy 연산

1. 연산자를 이용

   - +, -, *, /

   

2. 함수를 이용

   - `add()`

   - `substract()`

   - `multiply()`

   - `divide()`

   - `dot()` : vector, matrix의 product를 구하는 함수 (행렬의 곱)

   - `sum()` : 배열의 요소를 더하는 함수, `add()`와의 차이점은 `axis` 옵션을 사용한다.
     `axis=0`이면 같은 column끼리, `axis=1`이면 같은 row끼리,

   - `prod()` : 배열의 요소를 곱하는 함수, `multiply()`와의 차이점은 `axis` 옵션을 사용한다.
     `axis=0`이면 같은 column끼리, `axis=1`이면 같은 row끼리,

     

##### 6.numpy 자료형

- int, float, bool

1. 정수형(integer)

   - int8, int16, int32, int64 (signed)
   - uint (unsigned integer) : uint8(0~255), unit16(0~65535), uint32, uint64

   

2. 실수형(float)

   - float16, float32, float64
   - complex
     - complex64 : 두개의 32bit 부동소수점으로 표시되는 복소수
     - complex128 : 두개의 64bit 부동소수점으로 표시되는 복소수

   

##### 7.numpy 브로드캐스

- 소스코드 참고 `ch5.py`



---

#### *Pandas

- 데이터 분석 기능을 제공하는 라이브러리, CSV파일 등의 데이터를 읽고 원하는 데이터 형식으로 변환해줌



- pandas 자료구조: `Series`, `DataFrame`
  
  - `Series` : 일차원 배열 같은 자료구조, `dictionary` 구조와 비슷하다.
  
    - Series 객체와 Series의 인덱스는 모두 name이라는 속성이 있다.
    - 사용법은 소스코드 참고 `ch6.py`
  
    
  
  - `DataFrame` : 2차원 배열 같은 자료구조, R언어 data.frame과 비슷하다.
  
    - `ix`: row의 위치에 접근할 때 사용하는 메서드이지만, **최신버전에서는 지원이 안되는 거 같다.**
    - `loc`: 라벨 값을 통해서 row의 위치에 접근할 때 사용하는 메서드
    - `iloc`: 정수

