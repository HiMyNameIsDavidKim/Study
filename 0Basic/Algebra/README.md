# Algebra

## `[대수학]`
* 미지수에 변수를 ‘대입’하는 기술, 그것을 ‘계산’하는 기술.
* 결론적으로 방정식을 푸는 기술.
* 코딩은 수학으로 되어 있는 것을 문자로 치환하는 것이므로 곧 대수학이다.
<br><br>

### [대수]
* 대수는 상수와 변수의 집합이다.
    * 상수 : constant, 변하지 않는 것
    * 변수 : variable, 변하는 것
* 대수학의 시작은 ‘알콰리즈미’에 의해 시작했고, 그 이름을 따 ‘알제브라’라고 명했다.
* 이에 파생되어 문제를 해결하는 솔루션을 '알고리즘'이라 한다.
<br><br>



## `[선형대수]`

### [행렬]
* 전치 행렬 : transposed matrix, 주대각선을 축으로 하는 반사 대칭 행렬.
    * A^(T)
    * 주대각선 : main diagonal, i=j인 요소를 연결한 선.
    * (ex. [[a,a1,a2], [a1,b,a3], [a2,a3,c]])
    * 한 컬럼을 가진 행렬을 표현하기 위해 리스트의 전치행렬을 많이 쓴다.
* 행렬 곱 : matrix product, 두 행렬에서 한 행렬을 연산.
    * C = AB
    * C의 1,1 원소 = A의 1행과 B의 1열의 스칼라곱.
* 항등 행렬 : identity matrix, 주대각선의 원소가 모두 1이고 나머지는 0인 정사각 행렬.
    * I
    * 행렬A와 I를 곱셈하면 항상 A가 나온다.
* 역행렬 : inverse marix, 행렬과 곱한 결과가 단위행렬이 되게 하는 행렬.
    * A^(-1)
    * [[a, b], [c, d]]^(-1) = 1/(ad-bc)[[d, -b], [-c, a]]
* 행렬식 : determinant, 정사각 행렬에 스칼라를 대응시키는 함수의 하나.
    * det[[a, b], [c, d]] = ad - bc
* 선형 결합 : linear combination, 각 항에 상수를 곱하고 더함으로써 일련의 항으로 구성된 표현식.
    * x와 y의 선형결합은 ax + by 형식.
* 놈 : norms, 벡터의 크기를 측정하는 방법.
    * Ln = ∥x∥n
    * L1 = |x1| + |x2| + ... + |xn|
    * L2 = √ (x1^2 + x2^2 + ... + xn^2)
    * Lmax = 벡터 성분들 절대값 중에서 가장 큰 절대값.
    * L0 = 벡터 성분들 중에서 0이 아닌 값 개수.
<br><br>

### [행렬(심화)]
* 고유벡터(x) : eigenvector, 선형 변환이 일어난 후에도 방향이 변하지 않는 0이 아닌 벡터.
    * 열벡터로 나타난다.
    * 정방행렬 A에 대하여 Ax = λx를 성립하는 x가 존재해야 한다.
* 고유값(λ) : eigenvalue, 선형 변환 후 달라진 배율값.
    * 상수로 나타난다.
    * 고유벡터에 대응한다.
* 켤레 전치 행렬 : 행렬을 전치한 후 모든 요소를 켤레 복소수로 바꾼 행렬.
    * A^(*)
* 에르미트 행렬 : 켤레 전치가 자기 자신과 같은 복소수 정사각 행렬.
    * A = A^(*)
    * (ex. [[2,2+i,4], [2-i,3,i], [4,-i,1]])
* 유니터리 행렬 : 켤레 전치가 역행렬과 같은 복소수 정사각 행렬.
    * A^(*) = A^(-1)
* 대각 합 : trace operator, 정사각 행렬의 주대각선 성분의 합.
    * Tr(A) = A_1,1 + A_2,2 + ... + A_n,n
<br><br>

### [행렬 분해]
* 고유값 분해 : eigen decomposition, 고유값 및 고유벡터 형태로 분해.
    * det(xI - A)로 고유벡터 x1, x2를 구한다.
    * 고유 벡터의 순서에서 고유행렬 P를 구한다.
    * P^(-1) A P = Λ에서 Λ를 구한다.
    * A = P Λ P^(-1) 이다.
    * 이때 P가 직교행렬 Q이면, A = Q Λ Q^(T)도 성립한다.
* 특이값 분해 : SVD(single value decomposition), 특정한 구조로 분해.
    * M = U Σ V^(*)
    * M = mxn 행렬
    * U = mxm 유니터리 행렬
    * V = nxn 유니터리 행렬
    * Σ = mxn의 주대각선 외 모든 요소가 0인 행렬.
<br><br>

### [무어-펜로즈 유사역행렬]
* 가역 행렬의 역행렬 연산을 일반화. 특이값 분해를 통해 계산한다.
* 즉, 역행렬이 있던 없던 강제로 역행렬을 뽑아낸다.
* A = U Σ V^(*)이 성립할 때, A^(+) = V Σ U^(*)
* 반드시 존재하며, 단 1개만 존재한다.
<br><br>