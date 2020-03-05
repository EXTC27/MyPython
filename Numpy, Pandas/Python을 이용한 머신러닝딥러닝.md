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



##### 1. pandas 자료구조: `Series`, `DataFrame`

- `Series` : 일차원 배열 같은 자료구조, `dictionary` 구조와 비슷하다.

  - Series 객체와 Series의 인덱스는 모두 name이라는 속성이 있다.
  - 사용법은 소스코드 참고 `ch6.py`

  

- `DataFrame` : 2차원 배열 같은 자료구조, R언어 data.frame과 비슷하다.

  - `ix`: row의 위치에 접근할 때 사용하는 속성이지만, **최신버전에서는 지원이 안되는 거 같다.**
  - `loc`: 라벨 값을 통해서 row의 위치에 접근할 때 사용하는 메서드
  - `iloc`: 정수
  - `T` : row와 column의 인덱스를 뒤집을 수 있다. (역행렬)
  - `values` : 저장된 데이터를 2차원 배열로 리턴해준다.



##### 2. 색인(index) 객체

- pandas의 색인 객체는 표 형식의 데이터에서 각 행과 열에 대한 헤더(이름)와 다른 메타데이터(축의 이름)를 저장하는 객체
- Series나 DataFrame객체를 생성할 때 사용되는 배열이나 또는 순차적인 이름은 내부적으로 색인으로 변환된다.
- **색인 객체는 변경할 수 없다.**
- `reindex`를 통해 재색인을 할 수 있다.



##### 3. 연산

- 인덱스가 다른 객체를 더하는 산술연산

  - 인덱스가 공통으로 존재하는 경유 연산이 되고, 아닌경우 NaN이 나온다.
    

- DataFrame과 Series간의 연산

  - numpy의 브로드캐스팅과 유사하다. product 연산이 아니라 요소하나하나 대응된다.

  - 기본적으로 column에 대한 연산이다.

  - row에 대한 연산을 수행할 경우 함수를 이용한다.

    >ex)
    >
    >`print(df.add(s3, axis=0)) ` #axis가 0이면 row에 대한 연산

  

##### 4. 함수적용과 매핑

- `apply()` 메서드와 람다식을 통해 row와 column에 대하여 함수를 적용시킬 수가 있다.

- 데이터프레임 객체에서 실수 값을 문자열 포맷으로 변환 할 경우 applymap 함수를 이용한다.

  >왜 굳이 applymap인가?
  >
  >DataFrame객체에서는 applymap을 사용한다.
  >
  >Series객체는 map 메서드를 사용한다.



##### 5. 정렬

- row나 column의 인덱스 순으로 정렬하는 등의 기준이 필요하다.
  
- `sort_index()` 메서드를 이용해서 정렬을 한다.

  - row를 기준으로 정렬

    >ex)
    >
    >`df.sort_index()`

  - column을 기준으로 정렬

    >ex)
    >
    >`df.sort_index(axis=1)`

  

- 데이터(인덱스, 값)는 기본적으로 오름차순으로 정렬이 된다.
  내림차순으로 정렬할 경우 ascending=False 해준다.

  >ex)
  >
  >`df.sort_index(axis=1, ascending=False)`

  

- 객체를 값에 따라 정렬할 경우에는` sort_values()`메서드를 사용한다.
  
- NaN의 경우 가장 마지막에 정렬된다.
  
- DataFrame의 경우

  - `sort_values(by='a')` 처럼 by옵션에 정렬하고자 하는 column명을 넣어준다.
  - `sort_values(by=['a', 'b'])` 처럼 list로 기준의 우선순위를 정하여 정렬할 수 있다.




##### 6. 순위

- `rank()` 함수를 통해 순위를 정할 수 있다.

  - 데이터의 값들을 기준으로 순위가 정해진다.
  - 동률이 존재할 경우 소수점으로 표시된다.
  - `method='first'` 옵션을 통해서 데이터 순서에 따라 순위를 정할 수 있다. 하지만 동률의 경우 다른 순위로 표기된다.
  - `method='max'` 를 사용하면 동률 표기가 가능해진다.

  

##### 7. 중복색인

- 중복되는 인덱스가 있을 경우 인덱스를 이용한 결과로 Series 객체를 리턴한다.



- pandas는  기본적으로 중복색인을 허용한다.



##### 8. 기술 통계 계산

- pandas는 일반적인 수학/통계 메서드를 제공한다.



- pandas의 메서드는 처음부터 누락된 데이터를 제외하도록 설계되어 있다.

  - `skipna` 옵션을 통해 누락된 데이터를 포함하고 계산할 수도 있다.
    누락된 값을 제외시키지 않으면 `NaN`이 나온다.

  

- `idxmin`, `idxmax` 메서드는 최소, 최대값을 가지고 있는 인덱스를 리턴한다.

- 누산 메서드

  - `cumsum()`

  

- 유일한 값

  - `unique()` : 중복값을 없애는 메서드, `unique()`에 의한 결과값은 정렬되지 않은 상태로 반환된다.



- 도수 메서드

  - `value_counts()`  : 값의 수(빈도수)를 계산한, Series 객체를 리턴한다.

  

- `isin()` : 어떤 값이 Series에 있는지 나타내는 메서드이다. boolean 값(True, False)을 반환한다.  DataFrame, Series에서 원하는 값을 골라내고 싶을 떄 유용하게 사용하는 메서드.



- 누락된 데이터 처리
  - pandas에서는 누락된 데이터를 모두 NaN으로 취급한다.
  - NaN의 값은 파이썬의 None값 NA와 같은 값으로 취급된다.



- 누락된 데이터 골라내기

  - `dropna()` 메서드를 이용

    - Series 객체를 리턴한다.
      

  - DataFrame에서 누락된 데이터 골라내기

    - dropna는 기본적으로 NA값이 하나라도 있는 row는 제외시킨다.
    - `how='all'` 옵션을 주면 모든 값이 NA인 row만 제외된다.
    - `how='all', axis=1` 모든 값이 NA인 column만 제외된다.
    - `thresh` 옵션은 몇 개의 value가 들어있는 행을 가져오고 싶을 경우 사용한다.

    

  - 누락된 값 채우기

    - 데이터 프레임에서는 누락된 데이터를 완벽하게 골라낼 수 가 없으므로 다른 데이터도 함께 버려지게 된다. 이런 경우에는 `fillna()` 메서드를 활용해서 비어있는 구멍을 채워주면 데이터의 손실을 막을 수 있다.

      >ex)
      >
      >dataFrame.fillna(0)

    - 활용에 따라 각 column마다 다른 값을 채워넣을 수 있다.

      >ex)
      >
      >dataFrame.fillna({1:10, 3:30})

    - 보간

      >ex)
      >
      >dataFrame.fillna(method='ffill')
      >
      >dataFrame.fillna(method='ffill', limit=1) 하나만 보간

    - 평균값으로 채우기

      >ex)
      >
      >dataFrame.fillna(dataFrame.mean())



##### 9.다중 색인(multi index)

- 색인의 계층 : pandas의 중요 기능 중의 하나로 다중 색인 단계를 지정할 수 있다.



- 인덱스 계층의 순서 바꾸기

  - `swaplevel()` 메서드를 이용해서 바꾼다.

    >ex)
    >
    >DataFrame.swaplevel('key1', 'key2') #key1과 key2를 바꾼다.

    

- 사전식으로 계층을 바꾸어서 정렬

  - `sortlevel()` 메서드를 이용해서 정렬한다.

    - 하지만, pandas 0.20.0 버전부터 `sort_index()`로 대체한다.

    >ex)
    >
    >DataFrame.sort_index(0)



- `set_index()` 메서드는 하나 이상의 column을 인덱스로 하는 새로운 DataFrame을 생성

- `reset_index()` 메서드는 `set_index()`와 반대되는 개념의 메서드이다. 
  인덱스를 column으로 하는 새로운 DataFrame을 생성한다.